cubes = list(range(1, 11))
print(cubes)
for value in range (1, 11):
	print(value**3)

cubes = []
for number in range (1, 11):
	cube = number**3
	cubes.append(cube)
for cube in cubes:
	print(cube)