result = []
my_file = open('test.txt','r')
contents = my_file.readlines()
my_file.close()
for i in contents:
    print(i.split(',').split(' ').split('[').split(']'))
    result.append(i)
print(result)
