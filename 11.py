p=float(input("enter principle(amount) "))
r=float(input("enter rate of intrest "))
t=float(input("enter time "))
print((p*r*t)/100)
am=p*(1+r/100)**t
ci=am-p
print(ci)
