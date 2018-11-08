#!/usr/bin/python
import json
import random

data = json.load(open("dict.json"))

word = " "
while " " in word: #to limit the selection to only single words
    word = (random.choice(list(data.keys()))).lower()

turns = 7
guessed_word = ""
wrong_alphabets = []

for w in word:
	guessed_word += "*" #adding a star for every alphabet of the word

print "The word has " + str(len(word)) + " letters\n"

while turns > 0: #do till all the chances are exhausted
	
	alpha = (raw_input("Enter an alphabet:")).lower() #getting the alphabets from std. input
	
	if (alpha not in word) and (alpha not in wrong_alphabets):
		print "Wrong"
		wrong_alphabets.append(alpha) #if the guessed alphabet is not present in the word, add it to the list of wrongly guessed alphabets
		turns -= 1
	elif alpha in word:
		print "Correct"
        else:
            print "Wrong"
	
	for idx, a in enumerate(word):
		if alpha == a:
			guessed_word = guessed_word[:idx] + a + guessed_word[idx+1:] #replacing the star with the correct alphabets
        print guessed_word
        print "Turns remaining %s and wrong alphabets: %s" %(turns, wrong_alphabets)
        
	if guessed_word == word:
		print "Yay! You won!"
		break

        #printing out the hangman drawing
        if turns == 6:
            print "  O"
            
        elif turns == 5:
            print "  O\n  |"
            
        elif turns == 4:
            print "  O\n \|"
            
        elif turns == 3:
            print "  O\n \|/"
            
        elif turns == 2:
            print "  O\n \|/\n  |"
            
        elif turns == 1:
            print "  O\n \|/\n  |\n /"
            
        elif turns == 0:
            print "  O\n \|/\n  |\n / \ "
            print "Game Over!\nThe word was "+ word
       
        print "----------------------------------------------------------------------------"
