# -*-coding: utf8

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 참 이라서 루프가 유지된다. while 문에서 위에 more_stuff의 뒤에서 세번째까지를 ten_things의 뒤에 연결되게 한다.
while len(stuff) !=10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There are %d items now." % len(stuff))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool! , stuff사이에 '  '를 넣어주기 (문자열 자료형 참고)
print ('#'.join(stuff[3:5])) # super stellar!
