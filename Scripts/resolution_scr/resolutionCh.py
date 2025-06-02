from pathlib import Path
from PIL import Image

#projects = ["Cezerin", "nopCommerce", "prestashop", "shopizer"]
projects = ["medusa"]
base_dir = Path(r"C:\Diana\MasterCode\code\Projects")
source_subpath = Path("Processes/data/screenshots/source")
target_subpath = Path("Processes/data/screenshots/resolution")

sizes = {
    "672": (672, 672),
    "768": (768, 768),
    "1024": (1024, 1024)
}
for project in projects:
    source_root = base_dir / project / source_subpath
    target_root = base_dir / project / target_subpath
    png_files = list(source_root.rglob("*.png"))
    for source_path in png_files:
        relative_path = source_path.relative_to(source_root)
        with Image.open(source_path) as img:
            for size_name, size in sizes.items():
                target_path = target_root / size_name / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                img.resize(size).save(target_path)                      
print("FIN")