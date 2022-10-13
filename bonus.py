array = [int(i) for i in input("Enter the array: ").split()] 
delta = int(input("Enter the delta: "))
mmin = array[0]

for i in array:
    mmin = min(i, mmin)
    
cnt = 0

for i in array:
    if mmin + delta == i:
        cnt += 1    
        
print(cnt)
