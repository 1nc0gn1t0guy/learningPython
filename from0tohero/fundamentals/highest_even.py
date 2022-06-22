def highest_even(li):
    new_list = []

    for item in li:
        if item % 2 == 0:
            new_list.append(item)
    
    return max(new_list)
        
print(highest_even([10,2,3,22,8,11]))