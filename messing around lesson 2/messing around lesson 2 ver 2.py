

alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '|', '/', '_', '+', '-', '=', ';', ':', '"', "'", '`', '~', ' ']

message_list = []
encode_list = []
message_size = 0

for x in range(10):
    print('\n')

red = 0
green = 0
blue = 0
hor_move = 0

message = input("What message do you want to send?  ")
print("Message type", type(message))

trying = True
while trying:
    try:
        code = int(input("What do you want the secret code to be?  "))
        distance = int(input("Enter a nubmer between 1 and 100"))
        if not(distance > 100 or distance < 0):
            trying = False
        else:
            print("try again")
    except ValueError:
        print("Please enter a valid number \n")

for x in message:
    temp_code = alpha.index(x) * code
    temp = int(temp_code/16777216)
    if temp != 0:
        hor_move += temp
        temp_code -= (temp * 16777216)
    red = temp_code % 256
    temp_code = int(temp_code/256)
    green = temp_code % 256
    temp_code = int(temp_code/256)
    blue = temp_code % 256
    encode_list.append((str(red) + "," + str(green) + "," + str(blue)) + "," + str(hor_move))

print(encode_list)