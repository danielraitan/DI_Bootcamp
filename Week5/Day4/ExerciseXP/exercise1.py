import random

with open("random.txt", mode='r') as file:
    lines = file.readlines()

filtered_list = []
for line in lines:
    filtered_list.append(line.strip('\n'))

def get_random_sentence():

    user_input = int(input("how long do you want the random sentence to be?"))

    if user_input > 20:
        print("sorry to long")

    elif user_input < 2:
        print("sorry to short")

    else:
         random_word = [random.choice(filtered_list) for _ in range(user_input)]

         mystring = " "

         for x in random_word:
            mystring += " "+ x

         print(f"here's your random sentence:{mystring.lower()}")

get_random_sentence()
 