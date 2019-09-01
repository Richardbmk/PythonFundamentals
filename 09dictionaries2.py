#Exercise
print("-------- My Solution -----------")

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for v in donations.values():
    total_donations += v
    print(total_donations)

print("-------- COLT SOLUTION 1 -----------")

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for donation in donations.values():
 total_donations += donation

print("-------- COLT SOLUTION 2 -----------")

total_donations = sum(donation for donation in donations.values())

print("-------- COLT SOLUTION 3 -----------")

total_donations = sum(donations.values())
