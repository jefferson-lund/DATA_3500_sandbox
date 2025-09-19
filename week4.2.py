import random


# for i in range(1, 10+1):
#     print(f"i = {i}")

# counter = 0

# # for i in range(10):
# #     counter**=2
# #     print(f"counter: {counter}")

# number = str(179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216)
# for i in number:
#     counter+=1
# print(f"\nprinted a {counter} digit number.\n")
# age = 0
# while age <= 20:
#     print(f"you are {age} years old")
#     age += 1

secret_number = random.randint(1, 100)
guess = 101
while guess != secret_number:
    guess = int(input("guess my secret number >"))
    if guess > secret_number:
        print("nuber too high, guess again")
    elif guess < secret_number:
        print("number too low, guess again")
    elif guess == secret_number:
        print(f"You got it! The number was {secret_number} all along!")
    else:
        print("that's not it, guess again")
        