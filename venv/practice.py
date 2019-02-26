# 1 Question
inputted = input("Enter serial numbers?")
list = [int(i) for i in inputted.split(",")]
print(sum(list))


# 2 Question
def toLetter(let):
    splited = let.split(".");
    newLetter = "";
    for i in range(len(splited)):
        newLetter += splited[i].strip().capitalize();
        if (i + 1) != len(splited):
            newLetter += ". "
    return newLetter;


print(toLetter("hello world. how are you. fine."))

# 3 Question
myTuple = ("apple", "orange", "kiwi")
inputted = input("Enter a new Words (separate words by space):")
words = inputted.split(" ");
newTuple = tuple((str(i) for i in words));
print(newTuple + myTuple)


# 4 Question
list = ["Python" , "Java","Kotlin" , "Swift" , "VB" , "C#"]

isExist1 = 'Java' not in list
isExist2 = 'python' in list;

print(isExist1)
print(isExist2)


# 5 Question
import sys
keys = input("Enter keys (Separate by ,):").split(",");

if len(keys) > 3:
    print("You should enter only 3 item for keys.")
    sys.exit()

values = input("Enter values (Separate by ,):").split(",");
dic = dict();
for i in range(len(keys)):
    dic[keys[i]] = values[i];

print(dic)



# 6 Question
myList = {"0" : "A" , "1" :"B", "2" : "C" , "3" : "D"};
print(type(myList.keys())); # type is dic_key
print(type(myList.values())); #type is dic_val

keyList = list(myList.keys());
valueList = list(myList.values());

