import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Comment

input_root = Path(r"C:\diana\MasterCode\code\Projects\prestashop\Processes\data\getData\sourceData")
output_root = Path(r"C:\diana\MasterCode\code\Projects\prestashop\Processes\data\cleanData")

def compress_html(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style"]): tag.decompose()
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)): c.extract()

    for sel in [
        ".header-banner", ".footer", "#footer", ".page-footer", "#_desktop_logo",
        ".wishlist", "[class*='wishlist']", ".quick-view", ".product-list-reviews",
        ".product-flags", ".highlighted-informations", ".carousel", ".swiper",
        ".banner", ".block_newsletter", ".custom-text", "#custom-text",
        ".modal-backdrop", ".block-contact", ".search-widgets"
    ]:
        for el in soup.select(sel): el.decompose()

    for el in soup.find_all(style=lambda s: s and "display: none" in s.lower()): el.decompose()
    for el in soup.select("[hidden], [aria-hidden='true'], .sr-only"): el.decompose()

    for tag in soup.find_all(): tag["__keep"] = False
    for sel in [
        ".js-product", ".product-title", "button.add-to-cart",
        "#top-menu", "#main", "#wrapper", "#content-wrapper",
        ".modal-content", ".modal-title", "a[href*='/9-art']"
    ]:
        for el in soup.select(sel):
            el["__keep"] = True
            for p in el.parents:
                if p and p.name != "[document]": p["__keep"] = True

    for tag in list(soup.find_all()):
        if tag and not tag.has_attr("__keep"): tag.decompose()
        elif "__keep" in tag.attrs: del tag.attrs["__keep"]

    for tag in soup.find_all():
        tag.attrs = {k: v for k, v in tag.attrs.items()
                     if k in {"id", "class", "href", "type", "value", "name", "method", "action", "for"}}

    for tag in soup.find_all(["div", "span", "section", "aside", "nav"]):
        if not tag.get_text(strip=True) and not tag.find(["input", "a", "button", "form", "img"]): tag.decompose()

    return re.sub(r'\s+', ' ', str(soup.body or soup)).strip()





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
