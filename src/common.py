# Dati condivisi tra le lingue: configurazione e fatti degli annunci (modificare qui, poi python build.py)
SITE = "https://rent-apartment-milan.com"
import os
LANGS = os.environ.get("RAM_LANGS", "en,it,es,fr,de").split(",")
LANG_NAMES = {"en": "English", "it": "Italiano", "es": "Español", "fr": "Français", "de": "Deutsch"}

CONFIG = {
    "default_lang": "en",
    "email": "hello@rent-apartment-milan.com",
    "ga4": "G-83KEV6QRN8",
    "cf_beacon": "bdb20b4430954040b846f08a6de1b21c",  # Cloudflare Web Analytics: senza cookie, non serve consenso
    # NAP allineato alla scheda Google Business "Rent Apartment Milan"
    "phone": "+39 328 061 4612", "street": "Via Jean Jaurès 7/B", "zip": "20125",
    "same_as": ["https://www.google.com/maps?cid=13234886842758471390"],
    "superhost": True,        # True solo dopo verifica sul profilo Airbnb
    "rating": "5.0",
    "reviews_total": 25,
    "reviews_count": 0,        # aggiornato da data/reviews.json
    "guides": ["nodeposit", "monthly", "students", "bicocca", "fairs", "neighborhood", "contract"],
}

# photos = nome del set in images.json (se manca usa un set di riserva)
LISTINGS = {
    "mm": {"status": "live", "photos": "mmall", "cover": 0, "guests": 8, "bedrooms": 2, "rooms_n": 4, "baths": 2,
           "price_from": 85, "airbnb": "https://www.airbnb.it/rooms/1532669644773856892", "street": "Precotto", "cin": "IT015146C2ACBNX55O", "rating": "5,0", "nrev": 18, "superhost": True},
    "pa": {"status": "soon", "photos": "pa", "cover": 0, "guests": 4, "bedrooms": 1, "rooms_n": 2, "baths": 1,
           "price_from": None, "airbnb": "", "street": "Precotto", "cin": "IT015146C2ACBNX55O"},
    "turro": {"status": "live", "photos": "turro", "cover": 1, "guests": 2, "bedrooms": 0, "rooms_n": 1, "baths": 1,
              "floor_m2": 38, "price_from": None, "airbnb": "https://www.airbnb.it/rooms/856641617814684128", "street": "Via Jean Jaurès", "cin": "IT015146C2F8332Y8Z", "rating": "5,0", "nrev": 7, "guestfav": True},
    "vdn": {"status": "live", "photos": "valdinon", "cover": 0, "guests": 2, "bedrooms": 1, "rooms_n": 2, "baths": 1,
            "price_from": None, "airbnb": "https://www.airbnb.it/rooms/1804250398568015528", "street": "Via Val di Non 26", "cin": "IT015146C2CE7SCUCM"},
}
