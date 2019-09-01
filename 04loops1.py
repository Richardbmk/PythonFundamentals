# for x in range(1,5):
#     print(x)
#     print(x*x)

# for let in "Love":
#     print(let)

#using range

# range(0,10)
# l = range(10, 2, -1) # imprime de 10 a 2, restando -1 
# list(l) # pone tod la info en una lista. 
#
# for num in range(10):
#     print(num)
#
# for num in range(10, 20, 5):
#     print(num)

#FIRST EXERCISE 1

#Using range steps
x = 0
for oddnum in range(19, 9, -2):
    x += oddnum
    print(x)

x = 0
for i in range(11,21,2):
        x += i
        print(x)
#Using for and if condition
x = 0
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n
        print(x)
