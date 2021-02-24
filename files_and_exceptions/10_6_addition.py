prompt = "Tell me two numbers and I will add them together. Enter 'q' to quit."
prompt += "The first number is: "
prompt_2 = "The second number is: "
first_number = input(prompt)
second_number = input(prompt_2)

while True:
    if first_number == 'q':
        break
    if second_number == 'q':
        break
    else:
        try:
            f_number = int(first_number)
            s_number = int(second_number)
        except ValueError:
            print("You have to enter a number, not a text.")
        else:
            sum = f_number + s_number
            print(f"The sum of {f_number} and {s_number} is {sum}.")

