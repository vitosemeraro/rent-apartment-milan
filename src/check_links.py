# Controlla link e immagini interne di dist/; con --pages crea deploy/ram-pages.zip senza la cartella img
import os, re, glob, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "dist")
bad = set()
for f in glob.glob(D + "/**/*.html", recursive=True):
    s = open(f, encoding="utf8").read()
    refs = re.findall(r'(?:href|src)="(/[^"#?]*)', s)
    refs += [u.strip().split(" ")[0] for x in re.findall(r'srcset="([^"]+)"', s) for u in x.split(",")]
    for h in refs:
        p = D + h + ("index.html" if h.endswith("/") else "")
        if not os.path.exists(p) and "contact.php" not in h:
            bad.add(h)
print("broken:", sorted(bad)[:30])
if "--pages" in sys.argv:
    out = os.path.join(HERE, "..", "deploy", "ram-pages.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, dn, fn in os.walk(D):
            rel_dir = os.path.relpath(dp, D).replace(os.sep, "/")
            if rel_dir == "img" or rel_dir.startswith("img/"):
                continue
            for f in fn:
                p = os.path.join(dp, f)
                z.write(p, os.path.relpath(p, D).replace(os.sep, "/"))
    print(out, os.path.getsize(out) // 1024, "KB")
sys.exit(1 if bad else 0)
