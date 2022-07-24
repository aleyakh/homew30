nums = [1, 2, 3, 4, 5]
nums.insert(3, 'f')
print(nums)

first = [1, 2, 3, 4, 5]
second = first
second.append(6)

print(first[-1])

list_for_slise = "Don't panic!"
list_for_slise = list(list_for_slise)
#print(list_for_slise[0:4:1])

#print(list_for_slise[:5])
#print(''.join(list_for_slise[-6:]))

new_list = ''.join(list_for_slise[1:3]) + ''.join([list_for_slise[5], list_for_slise[4], list_for_slise[7], list_for_slise[6]])
print(new_list)