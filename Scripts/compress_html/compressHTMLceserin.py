import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Comment

source_dir = Path(r"C:\Diana\Master\MasterCode\code\Projects\Cezerin\Processes\data\getData\sourceData")
target_dir = Path(r"C:\Diana\Master\MasterCode\code\Projects\Cezerin\Processes\data\cleanData")

target_dir.mkdir(parents=True, exist_ok=True)

def compress_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    selectors_to_remove = [
        ".header", ".footer", ".topic-block", ".newsletter", ".swiper",
        ".footer-block", ".ui-helper-hidden-accessible", ".header-upper",
        ".header-lower", ".search-box", ".header-menu", ".bar-notification-container",
        "#bar-notification", "#dialog-notifications-success", "#dialog-notifications-error",
        "#dialog-notifications-warning", ".newsletter-subscribe", ".newsletter-result",
        ".product-viewmode", ".product-page-size"
    ]
    for selector in selectors_to_remove:
        for el in soup.select(selector):
            el.decompose()
    for btn in soup.select(".add-to-wishlist-button, .add-to-compare-list-button"):
        btn.decompose()
    for tag in soup.find_all(["div", "span", "ul", "li", "section", "aside", "nav"]):
        if not tag.get_text(strip=True) and not tag.find("img"):
            tag.decompose()
    for tag in soup.find_all():
        for attr in ["class", "id", "style"]:
            if tag.has_attr(attr) and not tag[attr]:
                del tag[attr]
    for li in soup.select("li.tab-section"):
        if "active" not in li.get("class", []):
            li.decompose()
    for logo in soup.select(".payment-logo"):
        logo.decompose()
    for back in soup.select(".back-link"):
        back.decompose()
    body = soup.body or soup
    cleaned = str(body)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()


def process_all_jsons():
    json_files = list(source_dir.glob("*.json"))

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        compressed_data = {key: compress_html(html) for key, html in data.items()}

        output_path = target_dir / json_file.name
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(compressed_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_all_jsons()
    print("FIN")
