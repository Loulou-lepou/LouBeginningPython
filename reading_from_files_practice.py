"""
1. count how many of each name there are in nameslist.txt
https://www.practicepython.org/assets/nameslist.txt
2. Count how many of each category of each image there are in Training_01.txt
https://www.practicepython.org/assets/Training_01.txt
"""
import requests
# from urllib.request import urlopen


names_url = "https://www.practicepython.org/assets/nameslist.txt"
# for line in urlopen(file_url):
#     # print(line)       # b'Darth\n' => b = a bytes literal
#     print(line.decode('utf-8'), end="")
response_names = requests.get(names_url)    # response [200] => valid url
names = response_names.text         # read the entire text file, return a long string
unique_names = set(names.split("\n"))
print(unique_names)
name_occurrences = [names.count(name) for name in unique_names]
print(name_occurrences)

images_url = "https://www.practicepython.org/assets/Training_01.txt"
response_images = requests.get(images_url)
image_paths = response_images.text.split("\n")
image_categories = {}      # empty dict
for line in image_paths:
    line_parts = line.split("/")
    new_key = '/'.join(line_parts[:-1])
    if new_key not in image_categories.keys():
        image_categories[new_key] = 1
    else:
        image_categories[new_key] += 1
for key, value in image_categories.items():
    print(key,":", value)
