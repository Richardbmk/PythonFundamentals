{x**2 for x in range(10)}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

{char.upper() for char in "SEX0"}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

string = "hello"
{char for char in string if char in "aeiou"}

len({char for char in string if char in "aeiou"})
