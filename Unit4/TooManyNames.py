#Write a function called name_counts. name_counts will take
#as input a list of full names. Each name will be two words
#separated by a space, like "David Joyner".
#
#The function should return a dictionary. The keys to the
#dictionary will be the first names from the list, and the
#values should be the number of times that first name
#appeared.
#
#HINT: Use split() to split names into first and last.


#Add your function here!

def name_counts(Alist):
    dictotal = {}
    for item in Alist:
        item = item.split()
        if item[0] in dictotal:
            dictotal[item[0]]+=1
        else:
            dictotal[item[0]]=1

    return dictotal

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))



