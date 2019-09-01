#Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][-1]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for l in nested_list:
    for val in l:
        print(val)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for l in nested_list:
    print(l)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in l] for l in nested_list]


board = [[num for num in range(1,4)] for val in range(1,4)]
print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

# LIfe exemple

coord = [[10.34, 2.34], [12.34, 12.45], [10.34, 54.21],  [90.32, 89.0]]

for loc in coord:
    print(loc)


for lo in coord:
    for i in lo:
        print(i)