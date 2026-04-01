# League of Legends Asset Downloader  
### Splash Arts • Chromas • Item Icons • Spell Icons • Champion Icons

A multilingual command‑line tool for browsing and downloading various League of Legends visual assets.

The program uses Riot Games’ official public data sources (Data Dragon and CommunityDragon) to retrieve splash arts, chroma icons, item icons, spell icons, and champion icons.  
It automatically detects your Windows system language and adjusts the interface accordingly.

---

## Features

### Splash Art Viewer & Downloader
- Lists only real skins (chromas excluded)
- Retrieves splash arts directly from CommunityDragon
- Download one or all splash arts for a champion

### Chroma Icons
- Lists all chromas for a selected champion
- Downloads chroma icons from CommunityDragon
- Supports downloading one or all chromas

### Item Icons
- Searches items by name in the selected language
- Downloads item icons from Data Dragon

### Spell Icons
- Lists all spells for a champion
- Downloads spell icons from Data Dragon

### Champion Icons
- Downloads champion portrait icons
- Supports downloading one or all champion icons

---

## Supported Languages

The program detects your Windows system language automatically.  
If unsupported, it defaults to English.

Supported languages:
- Hungarian (hu_HU)
- English (en_US)
- Spanish (es_ES)
- German (de_DE)
- Polish (pl_PL)

---

## How It Works

### Data Dragon (DD)
Used for:
- Champion icons  
- Item icons  
- Spell icons  
- Basic champion metadata  

### CommunityDragon (CD)
Used for:
- Splash arts  
- Chroma icons  
- Accurate skin/chroma separation  
- High‑resolution asset paths  

CommunityDragon is more reliable for skins and chromas, so splash arts and chroma icons are retrieved from there.

---

## Usage

1. Run the script with Python 3.10+
2. The program detects your system language
3. Choose an option from the main menu:
   - Splash art  
   - Chroma icons  
   - Item icon  
   - Spell icon  
   - Champion icon  
4. Enter the requested champion or item name  
5. The program displays the asset URL  
6. You may choose to download the file and specify a target folder  

---

## Legal Notice

This project is not affiliated with Riot Games in any way.

All League of Legends assets — including but not limited to:
- splash arts  
- champion icons  
- item icons  
- spell icons  
- chroma icons  
- champion names  
- item names  
- ability names  

are the property of Riot Games, Inc.

This tool does not redistribute or modify Riot assets.  
It only provides direct links to publicly available files hosted on Riot‑owned servers.

Riot legal policies:  
https://www.riotgames.com/en/legal

---

## Disclaimer

This tool is intended for educational and personal use only.  
Do not redistribute or rehost Riot Games assets.  
Respect Riot’s intellectual property rights and terms of service.

---

## Requirements

- Python 3.10+
- Internet connection
- `requests` library

---

## License

Released under the MIT License.  
You may modify or extend the code, but you must not claim ownership of Riot Games assets.

---

## About This Project

This is my first project of this type, created mainly to learn how to work with external APIs, JSON structures, and Python CLI tools.  
Because of that, some parts of the code may be unoptimized, overly complicated, or simply unnecessary.

I’m open to suggestions, improvements, and best‑practice advice.  
If you notice something that could be cleaner, faster, or more elegant, feel free to open an issue or submit a pull request.  
Any feedback is appreciated — this project is part of my learning journey.
