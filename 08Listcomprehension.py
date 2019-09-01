nums = [1, 2, 3]
[x*10 for x in nums]

name = "colt"
[char.upper() for char in name]

friends = ["ashley", "matt", "michael"]
[friend[0].upper() for friend in friends]
[friend[0].upper()+friend[1:] for friend in friends]

[num*10 for num in range(1,6)]
[bool(val) for val in [0, [], ""]]

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)
string_list1 = [str(num)+"Hello" for num in nums]
print(string_list1)

numbersf = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbersf if num % 2 == 0]
odds = [num for num in numbersf if num % 2 != 0]
[num*2 if num % 2 == 0 else num/2 for num in numbersf]

with_vowels = "This is so much fun!"
"".join(char for char in with_vowels if char not in "aeiou")
