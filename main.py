#TODO: Create a letter using starting_letter.txt
import time
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
namelist=[]
with open("./Input/Names/invited_names.txt","r") as names:
    name=names.read().split("\n")
    for nam in name:
        namelist.append(nam)
def fileopen():

    with open("./Input/Letters/starting_letter.txt","r") as letters:
        letter=letters.read()
        return letter

for nam in namelist:
    text=""
    letters=fileopen()
    for words in letters.split(" "):
        for nword in words.split(","):
            if nword == "[name]":

                text+=nam+","
            else :
                text+=nword+" "
    with open(f"./Output/ReadyToSend/{nam}.txt","w") as f:
        f.write(text )



    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp