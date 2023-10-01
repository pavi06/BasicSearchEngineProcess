dict={"name":"Pav","Age":"21","Gender":"Female"}
word=input("Enter the word: ")
def check(d):
    if d in dict:
        return dict[d]
print(check(word))
#can be used if working with few info. But, considering apps lot of users will be involved so make use of json format, where the info is collected as an object in key value pair of strings and can use it anywhere. 

