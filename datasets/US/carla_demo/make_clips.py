import cv2, numpy as np, subprocess, json
SRC='/mnt/user-data/uploads/carla.mp4'
X0,Y0,X1,Y1=120,160,888,592
# (name, drive start, drive end, stop page start)
CLIPS=[('stop2_single_yellow',  96.0,122.8,123.0),
       ('stop3_right_turn_arrow',168.4,174.8,175.0),
       ('stop4_roundabout',      226.0,240.4,240.6),
       ('stop5_double_yellow',   290.4,309.6,309.8),
       ('stop6_left_arrow_solid_right',351.8,370.4,370.6),
       ('stop7_two_way_left_turn_lane',442.6,459.8,460.0)]
cap=cv2.VideoCapture(SRC)
def frame_at(t):
    cap.set(cv2.CAP_PROP_POS_MSEC,t*1000); ok,f=cap.read(); return f[Y0:Y1,X0:X1].copy()
def clean_still(img):
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
    hue=((h>80)&(h<100))|((h>50)&(h<75))|(h<8)|(h>170)
    strong=((s>110)&(v>120)&hue).astype(np.uint8)
    weak=((s>45)&(v>100)&hue).astype(np.uint8)
    n,lab,st,_=cv2.connectedComponentsWithStats(strong,8)
    mask=np.zeros_like(strong)
    for i in range(1,n):
        x,y,w,hh,a=st[i]
        if w>25 and hh>12 and a<0.35*w*hh:          # outline of a drawn box (possibly two overlapping boxes)
            x0,y0,x1,y1=max(0,x-6),max(0,y-6),x+w+6,y+hh+6
            mask[y0:y1,x0:x1]=np.maximum(mask[y0:y1,x0:x1],weak[y0:y1,x0:x1])
    mask=cv2.dilate(mask,np.ones((7,7),np.uint8))
    return cv2.inpaint(img,mask*255,4,cv2.INPAINT_TELEA), int(mask.sum())
out=[]
for name,a,b,sp in CLIPS:
    k=int(name[4])
    orig=f'/mnt/user-data/uploads/T9/Project/Reasoning_Drive/results/carla/20261113_185858_route1/frames/{k:02d}.png'
    still=cv2.imread(orig); masked='original stop frame'
    cv2.imwrite(f'clips/{name}_stop.png',still)
    a2,b2=a+0.3,b-0.3
    tmp=f'clips/_{name}_drive.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a2),'-to',str(b2),'-i',SRC,
        '-vf',f'crop={X1-X0}:{Y1-Y0}:{X0}:{Y0},scale=1280:720:flags=lanczos,fps=25','-an',
        '-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',tmp],check=True)
    tmp2=f'clips/_{name}_still.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-t','3','-i',f'clips/{name}_stop.png',
        '-vf','scale=1280:720:flags=lanczos,fps=25','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',tmp2],check=True)
    open('clips/_list.txt','w').write(f"file '_{name}_drive.mp4'\nfile '_{name}_still.mp4'\n")
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','clips/_list.txt','-c','copy','-movflags','+faststart',f'clips/{name}.mp4'],check=True)
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'clips/{name}.mp4'],capture_output=True,text=True).stdout)
    out.append((name,round(d,1),masked))
    print(name,round(d,1),'s, box pixels removed',masked)
