import requests
import locale
from pathlib import Path

DD = "https://ddragon.leagueoflegends.com"
CD = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default"

SUPPORTED_LANGS = {
    "hu": "hu_HU",
    "en": "en_US",
    "es": "es_ES",
    "de": "de_DE",
    "pl": "pl_PL",
}

TEXT = {
    "main_menu_title": {
        "hu_HU": "Mit szeretnél megnézni?",
        "en_US": "What would you like to view?",
        "es_ES": "¿Qué quieres ver?",
        "de_DE": "Was möchtest du ansehen?",
        "pl_PL": "Co chcesz zobaczyć?",
    },
    "main_menu": {
        "hu_HU": "1 - Splash art\n2 - Chroma ikonok\n3 - Item ikon\n4 - Spell ikon\n5 - Champion ikon\n0 - Kilépés",
        "en_US": "1 - Splash art\n2 - Chroma icons\n3 - Item icon\n4 - Spell icon\n5 - Champion icon\n0 - Exit",
        "es_ES": "1 - Splash art\n2 - Iconos de chroma\n3 - Icono de objeto\n4 - Icono de habilidad\n5 - Icono de campeón\n0 - Salir",
        "de_DE": "1 - Splash-Art\n2 - Chroma-Icons\n3 - Gegenstands-Icon\n4 - Zauber-Icon\n5 - Champion-Icon\n0 - Beenden",
        "pl_PL": "1 - Splash art\n2 - Ikony chroma\n3 - Ikona przedmiotu\n4 - Ikona umiejętności\n5 - Ikona bohatera\n0 - Wyjście",
    },
    "prompt_choice": {
        "hu_HU": "Választás: ",
        "en_US": "Choice: ",
        "es_ES": "Opción: ",
        "de_DE": "Auswahl: ",
        "pl_PL": "Wybór: ",
    },
    "prompt_champion_name": {
        "hu_HU": "Champion neve: ",
        "en_US": "Champion name: ",
        "es_ES": "Nombre del campeón: ",
        "de_DE": "Champion-Name: ",
        "pl_PL": "Nazwa bohatera: ",
    },
    "available_skins": {
        "hu_HU": "Elérhető skinek:",
        "en_US": "Available skins:",
        "es_ES": "Skins disponibles:",
        "de_DE": "Verfügbare Skins:",
        "pl_PL": "Dostępne skiny:",
    },
    "prompt_skin_id": {
        "hu_HU": "Skin ID (üres = összes): ",
        "en_US": "Skin ID (empty = all): ",
        "es_ES": "ID del skin (vacío = todos): ",
        "de_DE": "Skin-ID (leer = alle): ",
        "pl_PL": "ID skina (puste = wszystkie): ",
    },
    "chromas_available": {
        "hu_HU": "Elérhető chromák:",
        "en_US": "Available chromas:",
        "es_ES": "Chromas disponibles:",
        "de_DE": "Verfügbare Chromas:",
        "pl_PL": "Dostępne chromy:",
    },
    "prompt_chroma_id": {
        "hu_HU": "Chroma ID (üres = összes): ",
        "en_US": "Chroma ID (empty = all): ",
        "es_ES": "ID del chroma (vacío = todos): ",
        "de_DE": "Chroma-ID (leer = alle): ",
        "pl_PL": "ID chroma (puste = wszystkie): ",
    },
    "spells_label": {
        "hu_HU": "Spellek:",
        "en_US": "Spells:",
        "es_ES": "Habilidades:",
        "de_DE": "Zauber:",
        "pl_PL": "Umiejętności:",
    },
    "prompt_spell_index": {
        "hu_HU": "Spell index (üres = összes): ",
        "en_US": "Spell index (empty = all): ",
        "es_ES": "Índice de habilidad (vacío = todas): ",
        "de_DE": "Zauber-Index (leer = alle): ",
        "pl_PL": "Indeks umiejętności (puste = wszystkie): ",
    },
    "link_label": {
        "hu_HU": "Link:",
        "en_US": "Link:",
        "es_ES": "Enlace:",
        "de_DE": "Link:",
        "pl_PL": "Link:",
    },
    "ask_download": {
        "hu_HU": "Le szeretnéd tölteni? (i/n): ",
        "en_US": "Download it? (y/n): ",
        "es_ES": "¿Descargar? (s/n): ",
        "de_DE": "Herunterladen? (j/n): ",
        "pl_PL": "Pobrać? (t/n): ",
    },
    "ask_folder": {
        "hu_HU": "Mappa elérési útja: ",
        "en_US": "Folder path: ",
        "es_ES": "Ruta de carpeta: ",
        "de_DE": "Ordnerpfad: ",
        "pl_PL": "Ścieżka folderu: ",
    },
    "downloaded_to": {
        "hu_HU": "Letöltve ide:",
        "en_US": "Downloaded to:",
        "es_ES": "Descargado en:",
        "de_DE": "Heruntergeladen nach:",
        "pl_PL": "Pobrano do:",
    },
    "invalid_choice": {
        "hu_HU": "Érvénytelen választás.",
        "en_US": "Invalid choice.",
        "es_ES": "Opción inválida.",
        "de_DE": "Ungültige Auswahl.",
        "pl_PL": "Nieprawidłowy wybór.",
    },
    "champ_not_found": {
        "hu_HU": "Champion nem található.",
        "en_US": "Champion not found.",
        "es_ES": "Campeón no encontrado.",
        "de_DE": "Champion nicht gefunden.",
        "pl_PL": "Bohater nie znaleziony.",
    },
}


def detect_windows_language():
    try:
        lang, enc = locale.getlocale()
        if lang is None:
            lang = "en_US"
    except:
        lang = "en_US"

    short = lang.split("_")[0].lower()
    return SUPPORTED_LANGS.get(short, "en_US")


def get_latest_version():
    return requests.get(f"{DD}/api/versions.json").json()[0]


def normalize_champion_name(name):
    cleaned = (
        name.replace(" ", "")
            .replace("'", "")
            .replace("-", "")
            .replace(".", "")
    )
    return cleaned[0].upper() + cleaned[1:]


def ensure_folder(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def download_file(url, folder, filename, locale):
    folder = ensure_folder(folder)
    path = folder / filename
    data = requests.get(url).content
    path.write_bytes(data)
    print(TEXT["downloaded_to"][locale], path.resolve())


def ask_download(url, locale):
    print(TEXT["link_label"][locale], url)
    yes = {"hu_HU": "i", "en_US": "y", "es_ES": "s", "de_DE": "j", "pl_PL": "t"}[locale]
    ans = input(TEXT["ask_download"][locale]).strip().lower()
    if ans == yes:
        folder = input(TEXT["ask_folder"][locale]).strip()
        if not folder:
            folder = "."
        filename = url.split("/")[-1]
        download_file(url, folder, filename, locale)


def menu_splash(version, locale):
    champ = input(TEXT["prompt_champion_name"][locale])
    champ_norm = normalize_champion_name(champ)

    data = requests.get(f"{DD}/cdn/{version}/data/en_US/champion/{champ_norm}.json")
    if data.status_code != 200:
        print(TEXT["champ_not_found"][locale])
        return

    skins = data.json()["data"][champ_norm]["skins"]

    real_skins = []
    for s in skins:
        skin_id = s["num"]
        url = f"{DD}/cdn/img/champion/splash/{champ_norm}_{skin_id}.jpg"
        resp = requests.get(url)
        if resp.status_code == 200:
            real_skins.append(s)

    print(TEXT["available_skins"][locale])
    for s in real_skins:
        print(f"{s['num']} - {s['name']}")

    skin_id = input(TEXT["prompt_skin_id"][locale]).strip()

    if skin_id == "":
        for s in real_skins:
            url = f"{DD}/cdn/img/champion/splash/{champ_norm}_{s['num']}.jpg"
            ask_download(url, locale)
    else:
        if not any(s["num"] == int(skin_id) for s in real_skins):
            print("Ehhez a skinhez nincs splash art (valószínűleg chroma).")
            return

        url = f"{DD}/cdn/img/champion/splash/{champ_norm}_{skin_id}.jpg"
        ask_download(url, locale)



def menu_chromas(locale):
    champ = input(TEXT["prompt_champion_name"][locale])
    champ_norm = normalize_champion_name(champ)

    # champion-summary.json – ez a helyes lista
    champ_list = requests.get(f"{CD}/v1/champion-summary.json").json()
    champ_id = None
    for c in champ_list:
        if c["alias"].lower() == champ_norm.lower():
            champ_id = c["id"]
            break

    if champ_id is None:
        print(TEXT["champ_not_found"][locale])
        return

    # Teljes champion adat
    data = requests.get(f"{CD}/v1/champions/{champ_id}.json").json()

    # Chromák a skineken belül vannak
    chromas = []
    for skin in data.get("skins", []):
        for ch in skin.get("chromas", []):
            chromas.append({
                "id": ch["id"],
                "name": ch.get("name", "Unknown")
            })

    if not chromas:
        print("Nincs chroma ehhez a championhoz.")
        return

    print(TEXT["chromas_available"][locale])
    for c in chromas:
        print(f"{c['id']} - {c['name']}")

    chroma_id = input(TEXT["prompt_chroma_id"][locale]).strip()

    if chroma_id == "":
        for c in chromas:
            url = f"{CD}/v1/champion-chroma-images/{champ_id}/{c['id']}.png"
            ask_download(url, locale)
    else:
        url = f"{CD}/v1/champion-chroma-images/{champ_id}/{chroma_id}.png"
        ask_download(url, locale)



def menu_item(version, locale):
    data = requests.get(f"{DD}/cdn/{version}/data/{locale}/item.json").json()["data"]

    name = input("Item neve: ").strip().lower()

    for item_id, item in data.items():
        if item["name"].lower() == name:
            url = f"{DD}/cdn/{version}/img/item/{item_id}.png"
            ask_download(url, locale)
            return

    print("Item nem található.")


def menu_spell(version, locale):
    champ = input(TEXT["prompt_champion_name"][locale])
    champ_norm = normalize_champion_name(champ)

    data = requests.get(f"{DD}/cdn/{version}/data/{locale}/champion/{champ_norm}.json")
    if data.status_code != 200:
        print(TEXT["champ_not_found"][locale])
        return

    spells = data.json()["data"][champ_norm]["spells"]

    print(TEXT["spells_label"][locale])
    for i, sp in enumerate(spells):
        print(f"{i} - {sp['name']}")

    idx = input(TEXT["prompt_spell_index"][locale]).strip()

    if idx == "":
        for sp in spells:
            icon = sp["image"]["full"]
            url = f"{DD}/cdn/{version}/img/spell/{icon}"
            ask_download(url, locale)
    else:
        idx = int(idx)
        icon = spells[idx]["image"]["full"]
        url = f"{DD}/cdn/{version}/img/spell/{icon}"
        ask_download(url, locale)


def menu_champ_icon(version, locale):
    champ = input(TEXT["prompt_champion_name"][locale])
    champ_norm = normalize_champion_name(champ)

    url = f"{DD}/cdn/{version}/img/champion/{champ_norm}.png"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(TEXT["champ_not_found"][locale])
        return

    ask_download(url, locale)


def main():
    version = get_latest_version()
    locale = detect_windows_language()

    while True:
        print()
        print(TEXT["main_menu_title"][locale])
        print(TEXT["main_menu"][locale])
        choice = input(TEXT["prompt_choice"][locale]).strip()

        if choice == "1":
            menu_splash(version, locale)
        elif choice == "2":
            menu_chromas(locale)
        elif choice == "3":
            menu_item(version, locale)
        elif choice == "4":
            menu_spell(version, locale)
        elif choice == "5":
            menu_champ_icon(version, locale)
        elif choice == "0":
            break
        else:
            print(TEXT["invalid_choice"][locale])


if __name__ == "__main__":
    main()
