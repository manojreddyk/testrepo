import sys
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches    
def meaning(wrd) :
    if wrd.lower() in data.keys() :
        return data[wrd.lower()]
    else :
        
        if len(get_close_matches(wrd.lower() , data.keys())[0]) > 0 :
            wrd=get_close_matches(wrd.lower() , data.keys())[0]
            print( "Did you mean %s, Please enter Y or N" %wrd)  
            option=input("Enter Y or N:")
            if option == "Y" :
                return data[wrd]
            else :         
                print( "Word does not exist")
                return wrd
        else :
            print("Word does not exist" )
            return wrd


data = json.load(open("files/data.json"))
while True:
    wrd = input("Enter your word:")
    if wrd == "\end" :
        break
    else :
        for  i in meaning(wrd) :
            print(i)
        continue
