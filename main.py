# Use the logical connective and rather than a double inequality.

'''
player_hand = 17
dealer_hand = 19

if (player_hand > dealer_hand) and (player_hand <= 21):
    print("The player wins!")

# Last time, we explored user input.

print()

name = input("What's your name? ")
print(f"Hello, {name}.")

# The input function interprets the user's input
# as a string!

print()

age_string = input("What's your age? ")
age = int(age_string)
if age > 60:
    print("You're old!")

print()

age = int(input("What's your age? "))
if age > 40:
    print("You're old!")

print()

# Chain if-elif-else is efficient.
user_response = input("Do you want to keep playing? (Enter Y or N) ")
if user_response == 'Y':
    print("Let's continue!")
# Otherwise if...
elif (user_response == "N"):
    print("Let's quit.")
else:
    print("Error!")

# Contrast with sequential if statements.
user_response = input("Do you want to keep playing? (Enter Y or N) ")
if user_response == 'Y':
    print("Let's continue!")
if user_response == "N":
    print("Let's quit.")
if (user_response != 'Y') and (user_response != 'N'):
    print("Error!")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print()

for i in range(5):
    print(i + 1)

# A for loop can be rewritten as a while loop.

print()

prompt = "\nTell me something, and " \
         "I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Streamline the while loop, so that we don't have two
# places in the while loop that check the same condition
# message != 'quit'.

prompt = "\nTell me something, and " \
         "I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    print(message)
    message = input(prompt)
# Does your code work as intended?

# A flag (active) is used to decide whether to continue
# in the while loop.
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Let's try to streamline.
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True
message = ''
while active:
    print(message)
    message = input(prompt)
    if message == 'quit':
        active = False
'''

# Using break to exit while loop.
prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I've been to {city}!")
