import sys
import os
import shutil

GLOBAL_PATH = ''

gen_fold = ['images', 'documents', 'videos', 'audios', 'archives']
imagesFilt = ['.jpg', '.png', '.jpeg']
videoFilt = ['.avi', '.mp4', '.mov']
docFilt = ['.pdf', '.docx', '.txt', '.xlsx']
musicFilt = ['.mp3', '.ogg', '.wav', '.amr']
arhiveFilt = ['.zip', '.7zip', '.gz', '.tar']


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

    stringN = []
    normalized = ''

    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            stringN.append(c)
        else:
            c = c.translate(s_map)
            stringN.append(c)
    return normalized.join(stringN)


def create_folders():
    for name in gen_fold:
        directory = os.path.join(GLOBAL_PATH, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


def relocateFile(filesInfo):
    create_folders()
    info = filesInfo.split(";")
    src = os.path.join(info[1], info[2] + info[3])
    dest = os.path.join(GLOBAL_PATH, info[0], normalize(info[2]) + info[3])

    if info[0] == 'archives':
        shutil.unpack_archive(shutil.move(src, dest),
                              os.path.join(GLOBAL_PATH, info[0]))
        os.remove(dest)
    else:
        shutil.move(src, dest)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


def fileDistribute(fileCollections, path, nestingDeep):
    for file in fileCollections:
        fileName, fileExt = os.path.splitext(file)
        if fileExt in imagesFilt:
            relocateFile(f'images;{path};{fileName};{fileExt}')
        elif fileExt in videoFilt:
            relocateFile(f'videos;{path};{fileName};{fileExt}')
        elif fileExt in docFilt:
            relocateFile(f'documents;{path};{fileName};{fileExt}')
        elif fileExt in musicFilt:
            relocateFile(f'audios;{path};{fileName};{fileExt}')
        elif fileExt in arhiveFilt:
            relocateFile(f'archives;{path};{fileName};{fileExt}')


def tPath(path, nestingDeep=0):
    fileSet = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            tPath(os.path.join(path, file), nestingDeep + 1)
        else:
            fileSet.append(file)
    fileDistribute(fileSet, path, nestingDeep)


def main():
    tPath(r'C:\Users\Lenovo\Desktop\to_sort')


def clean():
    global GLOBAL_PATH
    if len(sys.argv) == 1:
        GLOBAL_PATH = os.getcwd()
        tPath(GLOBAL_PATH)
    else:
        GLOBAL_PATH = sys.argv[1]
        tPath(GLOBAL_PATH)


if __name__ == '__main__':
    main()
