print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split()
text1 = str1[-2:] + str1[0:-2]
text2 = str2[3:] + str2[0:3]
rounds = 1
while(text1 != str1 or text2 != str2):
    if rounds <= 5:
        print(str(rounds), text1, text2)
    text1 = text1[-2:] + text1[0:-2]
    text2 = text2[3:] + text2[0:3]
    rounds += 1
if rounds > 5:
    print(" . . . . . ")
print(str(rounds), text1, text2)
print(f"Total of  {rounds} rounds.")