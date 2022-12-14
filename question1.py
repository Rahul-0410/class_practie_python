# Find the maximum element present in a list. 
l=list(map(int,input().split(" ")))
largest_num=None
for number in l:
    if largest_num is None or largest_num< number:
        largest_num=number

print(largest_num)
