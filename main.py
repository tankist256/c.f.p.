meme_dict = {
            "ЛОЛ": "очень смешно",
            "КРИНЖ": "что-то странное, стыдное",
            "РОФЛ": "шутка",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ": "злиться",
            "ЩИЩ": "одобрение или восторг"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print("слово есть в словаре")
else:
    print("слова нет в словаре")