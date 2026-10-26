# Impacchetta dist/ in zip da max ~9 MB per l'upload dal File Manager di cPanel
import os, zipfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "dist")
OUT = os.path.join(HERE, "..", "deploy")
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT, exist_ok=True)
for _f in os.listdir(OUT): os.remove(os.path.join(OUT, _f))
files = []
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        p = os.path.join(dp, f)
        files.append((os.path.relpath(p, ROOT).replace(os.sep, "/"), os.path.getsize(p)))
files.sort(key=lambda x: (x[0].startswith("img/"), x[0]))
chunks, cur, size, LIM = [], [], 0, 9_000_000
for rel, s in files:
    if size + s > LIM and cur:
        chunks.append(cur); cur, size = [], 0
    cur.append(rel); size += s
chunks.append(cur)
for i, c in enumerate(chunks, 1):
    zp = os.path.join(OUT, f"ram-{i:02d}.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in c:
            z.write(os.path.join(ROOT, rel), rel)
    print(i, len(c), os.path.getsize(zp) // 1024, "KB")
