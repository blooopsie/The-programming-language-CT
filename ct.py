def firstdigit(x):
    for t in x:
        if t.isdigit():
            return t
def ct(d, cmd):
    if cmd == ";":
        return d.replace(firstdigit(d), " ", 1)
    elif cmd.isdigit() and d[0] == "1":
        return d + cmd
    else:
        pass
d = input("Data-string: ")
p = input("Program: ")
t = 0
while d != "":
    print(d := ct(d, p[t]))
    t += 1
    if t == len(p):
        t = 0
'''
Note: It has some errors.
Error:
ERROR!
Traceback (most recent call last):
  File \"<main.py>\", line 16, in <module>
  File \"<main.py>\", line 7, in ct
AttributeError: 'NoneType' object has no attribute 'replace'
'''
