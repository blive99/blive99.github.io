import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://doodii1.ufxplay.com/lowq/m{}/index.m3u8"

START = 19880700
END   = 19880799

TIMEOUT = 5
WORKERS = 20

headers = {
    "User-Agent": "Mozilla/5.0"
}

def check(number):
    url = BASE.format(number)

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=TIMEOUT,
            allow_redirects=True
        )

        if r.status_code == 200:
            content = r.text[:1000]

            # ตรวจว่าเป็น HLS playlist จริงหรือไม่
            if "#EXTM3U" in content:
                return number, url, "OK"

            return number, url, "HTTP 200 แต่ไม่ใช่ M3U8"

        return number, url, f"HTTP {r.status_code}"

    except requests.RequestException as e:
        return number, url, f"ERROR: {type(e).__name__}"


def main():

    numbers = range(START, END + 1)

    found = []

    with ThreadPoolExecutor(max_workers=WORKERS) as executor:

        futures = [
            executor.submit(check, n)
            for n in numbers
        ]

        for future in as_completed(futures):

            number, url, status = future.result()

            if status == "OK":
                print(f"[OK] {url}")
                found.append(url)

            elif "HTTP 200" in status:
                print(f"[?] {url} - {status}")

    with open("working.txt", "w", encoding="utf-8") as f:
        for url in sorted(found):
            f.write(url + "\n")

    print()
    print(f"พบลิงก์ที่ใช้งานได้: {len(found)}")
    print("บันทึกไว้ที่ working.txt")


if __name__ == "__main__":
    main()
