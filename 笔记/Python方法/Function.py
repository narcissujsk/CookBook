#test globals() and locals()

z=0
def f():
    z = 1
    print (locals())
    locals()["z"] = 2
    print (locals())
f()
globals()["z"] = 2
print (z)
print (globals())