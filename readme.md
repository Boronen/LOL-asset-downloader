\# League of Legends Asset Downloader (Splash Art, Chromas, Icons)



This is a multilingual command‑line tool for browsing and downloading various League of Legends visual assets.  

The program uses Riot Games’ official public data sources (Data Dragon and CommunityDragon) to retrieve splash arts, chroma icons, item icons, spell icons, and champion icons.



The tool automatically detects the Windows system language and adjusts the interface accordingly.



\---



\## Features



\### Splash Art Viewer and Downloader

\- Lists only real skins (chromas are excluded)

\- Retrieves splash arts directly from CommunityDragon

\- Allows downloading a single splash art or all splash arts for a champion



\### Chroma Icons

\- Lists all chromas for a selected champion

\- Downloads chroma icons from CommunityDragon

\- Supports downloading one or all chromas



\### Item Icons

\- Searches items by name in the selected language

\- Downloads item icons from Data Dragon



\### Spell Icons

\- Lists all spells for a champion

\- Downloads spell icons from Data Dragon



\### Champion Icons

\- Downloads champion portrait icons

\- Supports downloading one or all champion icons



\---



\## Supported Languages



The program automatically detects the Windows system language.  

If the detected language is supported, the interface switches to it.  

If not, the program defaults to English.



Supported languages:



\- Hungarian (hu\_HU)

\- English (en\_US)

\- Spanish (es\_ES)

\- German (de\_DE)

\- Polish (pl\_PL)



\---



\## How It Works



The program uses two official Riot‑maintained public data sources:



\### Data Dragon

Used for:

\- Champion icons

\- Item icons

\- Spell icons

\- Basic champion metadata



\### CommunityDragon

Used for:

\- Splash arts

\- Chroma icons

\- Accurate skin/chroma separation

\- High‑resolution asset paths



CommunityDragon is significantly more reliable for skins and chromas, which is why splash arts and chroma icons are retrieved from there.



\---



\## Usage



1\. Run the script with Python 3.10 or newer.

2\. The program detects your system language automatically.

3\. Choose an option from the main menu:

&#x20;  - Splash art

&#x20;  - Chroma icons

&#x20;  - Item icon

&#x20;  - Spell icon

&#x20;  - Champion icon

4\. Enter the requested champion or item name.

5\. The program displays the asset URL.

6\. You may choose to download the file and specify a target folder.



\---



\## Legal Notice



This project is not affiliated with Riot Games in any way.



All League of Legends assets, including but not limited to:

\- splash arts  

\- champion icons  

\- item icons  

\- spell icons  

\- chroma icons  

\- champion names  

\- item names  

\- ability names  



are the property of \*\*Riot Games, Inc.\*\*



This tool does not redistribute or modify Riot assets.  

It only provides direct links to publicly available files hosted on Riot‑owned servers (Data Dragon and CommunityDragon).



For Riot Games’ legal policies, refer to:



https://www.riotgames.com/en/legal



\---



\## Disclaimer



This tool is intended for educational and personal use only.  

Do not use it to redistribute or rehost Riot Games assets.  

Respect Riot’s intellectual property rights and terms of service.



\---



\## Requirements



\- Python 3.10+

\- Internet connection

\- `requests` library



\---



\## License



This project is released under the MIT License.  

You may modify or extend the code, but you must not claim ownership of Riot Games assets.

---

## About This Project

This is my first project of this type, and I built it mainly to learn how to work with external APIs, JSON data structures, and Python CLI tools.  
Because of that, there may be parts of the code that are not fully optimized, overly complicated, or simply unnecessary.

I’m always open to suggestions, improvements, or best‑practice advice.  
If you notice something that could be cleaner, faster, or more elegant, feel free to open an issue or submit a pull request.  
Any feedback is appreciated — this project is part of my learning journey.






