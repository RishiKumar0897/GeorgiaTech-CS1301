


#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

names_file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
count = 0
new_list = []
highest = 0
highest_name = ''

names_list = []

for line in names_file:
    split_list = line.split(",")
    names_list.append(split_list[0])
    
sorted_names_list = sorted(names_list)

for name_index in sorted_names_list in range(0, len(sorted_names_list)-2):
    if sorted_names_list[name_index] == sorted_names_list[name_index+1]:
        dup_names_list.append(sorted_names_list[name_index])
    
    
print(dup_names_list)


#print(count)



