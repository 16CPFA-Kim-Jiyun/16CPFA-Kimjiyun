#-*-coding:cp949
from sys import argv
#  Import argv from system modul
script, input_file = argv
# variables are script and input_file
def print_all(f):
    print (f.read())
# print all�� f�� ��� ���,���� f�� pritn�� ����.
def rewind(f):
    f.seek(3)
# rewind and seek 0 seak�� ó����ġ�� ���ư���  , f.read�� ���� 0������ ���ư��� �Ѵ�.
def print_a_line(line_count, f):
    print ("%d %s" % (line_count, f.readline()))
# formatter
current_file = open(input_file)
# read file
print ("First let's print the whole file:�n")
# read
print_all(current_file)
# show file's contents (��� ȣ���ض�)
print ("Now let's rewind, kind of like a tape.")
# read
rewind(current_file)
# rewind file
print ("Let's print three lines:")
# read
current_line = 1
print_a_line(current_line, current_file)
# read def
current_line = current_line + 1
print_a_line(current_line, current_file)
# read def
current_line = current_line + 1
print_a_line(current_line, current_file)
# read def