one = ['magical unicorns',19,'hello',98.98,'world']
two = [2,3,1,7,4,12]
three = ['magical','unicorns']
def type_list(list):
    string = ""
    sum = 0
    for x in list:
        if isinstance(x,str):
            string = string+ " " + x
        elif isinstance(x,int) or isinstance(x,float):
            sum += x
    print "string: ", string
    print "sum: ", sum
    if sum !=0 and string > 0:
        print "The list you entered is of mixed type"
    elif sum > 0 and string == 0:
        print "The list you entered is of integer type"
    elif string > 0 and sum == 0:
        print "The list you entered is of string type"

type_list(one)
type_list(two)
type_list(three)
