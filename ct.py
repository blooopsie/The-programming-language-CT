def firstdigit(x):
    for t in x:
        if t.isdigit():
            return t
def ct(d, cmd):
    if cmd == ";":
        return d.replace(firstdigit(d), " ", 1)
    elif cmd.isdigit() and firstdigit(d) == "1":
        return d + cmd
    else:
        return d
d = input("Data-string: ")
p = input("Program: ")
t = 0
while d != "" and d != " ":
    print(d := ct(d, p[t % len(p)]))
    t += 1
