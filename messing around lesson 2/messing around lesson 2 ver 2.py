import cv2
import math

for x in range(10):
    print('\n')

alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '|', '/', '_', '+', '-', '=', ';', ':', '"', "'", '`', '~', ' ']

replace_list = []
encode_list = []

height = 1
width = 0
red = 0
green = 0
blue = 0
#hor_move = 0

message = input("What message do you want to send?  ")
print("Message type", type(message))

trying = True
while trying:
    try:
        code = int(input("What do you want the secret code to be?  "))
        code = code % 176602
        trying = False
    except ValueError:
        print("Please enter a valid number \n")

for x in message:
    temp_code = alpha.index(x) * code
    temp = int(temp_code/16777216)
    red = temp_code % 256
    temp_code = int(temp_code/256)
    green = temp_code % 256
    temp_code = int(temp_code/256)
    blue = temp_code % 256
    encode_list.append(str(red) + "  " + str(green) + "  " + str(blue))
print(encode_list)

img = cv2.imread('assets/logo.jpg', 1)
width = int(img.shape[0]) #I love this line of code. Its not much, but I still love it. Will I explain it? No lol

if int(width/100) < len(message):
    height = int(math.ceil(width / len(message)))
    print(height)
    width = int((width / 100) % len(message))
    print(width)

    for x in range(height):
        height -= 1
        for y in range(width):
            width -= 1
#            img.shape.replace(img[width,height], img[width,height], encode_list.pop(0))
#I don't know how to replace elements in a numpy array yet, so now I need to go learn numpy. brb i guess