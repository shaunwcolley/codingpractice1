a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,89,55,25,103]
c = []

for number in a:
    if number == number in b:
        #The following line of code prevents duplicates!
        if number not in c:
            c += [number]
print(c)
