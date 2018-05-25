#!/usr/bin/python
def fibon(inp):
        summ=0
        v1=0
        v2=1
        print v1,v2,
        while summ<(inp-2):
                val=v1+v2
                v1=v2
                v2=val
                print val,
                summ=summ+1
        print
inp=input("Enter the input from the user :")
fibon(inp)

#!/usr/bin/python
def fib_li(inp):
        v1=0
        v2=1
        summ=0
        l=[v1,v2]
        while (summ<inp-2):
                val=v1+v2
                l.append(val)
                v1=v2
                v2=val
                summ+=1
        return l


#!/usr/bin/python
def fib_tu(inp):
        v1=0
        v2=1
        summ=0
        l=[v1,v2]
        while (summ<inp-2):
                val=v1+v2
                l.append(val)
                v1=v2
                v2=val
                summ+=1
        return tuple(l)


if __name__=="__main___":
	print "main...."
	fibon(10)


