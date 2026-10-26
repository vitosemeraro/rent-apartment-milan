# Routine settimanale: articolo SEO

Eseguita ogni lunedì alle 07:00 (Europe/Rome) da una routine Claude su questo repository.

1. Leggi `EDITORIAL.md` e prendi la prima riga della coda con stato `todo`.
2. Scrivi l'articolo nelle lingue indicate seguendo le "Regole per ogni articolo" (uno file `.md` per lingua in `src/articles/`, data = oggi).
3. Controlla i fatti contro `src/data/pricing.json`, `src/common.py` e le pagine guida esistenti; non inventare prezzi, distanze o servizi.
4. Esegui `cd src && python build.py && python check_links.py`: nessun link rotto.
5. In `EDITORIAL.md` cambia lo stato della riga in `done AAAA-MM-GG` e, se la coda ha meno di 4 righe `todo`, aggiungi 4 nuovi temi motivati dai dati.
6. Commit su `main` con messaggio `Articolo: <titolo>` e push. Il workflow "Build e deploy" pubblica sul sito.
