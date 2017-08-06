def extract_even(l):
    return [number for number in l if number % 2 == 0]

l = [1, 4, 5, -1, 10]
new_list = extract_even(l)
print(new_list)

input()

even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
