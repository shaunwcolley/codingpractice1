a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
num = int(input("This is a hold up, give me a number!\n>> "))
for number in a:
    if number < num:
        b += [number]
print(f"\nTurns, out this wasn't a hold up, but these are the numbers less than {num} in my list:\n\n{b}\n")

#One line of code to do the same as above, referred to as list comprehension
#b = [number for number in a if number < 5]
#print(b)
