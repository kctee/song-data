"""
pandasearch.py
written for Python 3

Uses pandas to search through a preformatted database of song information

2016 by Matt Tillman

What I want to be able to do is :

1.  enter a title and usually and artist

2.  search all the different databases to see if it there.

3.  If found, I want to know the:
A. database(1d)
B. year
C. ranking
D. title
E. artist
F. itune

4. Print output that looks like excel output
"""

### IMPORTS
import pandas as pd
import sys
import os    #added to try and find csv file line 46

### FUNCTIONS

def slicer(frame,column,term):
    """
    A simple function that slices a dataframe (frame) on a given (column) for a given search (term)
    Usefull for sequential slicing
    """
    outframe = frame.loc[frame[column] == term]
    return outframe

### SETUP SEARCH AND USER INPUTS

# change this as appropriate for the filename
#filename = 'test.csv'
# remove line above and replaced fi=ollowing rwt 1/7/17 got from stackoverflow
filename = os.path.join(os.path.dirname(__file__), 'test.csv')
print (filename)               
# if you like, comment out the line above and remove the comment from the line below and it will be user input
#filename = input('Input filename: ')

database = pd.read_csv(filename, header =0)

# changed raw_input to input rwt 1/7/17
#searchmode = raw_input('Search by (A)rtist, (T)itle or (B)oth? ')
searchmode = input('Search by (A)rtist, (T)itle or (B)oth? ')
print (filename)  
outfile = 'outfile.csv'
# if you like, comment out the line above and remove the comment from the line below and it will be user input
#outfile = raw_input('Output filename: ')

### SEARCH (REALLY A PANDAS SLICE FUNCTION)
print (filename)  
if (searchmode == 'A' or searchmode == 'a'):
    # changed raw_input to input rwt 1/7/17
    #searchterm = raw_input('Artist to search for: ')
	print (filename)  
	searchterm = input('Artist to search for: ')
	finalframe = slicer(database,'Artist',searchterm)
elif (searchmode == 'T' or searchmode == 't'):
	searchterm = input('Title to search for: ')
	#searchterm = raw_input('Title to search for: ')
	finalframe = slicer(database,'Title',searchterm)
elif (searchmode == 'B' or searchmode == 'b'):
	searchterm = input('Artist to search for: ')
	#searchterm = raw_input('Artist to search for: ')
	interimframe = slicer(database,'Artist',searchterm)
	searchterm = input('Title to search for: ')
	#searchterm = raw_input('Title to search for: ')
	finalframe = slicer(interimframe,'Title',searchterm)
else:
    print('Invalid Search Term Dumbass')
    sys.exit(0)


### OUTPUT
finalframe.to_csv(outfile, sep=',',encoding = 'utf-8')
