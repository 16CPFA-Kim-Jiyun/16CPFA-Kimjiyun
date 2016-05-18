# -*-coding:utf8

i = 0
numbers = []

# while 문은 반복해서 문장을 수행할때 쓴당(무한루프)
while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1

    print ("Numbers now: ", str(numbers))
    print ("At the bottom i is %d" % i)


print ("The numbers: ")

for num in numbers:
    print (num)
