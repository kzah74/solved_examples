name_prompt = "\nWhat is your name? "
response_prompt = "If you could visit one place in the world, "
response_prompt += "where would you go? "
repeat_prompt = "\nWould you like to let someone else responed? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    response = input(response_prompt)

    responses[name] = response

    repeat = input(repeat_prompt)
    if repeat != 'yes':
        break

print("\n---Results---")
for name, response in responses:
    print(f"{name.title()} would like to visit {response.title()}.")


