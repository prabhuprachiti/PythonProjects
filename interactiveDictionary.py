import json
import difflib
data = json.load(open("dict.json"))

while True:
    word = input("Give me a word!\n")

    try:
        for w in data[word.lower()]:
            print (w)
        break

    except KeyError:
        if word.title() in data:
            for w in data[word.title()]:
                print (w)
            break

        if word.upper() in data:
            for w in data[word.upper()]:
                print (w)
            break

        reco_words = difflib.get_close_matches(word,data)

        if len (reco_words) > 0: #to check for incorrectly spelled words
            print ("Did you mean \"" + reco_words[0] + "\"??")
            response = input("Enter Y for YES and N for NO \n")

            if response == "Y":
                for w in data[reco_words[0]]:
                    print(w)
                break
            elif response == "N":
                print("Sorry! That word does not exist")
            else:
                print ("Please try again!")

        else:
            print ("Not a real word! Try Again!")