input_num = int(input("Let's check for what a number is divisble by: "))

input_range = range(1, input_num+1)
divisors = []
for number in input_range:
    if input_num % number == 0:
        divisors += [number]
print(f"Here are the divisors:\n{divisors}\n")
