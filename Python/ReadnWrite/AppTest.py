linenum = int(input("type line number: "))

f = open("test.txt")
for x, line in enumerate(f):
    if x ==linenum:
        print(line)
