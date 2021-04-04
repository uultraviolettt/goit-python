import os
from pathlib import Path
import re
import sys
from shutil import copyfile, move, unpack_archive


def normalize(string):
    s_map = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'g',
             ord('Г'): 'G', ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('ё'): 'yo', ord('Ё'): 'Yo',
             ord('ж'): 'zh', ord('Ж'): 'Zh', ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I', ord('й'): 'y',
             ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K', ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M',
             ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', ord('п'): 'p', ord('П'): 'P', ord('р'): 'r',
             ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', ord('у'): 'u', ord('У'): 'U',
             ord('ф'): 'f', ord('Ф'): 'F', ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts', ord('ч'): 'ch',
             ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh', ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y',
             ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '', ord('э'): 'e', ord('Э'): 'E',
             ord('ю'): 'yu', ord('Ю'): 'Yu', ord('я'): 'ya', ord('Я'): 'Ya', }
    translit_str = string.translate(s_map)
    fin_str = re.sub(r'\W', "_", translit_str)
    return fin_str


def sort_folder(p):
    os.chdir(str_pass)
    image_ext = ('.jpeg', '.png', '.jpg', '.pdf')
    document_ext = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.pptx', '.xlsx')
    video_ext = ('.avi', '.mp4', '.mov')
    music_ext = ('.mp3', '.ogg', '.waw', '.amr')
    arch_ext = ('.zip', '.gz', '.tar')

    if p.is_dir():
        for item in p.iterdir():
            sort_folder(item)
    else:
        file_name = p.stem
        file_ext = os.path.splitext(p)[1]
        if file_ext in image_ext:
            os.makedirs(str_pass + "\\images", exist_ok=True)
            move(p, str_pass + "\\images\\" +
                 normalize(file_name) + file_ext)
        elif file_ext in document_ext:
            os.makedirs(str_pass + "\\documents", exist_ok=True)
            move(p, str_pass + "\\documents\\" +
                 normalize(file_name) + file_ext)
        elif file_ext in video_ext:
            os.makedirs(str_pass + "\\video", exist_ok=True)
            move(p, str_pass + "\\video\\" +
                 normalize(file_name) + file_ext)
        elif file_ext in music_ext:
            os.makedirs(str_pass + "\\audio", exist_ok=True)
            move(p, str_pass + "\\audio" + normalize(file_name) + file_ext)
        elif file_ext in arch_ext:
            os.makedirs(str_pass + "\\archives", exist_ok=True)
            unpack_archive(p, str_pass + "\\archives\\")


print("Finally sorted!)")


def main():
    global str_pass
    str_pass = sys.argv[1]
    path = Path(sys.argv[1])
    sort_folder(path)


if __name__ == '__main__':
    main()
