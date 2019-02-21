import re

while(True):
  inputtedStr = input("Please Enter a Text:");
  findStr = input("What a char?");




  print(len(re.findall(findStr, inputtedStr)));

  splitted = inputtedStr.split(findStr);
  print(len(splitted) - 1);




inputed = input("Enter a prظompt:");
word1 = input("Enter Word1: ");
word2 = input("Enter Word1 ");

print(inputed.count(word1));


