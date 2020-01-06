forbidden_num = 667
guess = input("guess a digit 1-1000 ")
print("your digit is " + str(guess) + " try again")
#+ str(forbidden_num))
while True:
    if int(guess) > 500:
        print("guess lower")
        #break
    if int(guess) < 668:
        print("guess higher")
        #break
    if type(guess) != int:
        print(str("please choose a digit 1-1000"))
    if guess == forbidden_num:
        print("bingo! you got it!")
        break