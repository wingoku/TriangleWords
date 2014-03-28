#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      WinGoku
# Website: 	   http://www.wingoku.com
# Created:     28/03/2014
# Copyright:   (c) WinGoku 2014
# Licence:     <Apache License>
#-------------------------------------------------------------------------------

import re

myList = [];

#triangle number formula
# finding triangle numbers upto 26 because there are only 26 english alphabets
for i in range(26):
    x = 0.5*(i*(i+1));
    myList.append(x);

myFile = open("C:\words.txt", "r" );

totalTriangle = 0;

line = "";

line = myFile.read()


# extracting words from the file
myWords = re.findall(r'"[a-zA-Z]+"', line);

x=0

for word in myWords:

    # getting rid of ""
    word = word[1:-1]

    x+=1
    letterSumTotal = 0;

    for j in range(len(word)):
        letter = word[j];

        #find ascii value
        asciiValue = ord(letter);

        # subtracting asciiValue of current character with ascii value of A=(65) to get position of alphabet in 1->26 range
        letterSumTotal += (asciiValue-65) + 1;

    # checking if sum of all letters in the word is in the list containing triangle numbers
    if letterSumTotal in myList:
        totalTriangle +=1;

print 'File contains: ', totalTriangle, " triangle word(s) out of ", x," total words";