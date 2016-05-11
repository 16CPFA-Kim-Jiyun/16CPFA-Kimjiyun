# -*-coding:utf8

# http://euler.synap.co.kr/prob_detail.php?id=1
"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

"""

i = 3
numbers = []

while i < 1000:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 3
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

j = 5
numbers = []

while j < 1000:
    print "At the top j is %d" % j
    numbers.append(j)

    j = j + 5
    print "Numbers now: ", numbers
    print "At the bottom j is %d" % j

k = 15
numbers = []

while k < 1000:
    print "At the top k is %d" % k
    numbers.append(k)

    k = k + 15
    print "Numbers now: ", numbers
    print "At the bottom k is %d" % k

print "The numbers: "

for num in numbers:
    print num

print "i + j - k = ", (i + j - k)
