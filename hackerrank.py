# Complete the solve function below.
def solve(s):
    list_full_name = s.split()
    list_capitalized_full_name = [name.capitalize() for name in list_full_name]
    return " ".join(list_capitalized_full_name)


# print(solve("richar    castaneda"))
# print(solve("Mario maria"))
# print(solve("laravelo Sturo"))
# print(solve("laravelo Sturo     mare "))
# print(solve("laravelo Sturo  salika"))
# print(solve(" laravelo Sturo salta"))
