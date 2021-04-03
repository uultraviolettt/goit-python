import os
import sys
from pathlib import Path
import re


image_files = []
document_files = []
video_files = []
music_files = []
arch_files = []
unknown_ff = []

known_ext = set()
unknown_ext = set()


def sort_folder(p):



    image_ext = ('.jpeg', '.png', '.jpg', '.pdf')
    document_ext = ('.doc', '.docx', '.txt',
                          '.pdf', '.xls', '.pptx', '.xlsx')
    video_ext = ('.avi', '.mp4', '.mov')
    music_ext = ('.mp3', '.ogg', '.waw', '.amr')
    archieve_ext = ('.zip', '.gz', '.tar')

    if p.is_dir():
        for item in p.iterdir():
            sort_folder(item)
    else:
        file = p.name
        file_ext = os.path.splitext(p)[1]
        if file_ext in music_ext:
            music_files.append(file)
            known_ext.add(file_ext)
        elif file_ext in image_ext:
            image_files.append(file)
            known_ext.add(file_ext)
        elif file_ext in document_ext:
            document_files.append(file)
            known_ext.add(file_ext)
        elif file_ext in video_ext:
            video_files.append(file)
            known_ext.add(file_ext)
        elif file_ext in archieve_ext:
            arch_files.append(file)
            known_ext.add(file_ext)
        else:
            unknown_ff.append(file)
            unknown_ext.add(file_ext)
    return music_files, image_files, document_files, video_files, arch_files, unknown_ff, known_ext, unknown_ext


def main():

    path = Path(sys.argv[1])
    sort_folder(path)


if name == 'main':
    main()


print(f"Image files: {image_files} \n"
      f"Document files: {document_files} \n"
      f"Video files: {video_files} \n"
      f"Music files: {music_files} \n"
      f"Archieve files: {arch_files} \n"
      f"Unknown files or folders: {unknown_ff} \n"
      )
print(
    f"We have files with the following extensions in this folder: {known_ext}")
print(
    f"We have unknown files with the following files extensions: {unknown_ext}")