from random import randint

array = [7, 9, 2, 1, 5, 3];
print("unsorted:", array)
for i in range(len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            temp = array[i];
            array[i] = array[j];
            array[j] = temp

print("sorted:", array)

array = [None] * 100
for i in range(100):
    v = randint(1, 10)
    array[i - 1] = v

length = len(array)
while length >= 0:
    val = array[length - 1];
    if val % 2 == 0:
        print("Even ", val)
    else:
        print("Odd ", val);
    length -= 1;


class Math:
    def get(self, val):
        for i in range(val):
            print(i, ":")
            for x in range(10):
                print(i, "*", x, "=", i * x)


