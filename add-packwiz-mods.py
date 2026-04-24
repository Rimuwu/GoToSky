from pathlib import Path
import re

source_path = Path(r"C:/Users/AS1/Desktop/GoToSky/modlist.html")
if not source_path.exists():
    raise FileNotFoundError(source_path)
source = source_path.read_text(encoding="utf-8")
urls = re.findall(r'href="([^"]+)"', source)
if not urls:
    raise SystemExit("No URLs found in modlist.html")
script_path = Path("add-packwiz-mods.ps1")
with script_path.open("w", encoding="utf-8") as f:
    f.write("# Auto-generated packwiz import script\n")
    f.write("cd \"C:/Users/AS1/Desktop/GoToSky/modpack\"\n")
    for url in urls:
        f.write(f'packwiz curseforge add "{url}" -y\n')
print(f"Wrote {len(urls)} commands to {script_path}")
