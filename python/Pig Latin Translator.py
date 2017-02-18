
# Find out why hyphens don't work correctly.




print "Welcome to the Pig Latin translator!"




attempt = 0




def lf(item) :  # Letter(s) Finder

    if word.startswith(item) or word.startswith(item.upper()) or word.startswith(item[0:1].upper()+item[1:]) :

        return True




def ssi(sound) :  # Starting Sound Is ...

    if lf(sound) :

        ssl = len(sound)  # Starting Sound Length




vowels = "AaEeIiOoUu"

uppercase = False

"""

def fv(vowel) :  # Find Vowel

    try :

        vowels = word.index(vowel)

    except :

        letter = 0

"""




def ca(ep):  # Contains Apostrophe (Ending Punctuation)

    if ep :

        try :

            contraction = word.split("'")

            if contraction[1].isalpha() :

                return True

            else :

                return False

        except :

            return False

    else :

        try :

            contraction = word.split("'")

            if contraction[1].isalpha() :

                return False

            else :

                return True

        except :

            return False




def startsWithVowel() :

    for letter in vowels :

        if word[0] == letter :

            return True

            break




newText = ""




while True :  # make "attempt" less than or equal to a number to limit the times to repeat.

    original = raw_input("Enter some text to translate.\n")

    newText = ""

    if original == "QUIT" :

        break

    if original.upper() == original :

        uppercase = True

    original = original.split(" ")

    for word in original :

        indexList = []

        if word.isalpha() or ca(True) :

            """

            ssi("th")

            ssi("sh")

            ssi("ch")

            ssi("ph")

            ssi("qu")

            ssi("kn")

            ssi("ts")

            ssi("wh")

            for vowel in range("a", "e", "i", "o", "u") :

                if lf(vowel) :

                    ssl = 0

            """

            for letter in vowels :  # this has to be "letters"

                try :

                    indexList.append(word.index(letter))

                except :

                    indexList.append(100)

            if startsWithVowel() :

                newText += " "+word[min(indexList):]+word[0:min(indexList)].lower()+"yay"

            else :

                newText += " "+word[min(indexList):]+word[0:min(indexList)].lower()+"ay"

        elif word[0:len(word)-1].isalpha() or ca(False) :

            for letter in vowels :  # this has to be "letters"

                try :

                    indexList.append(word.index(letter))

                except :

                    indexList.append(100)

            if startsWithVowel() :

                newText += " "+word[min(indexList):len(word)-1]+word[0:min(indexList)].lower()+"yay"+word[len(word)-1:]

            else :

                newText += " "+word[min(indexList):len(word)-1]+word[0:min(indexList)].lower()+"ay"+word[len(word)-1:]

    newText = newText.strip()

    newText = newText[0].upper()+newText[1:]

    if uppercase :

        print "\n"+newText.upper()

    else :

        print "\n"+newText

    

    attempt += 1