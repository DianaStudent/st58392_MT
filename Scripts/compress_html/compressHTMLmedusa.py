import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Comment

input_root = Path(r"C:\diana\MasterCode\code\Projects\medusa\Processes\data\getData\sourceData")
output_root = Path(r"C:\diana\MasterCode\code\Projects\medusa\Processes\data\cleanData")

def compress_html(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.head:
        soup.head.decompose()

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for el in soup.find_all(style=lambda s: s and "display: none" in s.lower()):
        el.decompose()

    for el in soup.select("[hidden], [aria-hidden='true'], .sr-only"):
        el.decompose()
    allowed_attrs = {"id", "href", "src", "alt", "type", "value", "name", "method", "action", "for", "title"}
    allowed_attrs |= {attr for tag in soup.find_all() for attr in tag.attrs if attr.startswith("data-testid") or attr.startswith("data-value")}

    important_tags = {"a", "button", "input", "select", "option", "img", "label", "form", "svg"}

    for tag in soup.find_all():
        tag.attrs = {k: v for k, v in tag.attrs.items() if k in allowed_attrs}

    for tag in soup.find_all(["div", "span", "section", "aside", "nav"]):
        has_attributes = tag.attrs and any(attr in tag.attrs for attr in allowed_attrs)
        has_text = bool(tag.get_text(strip=True))
        has_important_child = tag.find(important_tags)
        if not has_attributes and not has_text and not has_important_child:
            tag.decompose()

    body_html = str(soup.body or soup)
    body_html = re.sub(r'>\s+<', '><', body_html) 
    return body_html.strip()




def process_all():
    for json_file in input_root.rglob("*.json"):
        relative_path = json_file.relative_to(input_root)
        output_path = output_root / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        compressed_data = {key: compress_html(html) for key, html in data.items()}
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(compressed_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_all()
    print("FIN")
