from random import shuffle

def shuffle_word(word):
	word = list(word)
	shuffle(word)
	return ''.join(word)

myName = input ("Please enter your name...")
print (shuffle_word(myName))