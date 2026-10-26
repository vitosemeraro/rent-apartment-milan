# Piano editoriale RAM – rent-apartment-milan.com

Fonte di verità per la routine settimanale che scrive e pubblica gli articoli. Ogni settimana la routine prende la prima riga con stato `todo`, scrive l'articolo nelle lingue indicate, aggiorna lo stato a `done` con la data e fa push: il deploy parte da solo.

## Obiettivo

Più visite organiche in target e più richieste di prenotazione diretta (modulo sulle schede appartamento) da: professionisti in trasferta, remote worker, studenti ed Erasmus, docenti e ricercatori in visita, visitatori delle fiere.

## Cosa dicono i dati (Search Console, 24/06/2025–23/10/2026)

- 97 clic, 10.300 impressioni, CTR 0,9%, posizione media 11,5. Il 62% delle impressioni arriva dal Regno Unito.
- Cluster principale: "no deposit" (cheap apartments milan no deposit, room for rent milan no deposit, monthly rent milan no deposit…): circa 800 impressioni in posizione 5–8 con CTR quasi zero.
- Ricerche tedesche per studenti ("studenten apartment mailand", "apartment mailand student") in posizione ~90: spazio per contenuti DE dedicati.
- "turro flats" in posizione 10: query locali su Turro/Precotto da presidiare.

## Regole per ogni articolo

1. Un intento di ricerca per articolo, keyword principale nel title (max 60 caratteri utili), nell'H1 e nel primo paragrafo.
2. 700–1.100 parole, frasi brevi, sottotitoli H2 che rispondono a domande reali, almeno una tabella o elenco pratico.
3. Solo fatti verificabili: prezzi e regole degli appartamenti da `src/data/pricing.json` e `src/common.py`, tempi di viaggio coerenti con le pagine esistenti. Niente promesse non vere (es. "vicino alla Bocconi").
4. Link interni: almeno 2 verso pagine guida esistenti e 1 verso una scheda appartamento; chiudere con invito a usare il calendario di prenotazione.
5. Front-matter: `lang`, `date` (giorno di pubblicazione), `title`, `description` (140–155 caratteri), `h1`, `image` (set:indice da `src/images.json`), `apts`.
6. File in `src/articles/AAAA-MM-GG-slug.md`; le versioni in altre lingue hanno slug tradotto. Un articolo con data futura resta nascosto fino a quel giorno (il deploy giornaliero lo pubblica).
7. Prima del push: `cd src && python build.py && python check_links.py` deve terminare senza link rotti.

## Coda

| # | Settimana | Tema e keyword principale | Lingue | Target | Stato |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-02 | How to rent in Milan without a deposit (rent apartment milan no deposit) | en, it | expat, studenti | todo |
| 2 | 2026-11-09 | Salone del Mobile 2027: where to stay and how to get to Rho Fiera | en, it, de | fiere | todo |
| 3 | 2026-11-16 | Studentenwohnung in Mailand: Kosten, Viertel, Verträge 2027 | de, en | studenti DE | todo |
| 4 | 2026-11-23 | Cheap monthly rent in Milan: realistic prices by area (monthly rent milan) | en, it | professionisti, studenti | todo |
| 5 | 2026-11-30 | Remote work from Milan for a month: fibre, desk, coworking near M1 | en, it | remote worker | todo |
| 6 | 2026-12-07 | Erasmus spring semester in Milan: housing checklist February 2027 | en, es, fr | Erasmus | todo |
| 7 | 2026-12-14 | Visiting professor or researcher at Bicocca: where to stay | en, it | docenti, ricercatori | todo |
| 8 | 2026-12-21 | Studio for rent in Milan with no deposit (studio rent milan no deposit) | en, it | studenti, giovani | todo |
| 9 | 2026-12-28 | MIDO, MICAM and February fairs 2027: apartments for teams | en, it, de | fiere | todo |
| 10 | 2027-01-04 | Codice fiscale, residence and lease: first week in Milan for expats | en, es | expat | todo |
| 11 | 2027-01-11 | Living in Turro and NoLo: the honest neighbourhood guide (turro flats) | en, it | tutti | todo |
| 12 | 2027-01-18 | Doctors and residents at Niguarda hospital: monthly apartments nearby | it, en | medici, specializzandi | todo |
| 13 | 2027-01-25 | Room vs whole studio in Milan: the real monthly cost compared | en, it, de | studenti | todo |
| 14 | 2027-02-01 | Internship in Milan: where to live for 3–6 months | en, it, fr | stagisti | todo |
| 15 | 2027-02-08 | Transitional lease explained for non-EU students (visa, permesso) | en, es | studenti extra UE | todo |
| 16 | 2027-02-15 | Milan Design Week on a budget: share an apartment for 8 | en, it, de, fr | fiere, gruppi | todo |

Dopo la riga 16 la routine propone nuovi temi partendo dalle query di Search Console in posizione 5–20 e dalle domande ricorrenti degli ospiti, e li aggiunge in coda.
