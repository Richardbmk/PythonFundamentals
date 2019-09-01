print("------- My solution -----------")
msg = input("say something: ")
while msg != "stop":
    print(msg)
    msg = input("say something: ")
print("ok ok, I will stop")

print("------- COLT SOLUTION 1 -----------")

msg = input("say something: ")

while msg != "stop":
    print(msg)
    msg = input()
print("ok ok, I will stop")

print("------- COLT SOLUTION 2 -----------")

msg = input("say something: ")

while msg != "stop":
    msg = input(f"{msg}\n")
print("ok ok, I will stop")
