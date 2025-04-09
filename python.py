# input admission
i=int(input("Enter you Age"))
n=str(input("Enter you Name"))
fn=str(input("Enter you Father Name"))
mn=str(input("Enter you Mother Name"))
p=str(input("Enter you Place"))
r=str(input("Enter you Religion"))
add=str(input("Enter you Address"))

limit=5

if i >= 5:
    print( f"{n}{fn}{mn}{p}{r}{add} is capable to P.G & Admission")
elif i >= limit:
    print(f"{n}{fn}{mn}{p}{r}{add} is capable to P.G")
else:
    print(f"{n}{fn}{mn}{p}{r}{add}is not capable to Admission")