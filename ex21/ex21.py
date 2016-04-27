# coding: utf-8
# 참고문헌: hrrp://learnpythonthehardway.org/book/ex28.html
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b
# return의 역할 : (반환역할=)계산결과를 다른 함수로 받아서 쓸 수 있게 해준다. 21번째줄부터~~받아진다.
def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b
# a - b 값이 22째줄
def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b
# a*b 값이 23째줄
def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b
# a / b 값이 24쩨즐
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit. type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
