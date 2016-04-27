#-*-coding:cp949
from sys import argv
#  Import argv from system modul
script, input_file = argv
# variables are script and input_file
def print_all(f):
    print (f.read())
# print all은 f를 모두 출력,변수 f는 pritn로 들어간다.
def rewind(f):
    f.seek(3)
# rewind and seek 0 seak는 처음위치로 돌아간다  , f.read한 것을 0값으로 돌아가게 한다.
def print_a_line(line_count, f):
    print ("%d %s" % (line_count, f.readline()))
# formatter
current_file = open(input_file)
# read file
print ("First let's print the whole file:굈")
# read
print_all(current_file)
# show file's contents (모두 호출해라)
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