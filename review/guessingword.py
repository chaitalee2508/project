import random
words = ("red", "blue", "purple", "yellow")
word = random.choice(words)

correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[: position] + word[ (position +1):]

print(
     """       *** Welcomme to the word jumble ***
     """
    )
print("The jumble is: ", jumble)

guess = input("\n Your guess:")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess! ")

if guess == correct:
    print("That's it! You guessed it!\n")

print("Thanks for playing!")

