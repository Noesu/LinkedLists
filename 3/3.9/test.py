def modify_list(lst):
    lst.append(4)
    lst = lst + [5]
    return lst

my_list = [1, 2, 3]
new_list = modify_list(my_list)
print(my_list)
print(new_list)