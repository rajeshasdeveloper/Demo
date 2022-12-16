from copy import deepcopy
parent_list = ["name", "age", "is_student", "is_master", ['masters']]

list_alpha = deepcopy(parent_list)

parent_list[1] = 32
parent_list[-1][0] = 'bachelors'

print('parent list', parent_list)
print('list alpha', list_alpha)
