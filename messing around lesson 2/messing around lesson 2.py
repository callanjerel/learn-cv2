#code by callanjerel, secret message encodes in image

#last time I just finished up the encoding of the numbers. Take off from there, i got the encoder to work and its beautiful
import cv2
import random

img = cv2.imread('assets/logo.jpg', -1)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', ';', '!', '@', ':', '"', "'", '<', '>', '?', '/', '[', ']', '{', '}', '|', '#', '$', '%', '^', '&', '*', '(', ')']

for x in range(100):
    print('\n')

print(img.shape)

def encode(message):
    red = 0
    green = 0
    blue = 0
    running_secret_key = True
    encoding = True
    print('\n \n')
    print("encoding function \n")
    while running_secret_key:
        secret_key = input("enter a number\n")
        try:
            int(secret_key)
            running_secret_key = False
        except ValueError:
            print('\n')
            print("Enter a valid number")
    secret_key = int(secret_key)
    while encoding:
        if secret_key == 0:
            break
        red += 1
        secret_key -= 1
        print(red,green,blue)
        if red == 255:
            if secret_key == 0:
                break
            red = 0
            green += 1
            secret_key -= 1
            print(red,green,blue)
            if green == 255:
                if secret_key == 0:
                    break
                green = 0
                blue += 1
                secret_key -= 1
                print(red,green,blue)
    print("lol")

running_choice = True

while running_choice:
    choice = input("Would you like to encode or decode a message? \n")
    running_choice = True
    if choice.lower() == "encode":
        message = input("What message would you like to send? \n")
        encode(message)
        running_choice = False
    elif choice.lower() == "decode":
        secret_key = input("What is the secret key? \n")
        print("decode text")
        running_choice = False
    else: print("please type encode or decode \n")





#tag = img[20:70, 20:70]
#img[70:120, 70:120] = tag

#print(img)
#print(img.shape)
#print(type(img))

#cv2.imshow('img',img)
#cv2.waitKey(0)
#]cv2.destroyAllWindows()