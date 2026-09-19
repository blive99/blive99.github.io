import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://apitv.moneyclub999.com/ngz168/{}/playlist.m3u8"

START = 100
END = 200

OUTPUT_FILE = "working_links.txt"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def check_link(number):
    url = BASE_URL.format(number)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return None

        content = response.text

        # ตรวจว่าเป็น M3U8 จริง
        if "#EXTM3U" not in content:
            return None

        print(f"[OK] {number} -> {url}")

        return url

    except requests.RequestException:
        return None


def main():

    working_links = []

    print(f"Checking {START} - {END}...")

    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = [
            executor.submit(check_link, number)
            for number in range(START, END + 1)
        ]

        for future in as_completed(futures):

            result = future.result()

            if result:
                working_links.append(result)

    working_links.sort(
        key=lambda x: int(x.split("/ngz168/")[1].split("/")[0])
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        for url in working_links:
            f.write(url + "\n")

    print()
    print("================================")
    print(f"ตรวจทั้งหมด : {END - START + 1}")
    print(f"พบ M3U8    : {len(working_links)}")
    print(f"ผลลัพธ์     : {OUTPUT_FILE}")
    print("================================")


if __name__ == "__main__":
    main()
