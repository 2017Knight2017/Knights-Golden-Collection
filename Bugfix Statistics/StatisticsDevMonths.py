from datetime import datetime
from re import search
from requests import get
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from bs4 import BeautifulSoup as bs
import numpy as np

CURRENT_YEAR = datetime.now().year

UPDATES_OR_BUGFIXES = ""
while True:
	UPDATES_OR_BUGFIXES = input("Improvements or bugfixes? (i/b): ").lower().strip()
	if UPDATES_OR_BUGFIXES in ("i", "b"):
		break
	else:
		print("Incorrect input.")

MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
MONTHS_en = ["January", "February", "March", "April", "May", "June",
          	 "July", "August", "September", "October", "November", "December"]

if UPDATES_OR_BUGFIXES == "b":
	url_prefix = "https://yandere-simulator.fandom.com/ru/wiki/Обновления/Исправления_ошибок_"
else:
	url_prefix = "https://yandere-simulator.fandom.com/ru/wiki/Обновления/Обновления_"
addresses = [str(i) for i in range(2021, CURRENT_YEAR+1)]
ru = {str(i):{j:[] for j in MONTHS} for i in range(2021, CURRENT_YEAR+1)}
en = {str(i):{j:[] for j in MONTHS} for i in range(2021, CURRENT_YEAR+1)}

res = {i:{j:[] for j in MONTHS} for i in addresses}
for address in addresses:
	a = get(url_prefix+address)
	html = bs(a.content, "html.parser")
	g = list(html.find("span", id="Январь").find_parent("h2").next_siblings)
	g = filter(lambda x: x != "\n", g[:-6])
	g = list(filter(lambda x: x.name != "h3", g))
	i = 0
	while i < 12:
		j = 0
		try:
			while g[j].name != "h2":
				res[address][MONTHS[i]].extend(list(filter(lambda x: x != "\n", g[j].children)))
				j+=1
		except IndexError:
			break
		g = g[j:]
		i = MONTHS.index(g[0].findChildren("span", class_="mw-headline")[0].text)
		g = g[1:]

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot()

x = np.arange(sum([len(res[i]) for i in res]))
y1 = [len(res[i][j]) for i in addresses for j in MONTHS]

for i in range(len(y1)):
	print(f"202{i//12+1} {MONTHS_en[i%12]}: {y1[i]}")

ax.bar(x, y1, width=0.8, label=f"{('Improvements', 'Bugs')[UPDATES_OR_BUGFIXES == 'b']} that YandereDev has {('implemented', 'fixed')[UPDATES_OR_BUGFIXES == 'b']}")
ax.xaxis.set_major_locator(MultipleLocator(base=1))
plt.grid(True, axis="y")
ax.set_xticks([l for l in range(0, len(addresses)*12, 4)])
ax.set_xticklabels(['Jan 2021','May','Sept','Jan 2022','May','Sept','Jan 2023','May','Sept.'])
plt.legend()
plt.show()