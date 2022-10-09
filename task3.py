from os import listdir


files_in_dir = listdir("task3-files-toread/")
files_info = []
for file_name in files_in_dir:
    with open("task3-files-toread/" + file_name, encoding="utf-8") as file:
        content = file.read()
        file_length = len(content.split('\n'))
        files_info += [{"name": file_name, "length": file_length, "contents": content}]
sorted_files = sorted(files_info, key=lambda dict: dict["length"])

with open("task3.txt", "w", encoding="utf-8") as document:
    for file in sorted_files:
        document.write(file["name"] + "\n")
        document.write(str(file["length"]) + "\n")
        document.write(file["contents"] + "\n")