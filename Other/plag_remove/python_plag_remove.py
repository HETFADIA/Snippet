file = open('target.py', 'r')
out = open('new_file.py', 'w')
string = "ali=0"
for i in file:
    i = i[:-1]

    out.write(i)
    try:
        if len(i) == 0:
            pass
        elif i.endswith(','):
            pass
        elif i.endswith(':'):
            pass
        else:
            out.write(';'+string)
    except:
        pass
    out.write('\n')
