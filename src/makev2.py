import os

print(os.getcwd())

with open('../data/data_v2.txt', 'w') as file:
	file.write("I am v2")



