#-*-coding:cp949

x = "There are %d types of people." % 10
# 2 Ÿ���� ��� ������ �ִ�
binary = "binary"
# binary
do_not = "don't"
# �𸣴�
y = "Those who know %s and those who %s." % (binary, do_not)
# binary�� �ƴ� ����� �𸣴� ����� �ִ�
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# 2���� ������ ����� �ִ�
hilarious = False
# ��� = ����
joke_evaluation = "Isn't that joke so funny?! %r"
# ��� �� = ��� ����
print joke_evaluation % hilarious
# ��� �� = ��� ����
w = "This is the left side of..."
# ����
e = "a string with a right side."
# �������� ���ڿ�
print w + e
