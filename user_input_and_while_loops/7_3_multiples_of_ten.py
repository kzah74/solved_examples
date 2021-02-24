prompt = "Tell me a number and I will tell you if the number is "
prompt += "multiple of 10 or not: "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("The number is multiple of 10.")
else:
    print("The number is not multiple of 10.")