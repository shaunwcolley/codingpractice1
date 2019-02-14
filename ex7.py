a = [1,4,9,16,25,36,49,64,81,100]

b = [number for number in a if number % 2 == 0]

#Below is what I wrote before I reduced to a list comprehension
#for number in a:
#    if number % 2 == 0:
#        b += [number]
print(b)
