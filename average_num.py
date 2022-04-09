import time as t
import random as r
import matplotlib.pyplot as plt

SAS = 1000
# mid = 0
numbers_range_1 = []
numbers_range_2 = []

avg_total_1 = [0] * SAS
avg_total_2 = [0] * SAS
source = []

for i in range(SAS):
    num = r.randint(1, 10)
    vbros = r.randint(10, 100)
    if (i != 0 and i % 20 == 0):
        num = vbros
    source.append(num)

    if len(numbers_range_1) > 50:
        numbers_range_1.pop(0)
    numbers_range_1.append(num)
    avg_total_1[i] = sum(numbers_range_1)/len(numbers_range_1)

    if len(numbers_range_2) > 100:
        numbers_range_2.pop(0)
    numbers_range_2.append(num)
    avg_total_2[i] = sum(numbers_range_2)/len(numbers_range_2)

    # print(f'Число: {num} || i = {i} || mid = {avg_total_1[i]}')
    # plt.show()
    # t.sleep(1)

# x axis values
# x = [1,2,3,4,5,6]
# corresponding y axis values
# y = [2,4,1,5,2,6]
# height = [1, 24, 36, 40, 5]
# plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)

# plt.plot(left, avg_total_1, width = 0.8, color = ['blue'], marker = "o")
# plt.plot(range(len(source)), source, width = 0.8, color = ['red'], marker = )

plt.plot(range(len(source)), source, color='red', marker='o', markerfacecolor='red', markersize=1, linewidth = 1)
plt.plot(range(len(avg_total_1)), avg_total_1, color='blue', marker='o', markerfacecolor='blue', markersize=1)
plt.plot(range(len(avg_total_2)), avg_total_2, color='green', marker='o', markerfacecolor='blue', markersize=1)

plt.show()