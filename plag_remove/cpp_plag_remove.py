file = open('cf.cpp', 'r')
out = open('cf_new.cpp', 'w')
string = "int ali=0;"
new_string = "ali =0;"
count = 0
for i in file:
    if i[-1] == '\n':
        i = i[:-1]

    out.write(i)
    try:
        if len(i) == 0:
            pass
        elif not i.startswith(" "):
            pass
        elif not i.startswith("\t"):
            pass
        elif i.endswith(';'):
            if count == 0:
                out.write(string)
                count += 1
            else:
                out.write(new_string)
    except:
        pass
    out.write('\n')
