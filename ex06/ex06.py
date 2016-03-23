#-*-coding:cp949

x = "There are %d types of people." % 10
# 2 타입의 사람 유형이 있다
binary = "binary"
# binary
do_not = "don't"
# 모르는
y = "Those who know %s and those who %s." % (binary, do_not)
# binary를 아는 사람과 모르는 사람이 있다
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# 2가지 유형의 사람이 있다
hilarious = False
# 재미 = 거짓
joke_evaluation = "Isn't that joke so funny?! %r"
# 농담 평가 = 재미 없다
print joke_evaluation % hilarious
# 농담 평가 = 재미 없다
w = "This is the left side of..."
# 왼편에
e = "a string with a right side."
# 오른편의 문자열
print w + e
