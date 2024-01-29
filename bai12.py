prev_list = [1,2,3]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)
    new_list = [i * 2 for i in prev_list]
print(new_list)