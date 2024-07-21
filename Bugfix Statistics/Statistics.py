from datetime import datetime
from re import search
from requests import get
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from bs4 import BeautifulSoup as bs
import numpy as np

current_year = datetime.now().year

updates_or_bugfixes = None
while True:
    updates_or_bugfixes = input("Обновления или Багфиксы? (о/б): ").lower().strip()
    if updates_or_bugfixes in ("б", "о"):
        break
    else:
        print("Некорректный ввод.")

if updates_or_bugfixes == "б":
    url_prefix = "https://yandere-simulator.fandom.com/ru/wiki/Обновления/Исправления_ошибок_"
else:
    url_prefix = "https://yandere-simulator.fandom.com/ru/wiki/Обновления/Обновления_"
addresses = [str(i) for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1)]
ru = {str(i):[] for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1)}
en = {str(i):[] for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1)}

for i in addresses:
    a = get(url_prefix+i)
    html = bs(a.content, "html.parser")
    for j in html.find_all("li", class_=""):
        if j.text[0].lower() not in "\n\t" and search(r"[А-Яа-я]", j.text):
            ru[i].append(j.text)
        elif j.text[0].lower() in "qwertyuiopasdfghjklzxcvbnm":
            en[i].append(j.text)

for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1):
    s = str(i)
    lenr = len(ru[s]) - 3  # Гарантировано три лишних элемента. 
    print(f"{s} = {lenr}/{len(en[s])+lenr}, {(lenr / (len(en[s])+lenr))*100:.2f}%")

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot()

x = np.arange(len(addresses)) + 2014 + (updates_or_bugfixes=="б")
y1 = [len(ru[str(i)])-3 for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1)]
y2 = [len(en[str(i)])+len(ru[str(i)])-3 for i in range(2014 + (updates_or_bugfixes=="б"), current_year+1)]
w = 0.3

ax.bar(x-w/2, y1, width=w)
ax.bar(x+w/2, y2, width=w)
ax.xaxis.set_major_locator(MultipleLocator(base=1))

plt.show()

