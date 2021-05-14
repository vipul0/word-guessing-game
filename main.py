import random

print(" \t \t Welcome to the word guessing game \n \n")

user=input("Enter your name: ")
print(f"\n Welcome to the game {user}")


words=["linux", "sunflower", "mango", "television", "asia", "monitor", "earphone", "forest", "game"]

guesses=""

#picking the random index
index=random.randint(0, len(words))
word=words[index]

#filling random char in selected
fill=random.sample(range(0, len(word)), 2)

for i in fill:
    guesses+=word[i]

life=10

play=True

def playAgain():
    #check if user wants to continue the game
    choice=input("Do you want to conitnue the game: (yes/no) ")
    if choice=="yes":
        global word, life, guesses
        life=10
        index=random.randint(0, len(words))
        word=words[index]
        fill=random.sample(range(0, len(word)), 2)
        for i in fill:
            guesses+=word[i]

    else:
        global play
        play=False

while play:
    while life>0:
        won=True
        for i in word:
            if i in guesses:
                print(i, end="")
            else:
                print("-",end="")
                won=False


        if won:
            print("\n Hey, You won! \n")
            print("your score: ", life*10)
            playAgain()
            


        #take a guess from user
        guess=input("\n")
        guesses+=guess

        if guess not in word:
            life-=1
            print("\n Wrong answer. you loose one life!!")
            print(f"your life life in game {life}")

            if life == 0:
                print("You Lose")
                playAgain()

print("Thank you for playing. See you soon <3 ")
