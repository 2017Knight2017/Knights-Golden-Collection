import json
import requests

def is_in_rectangle(pos:tuple[float, float],
					selector1:tuple[float, float],
		    		selector2:tuple[float, float]) -> bool:
	a = selector1[0] > selector2[0]
	b = selector1[1] > selector2[1]
	match a, b:
		case True, True:
			return selector1[0] > pos[0] > selector2[0] and selector1[1] > pos[1] > selector2[1]
		case False, True:
			return selector1[0] < pos[0] < selector2[0] and selector1[1] > pos[1] > selector2[1]
		case True, False:
			return selector1[0] > pos[0] > selector2[0] and selector1[1] < pos[1] < selector2[1]
		case False, False:
			return selector1[0] < pos[0] < selector2[0] and selector1[1] < pos[1] < selector2[1]

def which_location_student_is_in(pos:tuple[float, float]) -> str:
	labyrinth = is_in_rectangle(pos, (5532, 2548), (5718, 2204))
	confession_tree = is_in_rectangle(pos, (4396, 5832), (4802, 6194))
	east_fountain = is_in_rectangle(pos, (3234, 1972), (3596, 1718))
	west_fountain = is_in_rectangle(pos, (5602, 1714), (6014, 1978))
	east_japanese_garden = is_in_rectangle(pos, (5890, 3440), (5646, 3726))
	east_japanese_garden_inside = is_in_rectangle(pos, (5914, 3916), (6444, 3258))
	west_japanese_garden = is_in_rectangle(pos, (3574, 3720), (3372, 3330))
	west_japanese_garden_inside = is_in_rectangle(pos, (3310, 3300), (2760, 3892))
	inner_garden = is_in_rectangle(pos, (7748, 1810), (7930, 1632))
	inner_garden_east = is_in_rectangle(pos, (7656, 1554), (7238, 1862))
	inner_garden_west = is_in_rectangle(pos, (7976, 1564), (8322, 1844))
	south_roof = is_in_rectangle(pos, (16, 4050), (2698, 3122))
	between_gym_and_pool = is_in_rectangle(pos, (4508, 5215), (4723, 4256))
	between_showers = is_in_rectangle(pos, (4731, 4200), (4485, 3787))
	male_shower_south = is_in_rectangle(pos, (4432, 3767), (3781, 3976))
	female_shower_south = is_in_rectangle(pos, (4746, 3996), (5492, 3812))
	gardening_club = is_in_rectangle(pos, (2814, 2706), (3495, 2016))
	lockers = is_in_rectangle(pos, (7553, 954), (8110, 248))
	class_11 = is_in_rectangle(pos, (7071, 659), (7551, 429))
	class_12 = is_in_rectangle(pos, (8601, 650), (8123, 429))
	class_21 = is_in_rectangle(pos, (7558, 3494), (7070, 3720))
	class_22 = is_in_rectangle(pos, (8610, 3492), (8116, 3726))
	class_31 = is_in_rectangle(pos, (1092, 444), (602, 666))
	class_32 = is_in_rectangle(pos, (2146, 444), (1652, 670))
	south_east_stairway_1 = is_in_rectangle(pos, (9155, 941), (8827, 613))
	south_west_stairway_1 = is_in_rectangle(pos, (6528, 933), (6861, 610))
	north_east_stairway_1 = is_in_rectangle(pos, (6857, 2548), (6528, 2870))
	north_west_stairway_1 = is_in_rectangle(pos, (9145, 2872), (8807, 2542))
	south_east_stairway_2 = is_in_rectangle(pos, (9141, 3675), (8806, 3996))
	south_west_stairway_2 = is_in_rectangle(pos, (6865, 3672), (6526, 4004))
	north_west_stairway_2 = is_in_rectangle(pos, (6865, 5607), (6526, 5935))
	north_east_stairway_2 = is_in_rectangle(pos, (9140, 5924), (8810, 5603))
	north_east_stairway_3 = is_in_rectangle(pos, (2677, 2549), (2339, 2880))
	south_east_stairway_3 = is_in_rectangle(pos, (2672, 944), (2352, 622))
	south_west_stairway_3 = is_in_rectangle(pos, (397, 626), (61, 954))
	north_west_stairway_3 = is_in_rectangle(pos, (400, 2890), (64, 2559))
	english_class = is_in_rectangle(pos, (2668, 1460), (2344, 976))
	biology_lab = is_in_rectangle(pos, (2674, 1508), (2346, 2002))
	art_room = is_in_rectangle(pos, (2672, 2036), (2344, 2512))
	science_club = is_in_rectangle(pos, (1648, 2812), (2156, 3064))
	newspaper_club = is_in_rectangle(pos, (1128, 2729), (1620, 3040))
	photography_club = is_in_rectangle(pos, (591, 2811), (1100, 3060))
	audiovisual_room = is_in_rectangle(pos, (62, 2027), (401, 2528))
	computer_class = is_in_rectangle(pos, (59, 1996), (398, 1504))
	announcement_room = is_in_rectangle(pos, (62, 970), (398, 1470))
	headmaster_room = is_in_rectangle(pos, (1125, 271), (1623, 743))
	cooking_club = is_in_rectangle(pos, (7567, 2797), (7055, 3046))
	drama_club = is_in_rectangle(pos, (8087, 2720), (7588, 3044))
	occult_club = is_in_rectangle(pos, (8622, 2780), (8113, 3046))
	meeting_room = is_in_rectangle(pos, (8844, 2025), (9144, 2511))
	sewing_room = is_in_rectangle(pos, (8858, 1496), (9144, 1985))
	homecare_room = is_in_rectangle(pos, (8816, 964), (9144, 1453))
	infirmary = is_in_rectangle(pos, (6861, 964), (6530, 1465))
	teacher_room = is_in_rectangle(pos, (6861, 1499), (6530, 1979))
	guidance_councelor_room = is_in_rectangle(pos, (6830, 2019), (6530, 2514))
	science_lab = is_in_rectangle(pos, (8807, 4026), (9142, 4528))
	craft_room = is_in_rectangle(pos, (8810, 5054), (9138, 4556))
	sociology_room = is_in_rectangle(pos, (8804, 5572), (9141, 5085))
	martial_arts_club = is_in_rectangle(pos, (8126, 5829), (8618, 6086))
	light_music_club = is_in_rectangle(pos, (7588, 5769), (8089, 6095))
	art_club = is_in_rectangle(pos, (7566, 5857), (7056, 6117))
	library = is_in_rectangle(pos, (6858, 5077), (6530, 5583))
	student_council_room = is_in_rectangle(pos, (6858, 5045), (6530, 4556))
	calligraphy_room = is_in_rectangle(pos, (6861, 4522), (6530, 4019))
	gym = is_in_rectangle(pos, (5976, 4460), (4832, 5152))
	pool = is_in_rectangle(pos, (4332, 4468), (3248, 5148))
	running_track = is_in_rectangle(pos, (5916, 5564), (3300, 5292))
	gates = is_in_rectangle(pos, (5300, 2040), (3912, 1032))
	storage_west_1 = is_in_rectangle(pos, (6528, 3040), (6871, 2889))
	storage_east_1 = is_in_rectangle(pos, (8800, 2892), (9148, 3049))
	storage_east_2 = is_in_rectangle(pos, (8796, 6112), (9151, 5945))
	storage_west_2 = is_in_rectangle(pos, (6522, 6107), (6868, 5949))
	storage_west_3 = is_in_rectangle(pos, (56, 3057), (395, 2904))
	storage_east_3 = is_in_rectangle(pos, (2337, 2903), (2682, 3058))
	near_storage_west_1 = is_in_rectangle(pos, (6877, 3057), (7039, 2884))
	near_storage_east_1 = is_in_rectangle(pos, (8633, 2889), (8794, 3051))
	near_storage_west_2 = is_in_rectangle(pos, (6878, 6109), (7039, 5949))
	near_storage_east_2 = is_in_rectangle(pos, (8632, 6112), (8792, 5904))
	near_storage_west_3 = is_in_rectangle(pos, (416, 3068), (572, 2901))
	near_storage_east_3 = is_in_rectangle(pos, (2166, 3075), (2320, 2917))
	near_art_club = is_in_rectangle(pos, (6989, 5846), (7578, 5597))
	near_light_music_club = is_in_rectangle(pos, (7580, 5791), (8106, 5498))
	near_martial_arts_club = is_in_rectangle(pos, (8711, 5849), (8120, 5587))
	near_sociology_room = is_in_rectangle(pos, (8618, 5625), (8803, 5071))
	near_craft_room = is_in_rectangle(pos, (8613, 4548), (8793, 5069))
	near_science_lab = is_in_rectangle(pos, (8613, 4548), (8793, 4006))
	near_headmaster_room = is_in_rectangle(pos, (1105, 972), (1640, 786))
	near_library = is_in_rectangle(pos, (7062, 5583), (6895, 5062))
	near_student_council = is_in_rectangle(pos, (7059, 4539), (6895, 5062))
	near_calligraphy_room = is_in_rectangle(pos, (7059, 4539), (6878, 4013))
	near_guidance_councelor = is_in_rectangle(pos, (6886, 2008), (7054, 2530))
	near_teacher_room = is_in_rectangle(pos, (6886, 2008), (7060, 1488))
	near_infirmary = is_in_rectangle(pos, (6884, 952), (7060, 1488))
	near_homecare_room = is_in_rectangle(pos, (8800, 956), (8618, 1490))
	near_sewing_room = is_in_rectangle(pos, (8782, 2016), (8618, 1490))
	near_meeting_room = is_in_rectangle(pos, (8782, 2016), (8614, 2524))
	near_occult_club = is_in_rectangle(pos, (8708, 2536), (8108, 2780))
	near_drama_club = is_in_rectangle(pos, (7572, 2520), (8096, 2708))
	near_cooking_club = is_in_rectangle(pos, (7580, 2512), (6972, 2772))
	near_english_room = is_in_rectangle(pos, (2140, 1492), (2332, 964))
	near_biology_lab = is_in_rectangle(pos, (2140, 1492), (2328, 2020))
	near_art_room = is_in_rectangle(pos, (2146, 2528), (2328, 2020))
	near_science_club = is_in_rectangle(pos, (1638, 2538), (2248, 2790))
	near_newspaper_club = is_in_rectangle(pos, (1638, 2538), (1114, 2714))
	near_photography_club = is_in_rectangle(pos, (502, 2794), (1112, 2526))
	near_audiovisual_room = is_in_rectangle(pos, (404, 2020), (598, 2536))
	near_computer_class = is_in_rectangle(pos, (404, 2020), (594, 1500))
	near_announcement_room = is_in_rectangle(pos, (412, 964), (594, 1500))
	between_men_shower_and_pool = is_in_rectangle(pos, (3232, 4446), (4350, 4284))
	barrel = is_in_rectangle(pos, (3236, 4264), (3712, 4064))
	between_women_shower_and_gym = is_in_rectangle(pos, (5678, 4448), (4754, 4260))
	near_class_11 = is_in_rectangle(pos, (7529, 958), (7008, 664))
	near_class_12 = is_in_rectangle(pos, (8143, 970), (8691, 667))
	near_class_21 = is_in_rectangle(pos, (6887, 4013), (7656, 3730))
	near_class_22 = is_in_rectangle(pos, (8722, 4005), (8012, 3722))
	near_class_31 = is_in_rectangle(pos, (1105, 975), (500, 678))
	near_class_32 = is_in_rectangle(pos, (1646, 967), (2245, 681))
	near_toilets_west_1 = is_in_rectangle(pos, (8623, 596), (8802, 25))
	near_toilets_east_1 = is_in_rectangle(pos, (6878, 599), (7059, 0))
	near_toilets_west_2 = is_in_rectangle(pos, (6875, 3657), (7051, 3139))
	near_toilets_east_2 = is_in_rectangle(pos, (8793, 3648), (8623, 3142))
	near_toilets_west_3 = is_in_rectangle(pos, (588, 537), (412, 84))
	near_toilets_east_3 = is_in_rectangle(pos, (2158, 551), (2330, 82))
	men_toilet_west_1 = is_in_rectangle(pos, (6512, 342), (6875, 69))
	men_toilet_east_1 = is_in_rectangle(pos, (9161, 73), (8800, 345))
	men_toilet_west_2 = is_in_rectangle(pos, (6872, 3403), (6513, 3138))
	men_toilet_east_2 = is_in_rectangle(pos, (9161, 3132), (8797, 3401))
	men_toilet_west_3 = is_in_rectangle(pos, (50, 347), (404, 87))
	men_toilet_east_3 = is_in_rectangle(pos, (2332, 89), (2692, 353))
	women_toilet_west_1 = is_in_rectangle(pos, (6512, 342), (6874, 601))
	women_toilet_east_1 = is_in_rectangle(pos, (9159, 595), (8800, 345))
	women_toilet_west_2 = is_in_rectangle(pos, (6872, 3403), (6515, 3662))
	women_toilet_east_2 = is_in_rectangle(pos, (9164, 3655), (8797, 3401))
	women_toilet_west_3 = is_in_rectangle(pos, (50, 347), (407, 613))
	women_toilet_east_3 = is_in_rectangle(pos, (2336, 596), (2692, 353))
	women_shower = is_in_rectangle(pos, (5475, 4259), (4757, 4047))
	men_shower = is_in_rectangle(pos, (3753, 4248), (4457, 4047))
	cafeteria = is_in_rectangle(pos, (8004, 3334), (7668, 3942))
	near_gardening_club = is_in_rectangle(pos, (3806, 1994), (3602, 2762))


	if labyrinth: return "near the Hedge Maze"
	elif confession_tree: return "under the Confession Tree"
	elif east_fountain: return "near the east Fountain"
	elif west_fountain: return "near the west Fountain"
	elif west_japanese_garden: return "near the west Japanese Garden"
	elif west_japanese_garden_inside: return "at the west Japanese Garden"
	elif east_japanese_garden: return "near the east Japanese Garden"
	elif east_japanese_garden_inside: return "at the east Japanese Garden"
	elif inner_garden: return "at the Plaza"
	elif inner_garden_east: return "on the east of the Plaza"
	elif inner_garden_west: return "on the west of the Plaza"
	elif south_roof: return "on the south of the Roof"
	elif between_gym_and_pool: return "between the Gymnasium and the Swimming Pool"
	elif between_showers: return "between the Shower Rooms"
	elif male_shower_south: return "south of the boys' Shower Room"
	elif female_shower_south: return "south of the girls' Shower Room"
	elif gardening_club: return "in the Gardening Club"
	elif lockers: return "near the lockers"
	elif class_11: return "at the Classroom 1-1"
	elif class_12: return "at the Classroom 1-2"
	elif class_21: return "at the Classroom 2-1"
	elif class_22: return "at the Classroom 2-2"
	elif class_31: return "at the Classroom 3-1"
	elif class_32: return "at the Classroom 3-2"
	elif south_east_stairway_1: return "at the south-east stairway of the 1st floor"
	elif south_west_stairway_1: return "at the south-west stairway of the 1st floor"
	elif north_east_stairway_1: return "at the north-east stairway of the 1st floor"
	elif north_west_stairway_1: return "at the north-west stairway of the 1st floor"
	elif south_east_stairway_2: return "at the south-east stairway of the 2nd floor"
	elif south_west_stairway_2: return "at the south-west stairway of the 2nd floor"
	elif north_west_stairway_2: return "at the north-west stairway of the 2nd floor"
	elif north_east_stairway_2: return "at the north-east stairway of the 2nd floor"
	elif north_east_stairway_3: return "at the north-east stairway of the 3rd floor"
	elif south_east_stairway_3: return "at the south-east stairway of the 3rd floor"
	elif south_west_stairway_3: return "at the south-west stairway of the 3rd floor"
	elif north_west_stairway_3: return "at the north-west stairway of the 3rd floor"
	elif english_class: return "at the English Classroom"
	elif biology_lab: return "at the Biology Lab"
	elif art_room: return "at the Art Room"
	elif science_club: return "at the Science Club"
	elif newspaper_club: return "at the Newspaper Club"
	elif photography_club: return "at the Photography Club"
	elif audiovisual_room: return "at the Audiovisual Room"
	elif computer_class: return "at the Computer Lab"
	elif announcement_room: return "at the Announcement Room"
	elif headmaster_room: return "at the Headmaster's Office"
	elif cooking_club: return "at the Cooking Club"
	elif drama_club: return "at the Drama Club"
	elif occult_club: return "at the Occult Club"
	elif meeting_room: return "at the Meeting Room"
	elif sewing_room: return "at the Sewing Room"
	elif homecare_room: return "at the Home Ec Room"
	elif infirmary: return "at the Infirmary"
	elif teacher_room: return "at the Faculty Room"
	elif guidance_councelor_room: return "at the Guidance Counselor's Office"
	elif science_lab: return "at the Science Lab"
	elif craft_room: return "at the Workshop"
	elif sociology_room: return "at the Sociology Room"
	elif martial_arts_club: return "at the Martial Arts Club"
	elif light_music_club: return "at the Light Music Club"
	elif art_club: return "at the Art Club"
	elif library: return "at the Library"
	elif student_council_room: return "at the Student Council Room"
	elif calligraphy_room: return "at the Calligraphy Room"
	elif gym: return "at the Gymnasium"
	elif pool: return "at the Swimming Pool"
	elif running_track: return "at the Running Track"
	elif gates: return "near the Gates"
	elif storage_west_1: return "at the west Storage Room of the 1st floor"
	elif storage_east_1: return "at the east Storage Room of the 1st floor"
	elif storage_east_2: return "at the east Storage Room of the 2nd floor"
	elif storage_west_2: return "at the west Storage Room of the 2nd floor"
	elif storage_west_3: return "at the west Storage Room of the 3rd floor"
	elif storage_east_3: return "at the east Storage Room of the 3rd floor"
	elif near_storage_west_1: return "near the west Storage Room of the 1st floor"
	elif near_storage_east_1: return "near the east Storage Room of the 1st floor"
	elif near_storage_west_2: return "near the west Storage Room of the 2nd floor"
	elif near_storage_east_2: return "near the east Storage Room of the 2nd floor"
	elif near_storage_west_3: return "near the west Storage Room of the 3rd floor"
	elif near_storage_east_3: return "near the east Storage Room of the 3rd floor"
	elif near_art_club: return "near the Art Club"
	elif near_light_music_club: return "near the Light Music Club"
	elif near_martial_arts_club: return "near the Martial Arts Club"
	elif near_sociology_room: return "near the Sociology Room"
	elif near_craft_room: return "near the Workshop"
	elif near_science_lab: return "near the Science Lab"
	elif near_headmaster_room: return "near the Headmaster's Office"
	elif near_library: return "near the Library"
	elif near_student_council: return "near the Student Council Room"
	elif near_calligraphy_room: return "near the Calligraphy Room"
	elif near_guidance_councelor: return "near the Guidance Counselor's Office"
	elif near_teacher_room: return "near the Faculty Room"
	elif near_infirmary: return "near the Infirmary"
	elif near_homecare_room: return "near the Home Ec Room"
	elif near_sewing_room: return "near the Sewing Room"
	elif near_meeting_room: return "near the Meeting Room"
	elif near_occult_club: return "near the Occult Club"
	elif near_drama_club: return "near the Drama Club"
	elif near_cooking_club: return "near the Cooking Club"
	elif near_english_room: return "near the English Classroom"
	elif near_biology_lab: return "near the Biology Lab"
	elif near_art_room: return "near the Art Room"
	elif near_science_club: return "near the Science Club"
	elif near_newspaper_club: return "near the Newspaper Club"
	elif near_photography_club: return "near the Photography Club"
	elif near_audiovisual_room: return "near the Audiovisual Room"
	elif near_computer_class: return "near the Computer Lab"
	elif near_announcement_room: return "near the Announcement Room"
	elif between_men_shower_and_pool: return "between the boys' Shower Room and the Swimming Pool"
	elif barrel: return "near the Burning Barrel"
	elif between_women_shower_and_gym: return "Between the girls' Shower Room and the Gymnasium"
	elif near_gardening_club: return "near the Gardening Club"
	elif near_class_11: return "near the Classroom 1-1"
	elif near_class_12: return "near the Classroom 1-2"
	elif near_class_21: return "near the Classroom 2-1"
	elif near_class_22: return "near the Classroom 2-2"
	elif near_class_31: return "near the Classroom 3-1"
	elif near_class_32: return "near the Classroom 3-2"
	elif near_toilets_west_1: return "near the west Bathrooms of the 1st floor"
	elif near_toilets_east_1: return "near the east Bathrooms of the 1st floor"
	elif near_toilets_west_2: return "near the west Bathrooms of the 2nd floor"
	elif near_toilets_east_2: return "near the east Bathrooms of the 2nd floor"
	elif near_toilets_west_3: return "near the west Bathrooms of the 3rd floor"
	elif near_toilets_east_3: return "near the east Bathrooms of the 3rd floor"
	elif men_toilet_west_1: return "at the west boys' Bathroom of the 1st floor"
	elif men_toilet_east_1: return "at the east boys' Bathroom of the 1st floor"
	elif men_toilet_west_2: return "at the west boys' Bathroom of the 2nd floor"
	elif men_toilet_east_2: return "at the east boys' Bathroom of the 2nd floor"
	elif men_toilet_west_3: return "at the west boys' Bathroom of the 3rd floor"
	elif men_toilet_east_3: return "at the east boys' Bathroom of the 3rd floor"
	elif women_toilet_west_1: return "at the west girls' Bathroom of the 1st floor"
	elif women_toilet_east_1: return "at the east girls' Bathroom of the 1st floor"
	elif women_toilet_west_2: return "at the west girls' Bathroom of the 2nd floor"
	elif women_toilet_east_2: return "at the east girls' Bathroom of the 2nd floor"
	elif women_toilet_west_3: return "at the west girls' Bathroom of the 3rd floor"
	elif women_toilet_east_3: return "at the east girls' Bathroom of the 3rd floor"
	elif women_shower: return "at the girls' Shower Room"
	elif men_shower: return "at the boys' Shower Room"
	elif cafeteria: return "at the outdoor Cafeteria"
	else: return f"({pos[0]}, {pos[1]})"


NAMES = [
	"Kaguya Wakaizumi",
	"Moeko Rakuyona",
	"Honami Hodoshima",
	"Sumiko Tachibana",
	"Ritsuko Chikanari",
	"Ai Doruyashi",
	"Teiko Nabatasai",
	"Komako Funakoshi",
	"Chigusa Busujima",
	"Sonoko Sakanoue",
	"Azuma Takahoshi",
	"Azusa Mitsuishi",
	"Aika Iseri",
	"Akari Komiyaku",
	"Akifumi Anno",
	"Banri Masayuki",
	"Bunzo Ohta",
	"Waka Yamaga",
	"Wataru Murata",
	"Gakuto Imakake",
	"Gota Kushida",
	"Daizo Momose",
	"Daisaku Aragaki",
	"Daichi Suzuki",
	"Jitsuko Furusawa",
	"Joze Shiuba",
	"Doremi Shimahara",
	"Zenji Shiokura",
	"Iwao Sato",
	"Ikue Yaitabashi",
	"Itsumi Yuuki",
	"Ichiei Nakayama",
	"Kagemori Takagi",
	"Kaho Miki",
	"Ken Kyonashima",
	"Koharu Hinata",
	"Maaya Ohshi",
	"Mahiro Honda",
	"Mei Mio",
	"Murasaki Nobumoto",
	"Nagako Ando",
	"Nagaharu Kurudo",
	"Okimoto Furukawa",
	"Omi Ohara",
	"Jokichi Yudasei",
	"Raizo Morioka",
	"Raimu Ichijo",
	"Ran Uchimara",
	"Reiichi Tanaami",
	"Ryusei Koki",
	"Saburo Meshino",
	"Sachi Yoneyama",
	"Sachihiko Fukuoka",
	"Seishiro Sadanaga",
	"Sora Sosuke",
	"Sota Yuki",
	"Tadaaki Sunada",
	"Taichi Hiranaka",
	"Takako Ueda",
	"Tiru Sutoriku",
	"Togo Atatsuma",
	"Ui Tunesu",
	"Umanosuke Yoshinari",
	"Umeko Uchiyama",
	"Fujio Kio",
	"Fujie Haijima",
	"Fuyukichi Kato",
	"Fuyumi Tachiki",
	"Hanae Ono",
	"Haruto Yuto",
	"Hachiro Iso",
	"Hayato Haruki",
	"Himeko Dereguchi",
	"Hozumi Takeda",
	"Honoka Kiyokawa",
	"Chidori Ikegami",
	"Chizuru Yamaguchi",
	"Chikao Tsurumaki",
	"Chujiro Kitasume",
	"Shinako Bunzai",
	"Shichiro Kurosapu",
	"Eiichi Asari",
	"Eiko Noguchi",
	"Etsuji Odaka",
	"Etsuko Hayashibara",
	"Yui Rio",
	"Yuna Hina",
	"Yahiko Onoda",
	"Yae Ogata",
	"Kyoko Koyasu",
	"Juri Nagasawa",
	"Mutsuko Nishimura",
	"Noriyo Hiramatsu",
	"Otome Nagasako",
	"Ryoko Ugaki",
	"Suzuko Naka",
	"Tsuru Kariya"]

GROUPS = [
	"Teachers",
	"Students",
	"Members of the Cooking Club",
	"Members of the Drama Club",
	"Members of the Occult Club",
	"Members of the Art Club",
	"Members of the Light Music Club",
	"Members of the Martial Arts Club",
	"Members of the Photography Club",
	"Members of the Newspaper Club",
	"Members of the Science Club",
	"Members of the Sport Club",
	"Members of the Gardening Club",
	"Members of the Drama Club, except the leader",
	"Members of the Occult Club, except the leader",
	"Members of the Light Music Club, except the leader",
	"Members of the Photography Club, except the leader",
	"Members of the Newspaper Club, except the leader",
	"Members of the Sport Club, except the leader",
	"Members of the Gardening Club, except the leader",
	"Deliquents-boys",
	"Deliquents-girls",
	"Student Council",
	"Rainbow Boys",
	"Rainbow Girls"
] 

translated = {
	"Kaguya Wakaizumi": "Кагуя Вакайзуми",
	"Moeko Rakuyona": "Моэко Ракуёна",
	"Honami Hodoshima": "Хонами Ходошима",
	"Sumiko Tachibana": "Сумико Тачибана",
	"Ritsuko Chikanari": "Рицуко Чиканари",
	"Ai Doruyashi": "Ай Доруяши",
	"Teiko Nabatasai": "Тейко Набатасай",
	"Komako Funakoshi": "Комако Фунакоши",
	"Chigusa Busujima": "Чигуса Бусуджима",
	"Sonoko Sakanoue": "Соноко Саканоуэ",
	"Azuma Takahoshi": "Азума Такахоши",
	"Azusa Mitsuishi": "Азуса Мицуиши",
	"Aika Iseri": "Айка Исери",
	"Akari Komiyaku": "Акари Комияку",
	"Akifumi Anno": "Акифуми Анно",
	"Banri Masayuki": "Банри Масаюки",
	"Bunzo Ohta": "Бунзо Ота",
	"Waka Yamaga": "Вака Ямага",
	"Wataru Murata": "Ватару Мурата",
	"Gakuto Imakake": "Гакуто Имакаке",
	"Gota Kushida": "Гота Кушида",
	"Daizo Momose": "Дайзо Момосэ",
	"Daisaku Aragaki": "Дайсаку Арагаки",
	"Daichi Suzuki": "Дайчи Сузуки",
	"Jitsuko Furusawa": "Джицуко Фурусава",
	"Joze Shiuba": "Джозе Шиуба",
	"Doremi Shimahara": "Дорэми Шимахара",
	"Zenji Shiokura": "Зенджи Шинокура",
	"Iwao Sato": "Ивао Сато",
	"Ikue Yaitabashi": "Икуэ Яйтабаши",
	"Itsumi Yuuki": "Ицуми Юуки",
	"Ichiei Nakayama": "Ичиэй Накаяма",
	"Kagemori Takagi": "Кагемори Такаги",
	"Kaho Miki": "Кахо Мики",
	"Ken Kyonashima": "Кен Кёнашима",
	"Koharu Hinata": "Кохару Хината",
	"Maaya Ohshi": "Маая Оши",
	"Mahiro Honda": "Махиро Хонда",
	"Mei Mio": "Меи Мио",
	"Murasaki Nobumoto": "Мурасаки Нобумото",
	"Nagako Ando": "Нагако Андо",
	"Nagaharu Kurudo": "Нагахару Курудо",
	"Okimoto Furukawa": "Окимото Фурукава",
	"Omi Ohara": "Оми Охара",
	"Jokichi Yudasei": "Джокичи Юдасей",
	"Raizo Morioka": "Райзо Мориока",
	"Raimu Ichijo": "Райму Ичиджо",
	"Ran Uchimara": "Ран Учимара",
	"Reiichi Tanaami": "Рейичи Танаами",
	"Ryusei Koki": "Рюсей Коки",
	"Saburo Meshino": "Сабуро Мешино",
	"Sachi Yoneyama": "Сачи Ёнеяма",
	"Sachihiko Fukuoka": "Сачихико Фукуока",
	"Seishiro Sadanaga": "Сейширо Саданага",
	"Sora Sosuke": "Сора Сосуке",
	"Sota Yuki": "Сота Юки",
	"Tadaaki Sunada": "Тадааки Сунада",
	"Taichi Hiranaka": "Тайчи Хиранака",
	"Takako Ueda": "Такако Уэда",
	"Tiru Sutoriku": "Тиру Суторику",
	"Togo Atatsuma": "Того Атацума",
	"Ui Tunesu": "Уи Тунесу",
	"Umanosuke Yoshinari": "Уманосукэ Ёшинари",
	"Umeko Uchiyama": "Умеко Учияма",
	"Fujio Kio": "Фуджио Кио",
	"Fujie Haijima": "Фуджиэ Хайджима",
	"Fuyukichi Kato": "Фуюкичи Като",
	"Fuyumi Tachiki": "Фуюми Тачики",
	"Hanae Ono": "Ханаэ Оно",
	"Haruto Yuto": "Харуто Юто",
	"Hachiro Iso": "Хачиро Исо",
	"Hayato Haruki": "Хаято Харуки",
	"Himeko Dereguchi": "Химеко Дерегучи",
	"Hozumi Takeda": "Хозуми Такеда",
	"Honoka Kiyokawa": "Хонока Киёкава",
	"Chidori Ikegami": "Чидори Икегами",
	"Chizuru Yamaguchi": "Чизуру Ямагучи",
	"Chikao Tsurumaki": "Чикао Цурумаки",
	"Chujiro Kitasume": "Чуджиро Китасуме",
	"Shinako Bunzai": "Шинако Бунзай",
	"Shichiro Kurosapu": "Шичиро Куросапу",
	"Eiichi Asari": "Эйичи Асари",
	"Eiko Noguchi": "Эйко Ногучи",
	"Etsuji Odaka": "Эцуджи Одака",
	"Etsuko Hayashibara": "Эцуко Хаяшибара",
	"Yui Rio": "Юи Рио",
	"Yuna Hina": "Юна Хина",
	"Yahiko Onoda": "Яхико Онода",
	"Yae Ogata": "Яэ Огата",
	"Kyoko Koyasu": "Кёко Коясу",
	"Juri Nagasawa": "Джури Нагасава",
	"Mutsuko Nishimura": "Муцуко Нишимура",
	"Noriyo Hiramatsu": "Нориё Хирамацу",
	"Otome Nagasako": "Отомэ Нагасако",
	"Ryoko Ugaki": "Рёко Угаки",
	"Suzuko Naka": "Сузуко Нака",
	"Tsuru Kariya": "Цуру Кария",
	"Teachers": "Учителя",
	"Students": "Ученики",
	"Members of the Cooking Club": "Члены клуба кулинарии",
	"Members of the Drama Club": "Члены клуба драмы",
	"Members of the Occult Club": "Члены оккультного клуба",
	"Members of the Art Club": "Члены арт клуба",
	"Members of the Light Music Club": "Члены клуба лёгкой музыки",
	"Members of the Martial Arts Club": "Члены клуба боевых искусств",
	"Members of the Photography Club": "Члены клуба фотографии",
	"Members of the Newspaper Club": "Члены газетного клуба",
	"Members of the Science Club": "Члены клуба науки",
	"Members of the Sport Club": "Члены клуба спорта",
	"Members of the Gardening Club": "Члены клуба садоводства",
	"Members of the Cooking Club, except the leader": "Члены клуба кулинарии, кроме лидера",
	"Members of the Drama Club, except the leader": "Члены клуба драмы, кроме лидера",
	"Members of the Occult Club, except the leader": "Члены оккультного клуба, кроме лидера",
	"Members of the Art Club, except the leader": "Члены арт клуба, кроме лидера",
	"Members of the Light Music Club, except the leader": "Члены клуба лёгкой музыки, кроме лидера",
	"Members of the Martial Arts Club, except the leader": "Члены клуба боевых искусств, кроме лидера",
	"Members of the Photography Club, except the leader": "Члены клуба фотографии, кроме лидера",
	"Members of the Newspaper Club, except the leader": "Члены газетного клуба, кроме лидера",
	"Members of the Science Club, except the leader": "Члены клуба науки, кроме лидера",
	"Members of the Sport Club, except the leader": "Члены клуба спорта, кроме лидера",
	"Members of the Gardening Club, except the leader": "Члены клуба садоводства, кроме лидера",
	"Deliquents-boys": "Правонарушители",
	"Deliquents-girls": "Правонарушительницы",
	"Student Council": "Студенческий совет",
	"Rainbow Boys": "Радужные парни",
	"Rainbow Girls": "Радужные девушки"
}

translated_RU_EN = {
	"Учителя": "Teachers",
	"Ученики": "Students",
	"Члены клуба кулинарии": "Members of the Cooking Club",
	"Члены клуба драмы": "Members of the Drama Club",
	"Члены оккультного клуба": "Members of the Occult Club",
	"Члены арт клуба": "Members of the Art Club",
	"Члены клуба лёгкой музыки": "Members of the Light Music Club",
	"Члены клуба боевых искусств": "Members of the Martial Arts Club",
	"Члены клуба фотографии": "Members of the Photography Club",
	"Члены газетного клуба": "Members of the Newspaper Club",
	"Члены клуба науки": "Members of the Science Club",
	"Члены клуба спорта": "Members of the Sport Club",
	"Члены клуба садоводства": "Members of the Gardening Club",
	"Члены клуба кулинарии, кроме лидера": "Members of the Cooking Club, except the leader",
	"Члены клуба драмы, кроме лидера": "Members of the Drama Club, except the leader",
	"Члены оккультного клуба, кроме лидера": "Members of the Occult Club, except the leader",
	"Члены арт клуба, кроме лидера": "Members of the Art Club, except the leader",
	"Члены клуба лёгкой музыки, кроме лидера": "Members of the Light Music Club, except the leader",
	"Члены клуба боевых искусств, кроме лидера": "Members of the Martial Arts Club, except the leader",
	"Члены клуба фотографии, кроме лидера": "Members of the Photography Club, except the leader",
	"Члены газетного клуба, кроме лидера": "Members of the Newspaper Club, except the leader",
	"Члены клуба науки, кроме лидера": "Members of the Science Club, except the leader",
	"Члены клуба спорта, кроме лидера": "Members of the Sport Club, except the leader",
	"Члены клуба садоводства, кроме лидера": "Members of the Gardening Club, except the leader",
	"Правонарушители": "Deliquents-boys",
	"Правонарушительницы": "Deliquents-girls",
	"Студенческий совет": "Student Council",
	"Радужные парни": "Rainbow Boys",
	"Радужные девушки": "Rainbow Girls"
}

CATEGORIES = {
    "Учителя":[
        "Кёко Коясу",
		"Джури Нагасава",
		"Муцуко Нишимура",
		"Нориё Хирамацу",
		"Отомэ Нагасако",
		"Рёко Угаки",
		"Сузуко Нака",
		"Цуру Кария"
    ],
    "Ученики":[
        "Кагуя Вакайзуми",
		"Моэко Ракуёна",
		"Хонами Ходошима",
		"Сумико Тачибана",
		"Рицуко Чиканари",
		"Ай Доруяши",
		"Тейко Набатасай",
		"Комако Фунакоши",
		"Чигуса Бусуджима",
		"Азума Такахоши",
		"Азуса Мицуиши",
		"Айка Исери",
		"Акари Комияку",
		"Акифуми Анно",
		"Банри Масаюки",
		"Бунзо Ота",
		"Вака Ямага",
		"Ватару Мурата",
		"Гакуто Имакаке",
		"Гота Кушида",
		"Дайзо Момосэ",
		"Дайчи Сузуки",
		"Джицуко Фурусава",
		"Дорэми Шимахара",
		"Зенджи Шинокура",
		"Ивао Сато",
		"Икуэ Яйтабаши",
		"Ицуми Юуки",
		"Ичиэй Накаяма",
		"Кагемори Такаги",
		"Кахо Мики",
		"Кохару Хината",
		"Маая Оши",
		"Махиро Хонда",
		"Меи Мио",
		"Мурасаки Нобумото",
		"Нагако Андо",
		"Нагахару Курудо",
		"Окимото Фурукава",
		"Оми Охара",
		"Джокичи Юдасей",
		"Райзо Мориока",
		"Райму Ичиджо",
		"Ран Учимара",
		"Риоба Аиши",
		"Рюсей Коки",
		"Сабуро Мешино",
		"Сачи Ёнеяма",
		"Сачихико Фукуока",
		"Сейширо Саданага",
		"Соноко Саканоуэ",
		"Сора Сосуке",
		"Сота Юки",
		"Тадааки Сунада",
		"Тайчи Хиранака",
		"Такако Уэда",
		"Тиру Суторику",
		"Того Атацума",
		"Уи Тунесу",
		"Уманосукэ Ёшинари",
		"Умеко Учияма",
		"Фуджио Кио",
		"Фуджиэ Хайджима",
		"Фуюкичи Като",
		"Фуюми Тачики",
		"Ханаэ Оно",
		"Харуто Юто",
		"Хачиро Исо",
		"Хаято Харуки",
		"Химеко Дерегучи",
		"Хозуми Такеда",
		"Хонока Киёкава",
		"Чидори Икегами",
		"Чизуру Ямагучи",
		"Чикао Цурумаки",
		"Чуджиро Китасуме",
		"Шинако Бунзай",
		"Шичиро Куросапу",
		"Эйичи Асари",
		"Эйко Ногучи",
		"Эцуджи Одака",
		"Эцуко Хаяшибара",
		"Юи Рио",
		"Юна Хина",
		"Яхико Онода",
		"Яэ Огата"
	],
    "Члены клуба кулинарии":[
        "Акифуми Анно",
        "Банри Масаюки",
        "Чикао Цурумаки",
        "Айка Исери",
        "Уи Тунесу"
	],
    "Члены клуба драмы":[
        "Дайчи Сузуки",
        "Фуджио Кио",
        "Эйичи Асари",
        "Чидори Икегами",
        "Химеко Дерегучи"
	],
    "Члены оккультного клуба":[
        "Гакуто Имакаке",
		"Хачиро Исо",
        "Ичиэй Накаяма",
        "Эйко Ногучи",
        "Фуджиэ Хайджима"
	],
    "Члены арт клуба":[
        "Нагахару Курудо",
        "Окимото Фурукава",
    	"Райзо Мориока",
        "Джицуко Фурусава",
        "Кахо Мики"
	],
    "Члены клуба лёгкой музыки":[
        "Оми Охара",
        "Ран Учимара",
        "Сачи Ёнеяма",
        "Такако Уэда",
        "Умеко Учияма"
	],
    "Члены клуба боевых искусств":[
        "Сачихико Фукуока",
        "Тадааки Сунада",
        "Уманосукэ Ёшинари",
        "Маая Оши",
        "Нагако Андо"
	],
    "Члены клуба фотографии":[
        "Ватару Мурата",
        "Яхико Онода",
        "Зенджи Шинокура",
        "Вака Ямага",
        "Яэ Огата"
	],
    "Члены газетного клуба":[
        "Шинако Бунзай",
        "Кагемори Такаги",
        "Махиро Хонда",
        "Ханаэ Оно",
        "Икуэ Яйтабаши"
	],
    "Члены клуба науки":[
        "Азума Такахоши",
        "Бунзо Ота",
        "Чуджиро Китасуме",
        "Азуса Мицуиши",
        "Чизуру Ямагучи"
	],
    "Члены клуба спорта":[
        "Дайзо Момосэ",
        "Эцуджи Одака",
        "Фуюкичи Като",
        "Эцуко Хаяшибара",
        "Фуюми Тачики"
	],
    "Члены клуба садоводства":[
        "Гота Кушида",
        "Хозуми Такеда",
        "Ивао Сато",
        "Хонока Киёкава",
        "Ицуми Юуки",
	],
    "Члены клуба кулинарии, кроме лидера":[
        "Банри Масаюки",
        "Чикао Цурумаки",
        "Айка Исери",
        "Уи Тунесу"
	],
    "Члены клуба драмы, кроме лидера":[
        "Фуджио Кио",
        "Эйичи Асари",
        "Чидори Икегами",
        "Химеко Дерегучи"
	],
    "Члены оккультного клуба, кроме лидера":[
		"Хачиро Исо",
        "Ичиэй Накаяма",
        "Эйко Ногучи",
        "Фуджиэ Хайджима"
	],
    "Члены арт клуба, кроме лидера":[
        "Окимото Фурукава",
    	"Райзо Мориока",
        "Джицуко Фурусава",
        "Кахо Мики"
	],
    "Члены клуба лёгкой музыки, кроме лидера":[
        "Ран Учимара",
        "Сачи Ёнеяма",
        "Такако Уэда",
        "Умеко Учияма"
	],
    "Члены клуба боевых искусств, кроме лидера":[
        "Тадааки Сунада",
        "Уманосукэ Ёшинари",
        "Маая Оши",
        "Нагако Андо"
	],
    "Члены клуба фотографии, кроме лидера":[
        "Яхико Онода",
        "Зенджи Шинокура",
        "Вака Ямага",
        "Яэ Огата"
	],
    "Члены газетного клуба, кроме лидера":[
        "Кагемори Такаги",
        "Махиро Хонда",
        "Ханаэ Оно",
        "Икуэ Яйтабаши"
	],
    "Члены клуба науки, кроме лидера":[
        "Бунзо Ота",
        "Чуджиро Китасуме",
        "Азуса Мицуиши",
        "Чизуру Ямагучи"
	],
    "Члены клуба спорта, кроме лидера":[
        "Эцуджи Одака",
        "Фуюкичи Като",
        "Эцуко Хаяшибара",
        "Фуюми Тачики"
	],
    "Члены клуба садоводства, кроме лидера":[
        "Хозуми Такеда",
        "Ивао Сато",
        "Хонока Киёкава",
        "Ицуми Юуки",
	],
	"Правонарушители":[
        "Сейширо Саданага",
		"Тайчи Хиранака",
		"Шичиро Куросапу",
		"Того Атацума",
		"Сабуро Мешино"
	],
    "Правонарушительницы":[
        "Тиру Суторику",
		"Дорэми Шимахара",
		"Мурасаки Нобумото",
		"Акари Комияку",
		"Райму Ичиджо"
	],
    "Студенческий совет":[
        "Рейичи Танаами",
        "Дайсаку Арагаки",
        "Джозе Шиуба",
        "Кен Кёнашима"
	],
	"Радужные парни":[
		"Харуто Юто",
		"Сора Сосуке",
		"Рюсей Коки",
		"Сота Юки",
		"Хаято Харуки"
	],
	"Радужные девушки":[
		"Юи Рио",
		"Юна Хина",
		"Меи Мио",
		"Кохару Хината"
	],
}


API = "https://yandere-simulator.fandom.com/ru/api.php?action=getmap&format=json&name={0}_неделя_(1980)"
maps = []
for i in range(1,11):
	maps.append(json.loads(requests.get(API.format(str(i))).content)["content"]["markers"])

while True:
	chosen_character = ""
	while True:
		chosen_character = input("Which character or group would you like to see? (enter \"Characters\" or \"Groups\" to see the list of characters or groups):\n>> ")
		if chosen_character in NAMES or chosen_character in GROUPS:
			break
		elif chosen_character == "Groups":
			for category in GROUPS:
				print(category)
			print()
		elif chosen_character == "Characters":
			i = 1
			for name in NAMES:
				print(name)
				if i % 25 == 0:
					print()
					input("Press Enter to see the next page.")
					print()
				i += 1 
			print()
		else:
			print("Incorrect input.")
	chosen_character = translated[chosen_character]

	res = []
	res_groups = []
	week = 1
	for map_ in maps:
		visits = {}
		groups = [l for l in CATEGORIES.keys() if chosen_character in CATEGORIES[l]]
		visits_groups = {key:{} for key in groups}
		for i in range(len(map_)):
			a = map_[i]["popup"]["description"].split("\n")
			for j in range(len(a)):
				if (x := a[j].find(chosen_character)) != -1:
					k = j - 1
					while not a[k][0].isdigit():
						k-=1
					try:
						visits[a[k]].append(map_[i]["position"])
					except KeyError:
						visits[a[k]] = [map_[i]["position"]]
				for group in groups:
					if (x := a[j].find(group)) != -1:
						k = j - 1
						while not a[k][0].isdigit():
							k-=1
						try:
							visits_groups[group][a[k]].append(map_[i]["position"])
						except KeyError:
							visits_groups[group][a[k]] = [map_[i]["position"]]
								
		res_groups.append(visits_groups)
		res.append(visits)
		week+=1

	print(f"This {('Student', 'Group')[chosen_character in CATEGORIES.keys()]} visits:\n")
	for i in range(len(res)):
		print(f"On Week {i+1}")
		for j in res[i].keys():
			print("At {0} they are {1}.".format(j, ", ".join([which_location_student_is_in(p) for p in res[i][j]])))
		for group in res_groups[i].keys():
			for j in res_groups[i][group].keys():
				print("(As member of the \"{0}\") at {1} they are {2}.".format(translated_RU_EN[group], j, ", ".join([which_location_student_is_in(p) for p in res_groups[i][group][j]])))
		print()
		input("Press Enter to continue...")
		print()
					
