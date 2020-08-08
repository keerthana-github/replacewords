
import random

try:
  # open up the thesaurus file
  fp = open("python_asg10_Roget_Thesaurus.txt", "r")
except:
  print ("Can't open file")
else:
  data = fp.read().lower()
  fp.close()

  # isolate each entry
  line = data.split("\n")
  
  # set up a dictionary to hold all of our thesaurus words
  thesaurus = {
              "happy": "glad",
              "sad"  : "bleak"
            }
  total=0
  # visit every line in the file
  for words in line:
    split_words=words.split(",")
    initial=split_words[0]
    rest = split_words[1:]

    #add the words to out dictionary
    thesaurus[ initial ] = rest
    total+=1

  print("Total words in thesaurus:", total)
  print()
  # ask the user for a word
  phrase = input("Enter a phrase: ")
  #split the words
  words = phrase.split(" ")

  for word in words:
    # see if we know about this word
    clean = ""
    for c in word:
      if c.isalpha():
        clean += c
    #make the word lower
    lower=clean.lower()
    #if it's in thesaurus
    if lower in thesaurus:
      #store the synonym 
      new_word=thesaurus[lower][random.randint(0, len(thesaurus[lower])-1)]
      #print the synonym in caps
      print (new_word.upper(), end=" ")
    #if not, add the regular word
    else:
        print(clean,end=" ")
