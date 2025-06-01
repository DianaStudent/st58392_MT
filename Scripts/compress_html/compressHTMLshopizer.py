import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Comment

input_root = Path(r"C:\Diana\Master\MasterCode\code\Projects\shopizer\Processes\data\getData\sourceData")
output_root = Path(r"C:\Diana\Master\MasterCode\code\Projects\shopizer\Processes\data\cleanData")

def compress_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for el in soup.find_all(style=lambda s: s and "display: none" in s):
        if "There are" not in el.get_text(strip=True):
            el.decompose()
    for input_tag in soup.find_all("input", {"type": "hidden"}):
        if input_tag.get("name") != "__RequestVerificationToken":
            input_tag.decompose()

    selectors_to_remove = [
        ".newsletter", ".swiper", ".footer", ".footer-block",
        ".ui-helper-hidden-accessible", ".bar-notification-container",
        "#bar-notification", "#dialog-notifications-success", "#dialog-notifications-error",
        "#dialog-notifications-warning", ".newsletter-subscribe", ".newsletter-result",
        ".react-toast-notifications__container"
    ]

    for selector in selectors_to_remove:
        for el in soup.select(selector):
            el.decompose()
    for btn in soup.select(".add-to-wishlist-button, .add-to-compare-list-button"):
        btn.decompose()

    for tag in soup.find_all(["div", "span", "ul", "li", "section", "aside", "nav"]):
        if not tag.get_text(strip=True) and not tag.find(["input", "a", "button", "form", "img"]):
            tag.decompose()

    for tag in soup.find_all():
        for attr in ["class", "id", "style"]:
            if tag.has_attr(attr) and not tag[attr]:
                del tag[attr]

    tokens = soup.find_all("input", {"type": "hidden", "name": "__RequestVerificationToken"})
    for token in tokens[1:]:
        token.decompose()

    body = soup.body or soup
    cleaned = str(body)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

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
