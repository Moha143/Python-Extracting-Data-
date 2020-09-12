import re
fhandle = open('regex_sum_929690.txt')#returns a handle
content = fhandle.read()
numbers = re.findall('[0-9]+', content)

sum_number = 0
for num in numbers:
    num = int(num)
    sum_number = sum_number+num
print (sum_number)