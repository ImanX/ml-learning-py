letter = "hello World. you are Ok. yes OK"
x = "Hello world";


def toLetter(let):
    splited = let.split(".");
    newLetter = "";
    print (letter)
    for i in range(len(splited)):
        newLetter += splited[i].strip().capitalize();
        if (i + 1) != len(splited):
            newLetter += ". "
    return letter;


print (toLetter(letter))

print(x[x.find("o"):len(x)]);
