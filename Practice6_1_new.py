from bs4 import BeautifulSoup
import requests
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0 (Edition Yx GX)"
}

print("Вводить ссылку ввиде https://music.yandex.ru/artist/ id_артиста /tracks")
url = str(input("Вставьте ссылку на вашего любимого исполнителя - "))

try:
    req = requests.get(url, headers=header)
    src = req.text
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(src)

except Exception:
    print("Неправильно указана ссылка")
    exit()


with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_tracks = soup.find_all(class_="d-track__name")
count = 0
for track in all_tracks:
    track_text = track.text
    if count < 10:
        print(f'{count + 1} {track_text}')
        count += 1
