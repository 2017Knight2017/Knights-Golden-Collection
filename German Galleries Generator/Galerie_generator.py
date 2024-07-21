import os

"""names = {
	"202X": [
#		"Аджии",
#		"Аканэ",
#		"Амай",
#		"Аой",
#		"Асу",
#		"Берумы",
#		"Беши",
#		"Борупена",
#		"Будо",
#		"Гаку",
#		"Гейджу",
#		"Гемы",
#		"Гиты",
#		"Дайроку",
#		"Даку",
#		"Дафуни",
#		"Джуку",
#		"Доры",
#		"Инкью",
#		"Ируки",
#		"Итачи",
#		"Каги",
#		"Кашико",
#		"Кенко",
#		"Кибы",
#		"Кизаны",
#		"Коконы",
#		"Кокоро",
#		"Кокумы",
#		"Куроко",
#		"Куу",
#		"Кьюджи",
#		"Май",
#		"Маки",
#		"Мантаро",
#		"Мегами",
#		"Меки",
#		"Мидори",
#		"Мины",
#		"Миюджи",
#		"Мусуме",
#		"Оки",
#		"Осаны",
#		"Осоро",
#		"Отохико",
#		"Пиппи",
#		"Райбару",
#		"Рику",
#		"Роджасу",
#		"Рюто",
#		"Саки",
#		"Сакуры",
#		"Сакью",
#		"Сейо",
#		"Сенпая",
#		"Сукуби",
#		"Сумире",
#		"Супаны",
#		"Тоги",
#		"Токуко",
#		"Умеджи",
#		"Унаги",
#		"Уэкии",
#		"Фуреддо",
#		"Хазу",
#		"Ханы",
#		"Ханако",
#		"Хаянари",
#		"Химари",
#		"Ходжиро",
#		"Хокуто",
#		"Хому",
#		"Хоро",
#		"Хоруды",
#		"Хошико",
#		"Цубаки",
#		"Цурузо",
#		"Чоджо",
#		"Шимы",
#		"Шина",
#		"Широми",
#		"Шо",
#		"Шозо",
#		"Шоку",
#		"Энпицу",
#		"Эфуде",
#		"Яку",
#		"Аяно",
#		"Генки",
#		"Карин",
#		"Кахо_Канокоги",
#		"Киоши",
#		"Кочо",
#		"Миды",
#		"Муджи",
#		"Насу",
#		"Нацуки",
#		"Рейны",
#		"Рино",
#		"Шиори"
    ],
	"1980": [
#		"Кагуи",
#		"Моэко",
#		"Хонами",
#		"Сумико",
#		"Рицуко",
#		"Ай",
#		"Тейко",
#		"Комако",
#		"Чигусы",
		"Азумы",
		"Азусы",
		"Айки",
		"Акари",
		"Акифуми",
		"Банри",
		"Бунзо",
		"Ваки",
		"Ватару",
		"Гакуто",
		"Готы",
		"Дайзо",
		"Дайсаку",
		"Дайчи",
		"Джицуко",
		"Джозе",
		"Дорэми",
		"Зенджи",
		"Ивао",
#		"Икуэ",
		"Ицуми",
		"Ичиэй",
#		"Кагемори",
		"Кахо",
		"Кена",
		"Кохару",
		"Мааи",
#		"Махиро",
		"Меи",
		"Мурасаки",
		"Нагако",
		"Нагахару",
		"Окимото",
		"Оми",
		"Джокичи",
		"Райзо",
		"Райму",
		"Ран",
		"Рейичи",
		"Риобы",
		"Рюсея",
		"Сабуро",
		"Сачи",
		"Сачихико",
		"Сейширо",
#		"Соноко",
		"Соры",
		"Соты",
		"Тадааки",
		"Тайчи",
		"Такако",
		"Тиру",
		"Того",
		"Уи",
		"Уманосукэ",
		"Умеко",
		"Фуджио",
		"Фуджиэ",
		"Фуюкичи",
		"Фуюми",
#		"Ханаэ",
		"Харуто",
		"Хачиро",
		"Хаято",
		"Химеко",
		"Хозуми",
		"Хоноки",
		"Чидори",
		"Чизуру",
		"Чикао",
		"Чуджиро",
#		"Шинако",
		"Шичиро",
		"Эйичи",
		"Эйко",
		"Эцуджи Odaka",
		"Etsuko ",
		"Yui Rio",
		"Yuna Hina",
		"Yahiko Onoda",
		"Yae Yaitabashi",
#		"Кёко",
#		"Джури",
#		"Маэ",
#		"Муцуко",
#		"Нориё",
#		"Отомэ",
#		"Рёко",
#		"Сузуко",
#		"Цуру"
	]
}"""

names = [
	"Aika Iseri",
	"Akari Komiyaku",
	"Akifumi Anno",
	"Azuma Takahoshi",
	"Azusa Mitsuishi",
	"Banri Masayuki",
	"Bunzo Ohta",
	"Chidori Ikegami",
	"Chikao Tsurumaki",
	"Chizuru Yamaguchi",
	"Chujiro Kitasume",
	"Daichi Suzuki",
	"Daisaku Aragaki",
	"Daizo Momose",
	"Doremi Shimahara",
	"Eiichi Asari",
	"Eiko Noguchi",
	"Etsuji Odaka",
	"Etsuko Hayashibara",
	"Fujie Haijima",
	"Fujio Kio",
	"Fuyukichi Kato",
	"Fuyumi Tachiki",
	"Gakuto Imakake",
	"Gota Kushida",
	"Hachiro Iso",
	"Haruto Yuto",
	"Hayato Haruki",
	"Himeko Dereguchi",
	"Honoka Kiyokawa",
	"Hozumi Takeda",
	"Ichiei Nakayama",
	"Itsumi Yuuki",
	"Iwao Satoh",
	"Jitsuko Furusawa",
	"Joze Shiuba",
	"Kaho Miki",
	"Ken Kyonashima",
	"Koharu Hinata",
	"Komako Funakoshi",
	"Maaya Ohshi",
	"Mei Mio",
	"Murasaki Nobumoto",
	"Nagaharu Kurudo",
	"Nagako Ando",
	"Okimoto Furukawa",
	"Omi Ohara",
	"Raimu Ichijo",
	"Raizo Morioka",
	"Ran Uchimara",
	"Reiichi Tanaami",
	"Ryusei Koki",
	"Saburo Meshino",
	"Sachi Yoneyama",
	"Sachihiko Fukuoka",
	"Seishiro Sadanaga",
	"Shichiro Kurosapu",
	"Sora Sosuke",
	"Sota Yuki",
	"Tadaaki Sunada",
	"Taichi Hiranaka",
	"Takako Ueda",
	"Teiko Nabatasai",
	"Tiru Sutoriku",
	"Togo Atatsuma",
	"Ui Tunesu",
	"Umanosuke Yoshinari",
	"Umeko Uchiyama",
	"Waka Yamaga",
	"Wataru Murata",
	"Yae Ogata",
	"Yahiko Onoda",
	"Yui Rio",
	"Yuna Hina",
	"Zenji Shinokura"
]

"""def getFullName(name: str, mode: str) -&gt; str:
	try:
		return " ".join(os.listdir(f"images/{mode}/{name}/Модель")[0].split("_")[:2])
	except (IndexError, FileNotFoundError):
		match name:
			case "Асу": return "Asu Rito"
			case "Оки": return "Oka Ruto"
			case "Кизаны": return "Kizana Sunobu"
			case "Мегами": return "Megami Saikou"
			case "Миды": return "Mida Rana"
			case "Муджи": return "Muja Kina"
			case "Осоро": return "Osoro Shidesu"
			case "Генки": return "Genka Kunahito"
			case "Кочо": return "Kocho Shuyona"
			case "Маэ": return "Mae Kunahito"
			case "Джури": return "Juri Nagasawa"
"""

def getContent(name: str) -> str:
	"""path = f"images/{mode}/{name}"
	student_images = os.listdir(path)

	portraitBlock = profileBlock = reputationBlock = interestBlock = modelBlock = []
	for i in student_images:
		a = os.path.join(path, i)
		match i:
			case "Модель": modelBlock = os.listdir(a)
			case "Портреты": portraitBlock = os.listdir(a)
			case "Профили": profileBlock = os.listdir(a)
			case "Репутация": reputationBlock = os.listdir(a)
			case "Интересы": interestBlock = os.listdir(a)
	"""
	short_name = name.split()[0] + "s"
	images = os.listdir("images")

	reputation = [i for i in images if i.split()[0] == short_name and i.split()[1] == "Reputation"]
	temp = list(map(lambda x: int("".join(filter(lambda y: y in "0123456789", x))), reputation))
	reputation = [i for i in reputation if str(max(temp)) in list(i)][0]

	try:
		interests = [i for i in images if i.split()[0] == short_name and i.split()[1] == "Interesten"]
		temp = list(map(lambda x: int("".join(filter(lambda y: y in "0123456789", x))), interests))
		interests = [i for i in interests if str(max(temp)) in list(i)][0]
	except IndexError:
		interests = False

	content = """{{Tabber
|tab1 = {{PAGENAME}}
|tab2 = Galerie
}}
{{"""

	content += """Infobox Charakter
|Bild = {0}
|Karriere = Student
|Gechlecht = ?
|Klasse = ... (1980)
|Klub = ...
|Typ = ?
|Schwarm = Niemand
|Reputation = ? insgesamt&lt;br&gt;Gefällt — ?&lt;br&gt;Erschreckt — ?&lt;br&gt;Respektierte — ?&lt;ref&gt;[[Datei:{1}|thumb|center]]&lt;/ref&gt; 
|Stärke = ...
""".format(f"{short_name} Porträt (aktuell).png", reputation)
	content += "}}"
	
	content += f"\n\'\'\'{name}\'\'\' ist ein der Studenten der [[Akademi High School]], im [[1980er Modus]].\n"

	content += """
== Aussehen ==
...

== Persönlichkeit ==
{{Quote
|text = ...
|person = Beschreibung in Ryobas Notizbuch.
}}
"""

	content += f"Nach Spielklassifizierung, {short_name[:-1]} — ? (Persönlichkeit). ? (Stärke).\n"

	content += """
== Tagesordnung ==
Um 7:05 AM kommt {0} in der Schule an und beginnt, die Schuhe zu wechseln.

Um 8:00 AM geht {0} zur Klasse.

Um 1:00 PM geht {0} zum Mittagessen.

Um 1:24 PM geht {0} zurück zur Klasse.

Um 3:30 PM nimmt {0} an der Reinigung teil.

== Interesten ==
""".format(short_name[:-1])

	content += '{| class="article-table" style="width: 50%;"'

	content += """|-
| colspan="2" | {0}
|-
! Gefällt !! Nicht
|-
|
* ...;
* ...;
* ...;
* ...;
* ...;
|
* ...;
* ...;
* ...;
* ...;
* ....
""".format((f"[[Datei:{interests}|thumb|center|300px]]", 
	    	"''Das Bild konnte nicht abgerufen werden. Informationen aus Spieldateien.''")[not interests])
	
	content += "|}\n"

	content += """
== Trivia ==
* ...
* ...
* ...

[[en:{0}]]
[[Kategorie:Generiert]]
[[Kategorie:Charakter (1980)]]
[[Kategorie:Studenten (1980)]]
""".format(name)

	return content

with open("Galerien.xml", "w", encoding="utf8") as file:
	file.write("<mediawiki xmlns=\"http://www.mediawiki.org/xml/export-0.11/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.mediawiki.org/xml/export-0.11/ http://www.mediawiki.org/xml/export-0.11.xsd\" version=\"0.11\" xml:lang=\"ru\">")
	for name in names:
		content = getContent(name)
		file.write(f"\n<page><title>{name}</title><revision><text>{content}</text></revision></page>")
	file.write("</mediawiki>")
