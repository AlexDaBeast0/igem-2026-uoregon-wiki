
import yaml
from pathlib import Path

NAV_DATA = Path("_data/navigation.yml").resolve()
PAGES_DIR = Path("_pages").resolve()


with open(NAV_DATA, encoding="utf-8") as file:
    data = yaml.safe_load(file)

def find_pages(item):
    pages = []

    if isinstance(item, dict):
        if "title" in item and "url" in item:
            pages.append({
                "title": item["title"],
                "url": item["url"],
            })

        for value in item.values():
            pages.extend(find_pages(value))

    elif isinstance(item, list):
        for value in item:
            pages.extend(find_pages(value))

    return pages

def make_page(title, url, pages_dir=PAGES_DIR):
    url = url.removeprefix("/").removesuffix(".html")
    page_path = pages_dir / (url + ".md")
    try:
        page_path.touch(exist_ok=False)

        page_template = (
            f"---\n"
            f"layout: default\n"
            f"permalink: {url}\n"
            f"---\n"
            f"\n# {title}\n"
            f"This page was not created yet"
        )

        with open(page_path, "w") as f:
            f.write(page_template)
        print(f"made the {url} page")
    except FileExistsError:
        print(f"{url} page already exists")
        
pages = find_pages(data)

for page in pages:
    make_page(page["title"], page["url"])
    

