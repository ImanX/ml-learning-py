





def toLetter(let):
    splited = let.split(".");
    newLetter = "";
    for i in range(len(splited)):
        newLetter += splited[i].strip().capitalize();
        if (i + 1) != len(splited):
            newLetter += ". "
    return newLetter;



print(toLetter("this is python. this's a powerful language. it's response from a function. wow"))

# print(x[x.find("o"):len(x)]);
