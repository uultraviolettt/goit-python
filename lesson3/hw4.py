import os
import sys

# input a valid address of the folder
path = sys.argv[1]
print(f"Start in {path}")

# list of file names of the  folder
files = os.listdir(path)

# set for file extensions
extensions_names = set()

image_files = []
document_files = []
video_files = []
music_files = []
unknown_ff = []

image_ext = ('.jpeg', '.png', '.jpg', '.pdf')
document_ext = ('.doc', '.docx', '.txt')
video_ext = ('.avi', '.mp4', '.mov')
music_ext = ('.mp3', '.ogg', '.waw', '.amr')

name_l, index_of_dot = 0, 0

# sorting
for file in files:
    name_l = len(file)
    for char in file:
        index_of_dot = file.rfind('.')
    extensions_names.add(file[index_of_dot:name_l:1])
    if file.endswith(image_ext):
        image_files.append(file)
    elif file.endswith(document_ext):
        document_files.append(file)
    elif file.endswith(video_ext):
        video_files.append(file)
    elif file.endswith(music_ext):
        music_files.append(file)
    else:
        unknown_ff.append(file)

print(f"Image files: {image_files} \n"
      f"Document files: {document_files} \n"
      f"Video files: {video_files} \n"
      f"Music files: {music_files} \n"
      f"Unknown files or folders: {unknown_ff} \n"
      )
print(
    f"We have sorted files with the following extensions in this folder: {extensions_names}")
