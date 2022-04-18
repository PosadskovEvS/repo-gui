'''#task1
out_f = open('out_file.txt', 'w')
while True:
    str = input('Введите строку: ')
    if str == '':
        break
    else:
        out_f.write(str)
out_f.close()
out_f = open('out_file.txt')
for line in out_f:
    print(line)
out_f.close()
'''

'''#task2
with open(r'task2.txt', 'r') as test_f:
    content = test_f.readlines()
count = 0
text_info = list()
for line in content:
    text_info.append(len(line))
    count += 1

for i in range(count):
    print(f'Длина строки {i+1}: {text_info[i]}')
print(f'Кол-во строк: {count}')
'''
'''#task3

with open('task3.txt', 'r', encoding='utf-8') as test_f:
    content = test_f.readlines()
for i in range(len(content)):
    content[i] = content[i].split()
sum = 0
for line in content:
    sum += int(line[1])
    if int(line[1]) < 20000:
        print(line)
print(f'Средняя з/п: {sum/len(content)}')
'''

'''#task4

from textblob import TextBlob

with open('task4.txt', 'r', encoding='utf-8') as test_f:
    content = test_f.readlines()
for i in range(len(content)):
    content[i] = content[i].split()
    content[i][0] = str(TextBlob(content[i][0]).translate(to='ru'))

with open('task4_result.txt', 'w', encoding='utf-8') as result_f:
    for line in content:
        result_f.write(str(line[0])+' '+str(line[1])+' '+str(line[2])+'\n')
'''
'''#task5

with open('task5.txt', 'w', encoding='utf-8') as result_f:
    for i in range(10):
        result_f.write(str(i+1)+' ')

with open('task5.txt', 'r', encoding='utf-8') as result_f:
    content = result_f.readline()
result = content.split()
sum = 0
for line in result:
    sum += int(line)
print(sum)
'''
'''
#task6

with open('task6.txt', 'r', encoding='utf-8') as result_f:
    content = result_f.readlines()
my_discipline = dict()
for i in range(len(content)):
    content[i] = content[i].replace(':', '')
    content[i] = content[i].replace('(л)', '')
    content[i] = content[i].replace('(пр)', '')
    content[i] = content[i].replace('(лаб)', '')
    content[i] = content[i].split()
    sum = 0
    for j in range(1, len(content[i]), 1):
        sum += int(content[i][j])
    my_discipline[content[i][0]] = sum
print(my_discipline)
'''

#task7

import json

with open('task7.txt', 'r', encoding='utf-8') as result_f:
    content = result_f.readlines()
my_result = dict()
for i in range(len(content)):
    content[i] = content[i].split()
    my_result[content[i][0]] = int(content[i][2]) - int(content[i][3])

avg_list = [line for line in list(my_result.values()) if line >= 0]
my_result['average_profit'] = sum(avg_list)/len(avg_list)
print(my_result)

with open('task7.json', 'w') as write_f:
    json.dump(my_result, write_f)




