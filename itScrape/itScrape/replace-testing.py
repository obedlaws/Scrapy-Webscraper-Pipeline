
# Testing to see how to replace and manage the date string so
# Postgresql can identify dates and data in the dabase
# is a lot more cleaner. (Basicly just trying to insert date at
# beginning of the string so it follows the format of Postgresql)

date = "01-11-2020"
l_date = ['01-11-2020', '03-12-2020', '02-01-2020', '03-24-2020']


#print(date[-4:])
#print(date[:5])

#add = date[-4:]
#psqldate = date[:5]
#formatted = add + '-' + psqldate

#print(formatted)

test = "01-11-2020"
test2 = " (01-11-2020)"

def change(string):
    new = []
    for s in l_date:
        y = s[-4:]
        d = s[:5]
        f = y + '-' + d
        new.append(f)

    print(new)

#test 1 // SSHOULD USE THIS FUNCTION
def arrange(value):
    string = value

    y = string[-4:]
    d = string[:5]
    string = y + '-' + d
    return string

#test 2 // FAILED
def date_extra(value):
    return value.replace('(','').replace(')','').replace('/','-').replace(' ','')

def arrange2(value):
    string = value

    y = string[-4:]
    d = string[:5]
    string = y + '-' + d
    print(string)

#hange(l_date)
print(arrange(test))
#date_extra(test2)
#arrange2(test2)
