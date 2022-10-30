question = input("enter a word: ")

answer = question
x = int(len(question))

if x < 10 :
    print("string not long enough")
elif x > 10 :
    print("string too long")

print(answer[0])
print(answer[-1])

mystr = answer
for i in range(len(mystr)+1):
    print (mystr[:i])


