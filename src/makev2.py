import os

print(os.getcwd())

lines = '\n'.join(open('../data/data_v1.txt', 'r').readlines())

with open('../data/data_v2.txt', 'w') as file:
	file.write(lines)
	file.write("I am v2")



