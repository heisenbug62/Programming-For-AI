import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.newegg.com/p/pl"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.newegg.com/"
}

def get_page(page):
    params = {
        "d": "gaming mouse",
        "page": page
    }

    r = requests.get(BASE_URL, headers=HEADERS, params=params)

    if r.status_code != 200:
        print("Blocked or error:", r.status_code)
        return None

    return BeautifulSoup(r.text, "html.parser")


def extract_image(tag):
    img = tag.select_one("img")

    if not img:
        return "N/A"

    # Newegg sometimes uses lazy loading
    return img.get("src") or img.get("data-src") or "N/A"


def parse_items(soup):
    products = []

    items = soup.select("div.item-cell")

    for item in items:
        try:
            title_tag = item.select_one("a.item-title")
            title = title_tag.text.strip() if title_tag else "N/A"

            price_tag = item.select_one("li.price-current")
            price = price_tag.text.strip() if price_tag else "N/A"

            image = extract_image(item)

            products.append({
                "title": title,
                "price": price,
                "image_url": image
            })

        except Exception:
            continue

    return products


def scrape(target=1000):
    all_data = []
    page = 1

    while len(all_data) < target:
        print(f"Scraping page {page}...")

        soup = get_page(page)
        if not soup:
            break

        data = parse_items(soup)

        if not data:
            break

        all_data.extend(data)

        print("Collected:", len(all_data))

        page += 1
        time.sleep(2)

    return all_data[:target]


def save_csv(data):
    with open("newegg_products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = scrape(1000)
    save_csv(data)
    print("Done! Saved to newegg_products.csv")