# Find the maximum element present in a list. 
l=list(map(int,input().split(" ")))
min_num=min(l)
count=l.count(min)
for i in range(count):
    l.remove(min_num)
print(max(l))
