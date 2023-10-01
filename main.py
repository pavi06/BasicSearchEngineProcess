import json
#importing the package

from difflib import get_close_matches
#used to provide the most relevant words to it

jsonfile=json.load(open("schoolData.json",'r'))
#read mode
#loading the file to look for the data

word=input("Enter the word: ")
def check(d):
    d=d.lower()
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys()))>0:
        choice=input("Did you mean %s\nEnter y to continue else enter n : " %get_close_matches(d,jsonfile.keys())[0])
        if choice=='y':
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif choice=='n':
            return "Sorry! The word doesn't exists."
        else:
            return "Enter the correct choice"
    else:
        return "Sorry! The word doesn't exists. Please enter the correct word!"
res=(check(word))
if type(res)==list:
    print(*res)
else:
    print(res)