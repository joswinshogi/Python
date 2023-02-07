L=[1,2,3,4,5,6,7,8,9]
print(L[::-1])
L = [[1,2,3],[0,4,5],[0,0,6]]
for i in range (3):
    for j in range(2,i-1, -1):
        print(L[i][j], end =" ")
n = 10
l = []
for i in range(10, n+10) :
    l.append(i**i)

for i in range (10,0, -1):
    print(l[i])

def add_items(x,y) : 
    x+= [1,2]
    y+= (3,4)
l = [0]
t = (5 ,)
add_items(l, t)
print(l,end="")
print(t)