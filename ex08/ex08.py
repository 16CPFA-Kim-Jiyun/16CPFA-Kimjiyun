#-*-coding:cp949
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
                   "That you could type up right.",
                   "But it didn't sing.",
                   # 문장안에 작은 따음표가 있어서 큰따음표로 출력됨
                   "So I said goodnight.")

