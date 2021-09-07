import os
from os import listdir
from os.path import isfile, join

os.chdir(r'/Users/apple/Downloads/')

my_path = os.getcwd()


kivy_list = []

onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

for i in onlyfiles: 
    if 'pdf' in i: 
        if 'Kivy' in i: 
            kivy_list.append(i)
    else: 
        continue

print(kivy_list)
#with open('list_of_files.txt', 'w+') as f: 
    #for j in kivy_list: 
        #f.write(j, sep = ',')
        
    