import random

def numbers():

    random_num = random.randint(1, 100)
    my_num = int(input("pick num from 1 - 100:"))

    if random_num == my_num:
        print("nice job!")
    
    else:
        print("not correct num")

numbers()