# Converte le foto sorgente in WebP responsive (480/960/1600) + JPG fallback 1600
import os, sys, json
from PIL import Image, ImageOps
B=r"C:/Users/vito.semeraro/OneDrive - RCS MediaGroup/Desktop/OneDrive/Desktop/CaseAffitti"
T=os.environ['TEMP']+"/ramphotos/out"
OUT=os.path.join(os.path.dirname(__file__),"..","dist","img")
sets={
 "turro":[B+"/Foto Jaures/Selezionate/"+f for f in ["IMG_6651 copia.jpg","_DSC0003 copia.jpg","IMG_6636 copia.jpg","_DSC0017 copia.jpg","IMG_6655 copia.jpg","IMG_6656 copia.jpg","_DSC0007 copia.jpg","cucina.png","2.png","3.png","4 (2).png"]],
 "valdinon":[B+"/FotoPrima-Dopo/ValDiNon/staged2/bright_airy/"+f for f in ["03_DSC0009_bright_airy.jpg","01_DSC0001_bright_airy.jpg","02_DSC0002_bright_airy.jpg","04_DSC0008_bright_airy.jpg","05_DSC0015_bright_airy.jpg","06_DSC0017_bright_airy.jpg","07_DSC0020_bright_airy.jpg","08_DSC0027_bright_airy.jpg","09_DSC0024_bright_airy.jpg","10_DSC0030_bright_airy.jpg"]]+[B+"/FotoPrima-Dopo/ValDiNon/staged2/bright_airy/aggiuntive/"+f for f in ["11_DSC0006_bright_airy.jpg","12_DSC0019_bright_airy.jpg","13_DSC0016_bright_airy.jpg","14_DSC0025_bright_airy.jpg"]],
 "vito":[T+"/"+f+".jpg" for f in ["vito-host-ritratto","vito-host-quadrato","vito-gestione-telefono","vito-hero","vito-laptop","vito-come-lavoro"]],
}
import json as _j
_mp=_j.load(open(os.environ['TEMP']+"/ramphotos/mmpa_list.json"))
sets["mm"]=[_mp["mm"][i] for i in [28,8,37,30,12,15,18,22,3,26,41,0,43,7]]
sets["pa"]=[_mp["pa"][i] for i in [21,51,14,30,24,44,55,36,8,10,6,3,15,42]]
only=os.environ.get("ONLY")
if only: sets={k:v for k,v in sets.items() if k in only.split(",")}
extra=sys.argv[1:]  # dir:name pairs per set aggiuntivi
for e in extra:
    d,n=e.split("::"); sets[n]=[os.path.join(d,f) for f in sorted(os.listdir(d)) if f.lower().endswith(('.jpg','.jpeg','.png','.webp'))]
meta={}
for name,files in sets.items():
    os.makedirs(os.path.join(OUT,name),exist_ok=True); meta[name]=[]
    for i,f in enumerate(files,1):
        im=ImageOps.exif_transpose(Image.open(f)).convert("RGB")
        base=f"{name}-{i:02d}" if name!="vito" else os.path.splitext(os.path.basename(f))[0]
        r=im.width/im.height
        for w in (480,960,1600):
            if w>im.width and w!=480: continue
            x=im.resize((w,round(w/r)),Image.LANCZOS)
            x.save(os.path.join(OUT,name,f"{base}-{w}.webp"),quality=76 if w>480 else 72,method=6)
        x=im.resize((min(1600,im.width),round(min(1600,im.width)/r)),Image.LANCZOS)
        x.save(os.path.join(OUT,name,f"{base}.jpg"),quality=80,optimize=True,progressive=True)
        meta[name].append({"base":base,"w":x.width,"h":x.height})
jp=os.path.join(os.path.dirname(__file__),"images.json")
old=json.load(open(jp)) if os.path.exists(jp) else {}
old.update(meta); json.dump(old,open(jp,"w"),indent=1)
print({k:len(v) for k,v in meta.items()})
