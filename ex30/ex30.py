# -*-coding:utf8

people = 13
cars = 25
trucks = 30

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
# else는 if에서의 비교가 아닐때 그 else값이 출력되고, elif는 다양한 조건을 판단한다.

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")