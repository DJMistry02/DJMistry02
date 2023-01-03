#install PyPDF2 using the command: pip install PyPDF2 in python terminal
#import necessary libraries
import os,PyPDF2
#change directory to directory of the pdf files
os.chdir(r'C:\Users\dhair\PycharmProjects\JStask\demo text')
#obtain list of files to be analyzed
file_list = os.listdir()
#initialize variables to keep track of necessary details
dup = 0
num = 0
for file in file_list:
    #open file in binary-read mode
    f = open(file, 'rb')
    #let PyPDF2 read the pdf and extract data from it
    reader = PyPDF2.PdfReader(f)
    #for every page in the document
    for i in range(len(reader.pages)):
        #extract words into a list
        file_deets = reader.pages[i].extract_text().split()
        #creating a set to identify duplicate words
        whole = set()
        for word in file_deets:
            #counting number of characters
            num += len(word)
            #if word is a duplicate
            if word in whole:
                dup += 1
            else:
                whole.add(word)

print('The number of duplicate words is',dup,'and the total number of characters is',num)


#Code written by Dhairya Mistry.