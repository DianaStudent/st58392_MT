import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Comment

input_root = Path(r"C:\Diana\Master\MasterCode\code\Projects\nopCommerce\Processes\data\getData\sourceData")
output_root = Path(r"C:\Diana\Master\MasterCode\code\Projects\nopCommerce\Processes\data\cleanData")
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
        ".topic-block", ".newsletter", ".swiper",
        ".ui-helper-hidden-accessible", ".advanced-search",
        ".product-viewmode", ".product-page-size",
        ".newsletter-subscribe", ".newsletter-result",
        ".product-sorting", ".footer-powered-by", 
        ".footer-lower", ".header-upper .header-links",  
    ]
    for selector in selectors_to_remove:
        for el in soup.select(selector):
            el.decompose()

    for btn in soup.select(".add-to-wishlist-button, .add-to-compare-list-button"):
        btn.decompose()
    for tag in soup.find_all(attrs={"onclick": True}):
        del tag["onclick"]

    for tag in soup.find_all(["div", "span", "ul", "li", "section", "aside", "nav"]):
        if not tag.get_text(strip=True) and not tag.find("img") and not tag.find("input"):
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

    tokens = soup.find_all("input", {"type": "hidden", "name": "__RequestVerificationToken"})
    for token in tokens[1:]:
        token.decompose()

    for token in soup.find_all("input", {"name": "__RequestVerificationToken"}):
        token.decompose()

    for footer in soup.find_all("div", {"class": "footer"}):
        footer.decompose()

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
