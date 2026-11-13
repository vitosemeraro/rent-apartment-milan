"""Riassume il contatore anonimo ev-stats.php in conteggi giornalieri per evento.

Uso: python tools/ev_conteggi.py ev-stats.json > ev-conteggi.json
Lo usa il workflow "Contatore eventi" e lo leggono le routine della Regia:
il campo "lead" conta gli invii dei moduli (prenotazione e contatto), anche
di chi rifiuta i cookie, perché ev.php non usa cookie.
"""
import json
import sys
from datetime import date, timedelta, datetime, timezone


def somma(giorni, evento, da, a):
    return sum(n for g, ev in giorni.items() if da <= g <= a for e, n in ev.items() if e == evento)


def main(path):
    dati = json.load(open(path, encoding="utf-8"))
    giorni = {}
    for r in dati.get("rows", []):
        g = giorni.setdefault(r["day"], {})
        g[r["e"]] = g.get(r["e"], 0) + int(r["n"])
    oggi = datetime.now(timezone.utc).date()
    ieri = oggi - timedelta(days=1)
    fine_28 = ieri.isoformat()
    inizio_28 = (ieri - timedelta(days=27)).isoformat()
    fine_prev = (ieri - timedelta(days=28)).isoformat()
    inizio_prev = (ieri - timedelta(days=55)).isoformat()
    out = {
        "fonte": "https://rent-apartment-milan.com/ev-stats.php?days=120",
        "aggiornato_il": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "dal": dati.get("since"),
        "periodo_28g": [inizio_28, fine_28],
        "periodo_prev": [inizio_prev, fine_prev],
        "lead_28g": somma(giorni, "lead", inizio_28, fine_28),
        "lead_prev": somma(giorni, "lead", inizio_prev, fine_prev),
        "view_28g": somma(giorni, "view", inizio_28, fine_28),
        "view_prev": somma(giorni, "view", inizio_prev, fine_prev),
        "giorni": dict(sorted(giorni.items())),
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main(sys.argv[1])
