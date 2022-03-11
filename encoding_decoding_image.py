# Ref : https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
from PIL import Image


#  encoding the image reindeer.gif
# 1. open the file
# 2. read its content
# 3. pass the path to the encode function base64.b64encode()
# 4. use base64_bytes.decode('utf-8') to print base64_str w/o prefix b'

with open("reindeer.gif", "rb") as image_file:
    my_path = image_file.read()
    base64_bytes = base64.b64encode(my_path)
print(base64_bytes.decode('utf-8'))

# decoding an image
image_64_decode = base64.b64decode(base64_bytes)
image_result = open('deer_decode.gif', 'wb')   # create a writable image and write the decoding result
image_result.write(image_64_decode)

# open the decoded image
# absolute path in raw string
absolute_image_path = r"/Users/macbookpro/PycharmProjects/LapTrinhGiaiToan/Python_Level_1_TUD D2020/deer_decode.gif"
decoded_image_1 = Image.open(absolute_image_path)
decoded_image_1.show()
# relative path
# decoded_image_2 = Image.open("deer_decode.gif")
# decoded_image_2.show()
