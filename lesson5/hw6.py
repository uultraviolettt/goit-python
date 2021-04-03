import re
test: str = input()


def normalize(string):

    s_map = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G', ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('ё'): 'yo', ord('Ё'): 'Yo', ord('ж'): 'zh', ord('Ж'): 'Zh', ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I', ord('й'): 'y', ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K', ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', ord('п'): 'p', ord('П'): 'P', ord('р'): 'r', ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F', ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts', ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh', ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y', ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '', ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'yu', ord('Ю'): 'Yu', ord('я'): 'ya', ord('Я'): 'Ya', }
    translit_str = string.translate(s_map)
    fin_str = re.sub(r'\W', "_", translit_str)
    return fin_str


# test
print(normalize(test))