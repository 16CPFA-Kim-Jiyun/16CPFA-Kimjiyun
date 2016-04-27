# -*-coding:utf8
print("Let's practice everything.")
print("You\'d need to know \'bout excapes with \\ that do \n newlines and \t tabs.")
# \은 백슬래시, \\은 백슬래시표현, \'은 문자열안에서 따음표들을 혼동없이 출력되게 해준다. \n은 한행아래로, \t는 tab기능
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# """ """ 은 여러 문자열 나열하게 해주고, 그 안에 입력한대로 출력됨.
print("-------------")
print(poem)
print("-------------")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# def 함수를 five 변수 보다 앞에 입력해도 출력된다!
five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("Whit a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates. " % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))