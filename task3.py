from os import listdir


# file_names = ["1.txt", "2.txt", "3.txt"]

files_in_dir = listdir("task3-files-toread/")
files_info = []
for file_name in files_in_dir:
    with open("task3-files-toread/" + file_name, encoding="utf-8") as file:
        content = file.read()
        file_length = len(content.split('\n'))
        files_info += [{"name": file_name, "length": file_length, "contents": content}]
sorted_files = sorted(files_info, key=lambda dict: dict["length"])
# for file in sorted_files:
#     print(file["name"])
#     print(file["length"])
#     print(file["contents"])

with open("task3.txt", "w", encoding="utf-8") as document:
    for file in sorted_files:
        document.write(file["name"] + "\n")
        document.write(str(file["length"]) + "\n")
        document.write(file["contents"] + "\n")