# Nuovo sito rent-apartment-milan.com: stato lavori (25 ott 2026)

## Fatto
- Sito statico in 5 lingue (EN alla radice, /it/ /es/ /fr/ /de/), 90 pagine, generato da `src/build.py` in `dist/`.
- Contenuti per lingua in `src/lang_*.py`; fatti degli annunci e configurazione in `src/common.py`; recensioni in `src/data/reviews.json`.
- Foto: `src/img_pipeline.py` (WebP 480/960/1600). Fonti: CaseAffitti (Turro, Val di Non), SitoGAB/Clienti/MariaGrazia/Foto (MM, PA), foto personali ritoccate.
- `src/static/.htaccess`: 301 dai vecchi URL WordPress, 410 per le pagine demo, HTTPS, cache. `contact.php` invia a hello@rent-apartment-milan.com.
- Layout: proposte A/B/C in `proposte/` (seed casuale in `seed.txt`); applicata la A "Linea M1".
- Lighthouse mobile: performance 100, SEO 100.
- Piano editoriale e keyword: documento Claude nell'account RCS (https://claude.ai/artifact/SiVbds9V3Fu7myuzQ2hvs1).

## Da fare (serve Claude in Chrome sullo stesso account Claude dell'app, profilo Chrome personale, mai quello RCS)
1. Leggere GA4 (G-83KEV6QRN8) e Search Console: query, pagine, paesi; ordinare le keyword.
2. Airbnb: recensioni 5 stelle in `src/data/reviews.json`, verificare Superhost (`CONFIG["superhost"]` in common.py), link annunci MM e Turro, numero bagni MM.
3. Chiedere a Vito i codici CIN dei 4 alloggi e conferma "niente tre mesi di deposito".
4. cPanel Netsons: backup completo WP (file + DB), spostare WP fuori da public_html, caricare `dist/` (zip ed estrai), testare redirect e modulo.
5. cPanel Email: inoltro hello@rent-apartment-milan.com -> vsemeraro@gmail.com.
6. Search Console: inviare sitemap.xml.

Ricostruire dopo modifiche: `cd src && python build.py`
