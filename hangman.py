import random
name = input("Enter Name: ");
print("Welcome " + name)
print("You have 10 turns left to guess the word(lower case letters only)")
print("-----------------------------------------------------------------")

words = ["aeroplane" , "cars" , "windows" , "laptop" , "avengers"]
turns = 10;
guessed = "";
complete = 0;
word = random.choice(words);
def hangman(turns):
	if(turns==10):
		print("-----")
	elif(turns==9):
		print("-----")
		print("  o  ")
	elif(turns==8):
		print("-----")
		print("  o  ")
		print("  |  ")
	elif(turns==7):
		print("-----")
		print("  o  ")
		print("  |  ")
		print(" /   ")
	elif(turns==6):
		print("-----")
		print("  o  ")
		print("  |  ")
		print(" / \\")
	elif(turns==5):
		print("-----")
		print(" \\o  ")
		print("  |  ")
		print(" / \\")
	elif(turns==4):
		print("-----")
		print(" \\o/ ")
		print("  |  ")
		print(" / \\")
	elif(turns==3):
		print("--|--")
		print(" \\o/ ")
		print("  |  ")
		print(" / \\")
	elif(turns==2):
		print("--|__")
		print(" \\o/ ")
		print("  |  ")
		print(" / \\")
	elif(turns==1):
		print("__|__")
		print(" \\o/ ")
		print("  |  ")
		print(" / \\")
	elif(turns==0):
		print("__|__")
		print("  o  ")
		print(" /|\\")
		print(" / \\")
def display(word):
	result = ""
	for i in word:
		if i in guessed:
			result+=i;
		else:
			result+="_"	
	return result;	
valid_letters = "abcdefghijklmonpqrstuvwxyz"	
while(turns>0):
	print('\n{} turns left'.format(turns))
	guess = input("Enter your guess: ")
	while guess not in valid_letters:
		guess = input("Enter valid letter please: ")
	while(guess in guessed):
		guess = input("Letter already used , Enter another: ")
	guessed+=guess;
	print(display(word))
	hangman(turns)
	if(display(word)==word):
		print("You win")
		break;
	turns = turns - 1;
if(turns==0):
	print("You lost")
	print("WORD WAS " + word)
	hangman(turns)

