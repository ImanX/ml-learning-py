letter = "hello World. you are Ok. yes OK"

splited = letter.split(".");
newLetter = "";
print (letter)
for i in range(len(splited)):
    newLetter += splited[i].strip().capitalize();
    if (i+1) != len(splited):
        newLetter+=". "


print (newLetter)
