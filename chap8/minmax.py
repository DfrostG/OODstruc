def min_cost(list, result):
    if len(list) >= 2:
        list.sort()
        new_value = list.pop(0) + list.pop(0)
        list.append(new_value)
        result.append(new_value)
        min_cost(list, result)
    return sum(result)

def max_cost(list, result):
    if len(list) >= 2:
        list.sort()
        new_value = list.pop() + list.pop()
        list.append(new_value)
        result.append(new_value)
        max_cost(list, result)
    return sum(result)

inp = input("Enter Input: ").split()
num_list1 = []
num_list2 = []
for value in inp:
    num_list1.append(int(value))
    num_list2.append(int(value))

print(f"Min cost: {min_cost(num_list1, [])}")
print(f"Max cost: {max_cost(num_list2, [])}")
