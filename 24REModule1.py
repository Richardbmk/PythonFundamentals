# 352. Regex Compilation Flags
#pat = re.compile(r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$") # e-mail regex
import re
parttern1 = re.compile(r"""
    ^([a-z0-9_\.-]+) #first part of email
    @                 #single @ sign
    ([\da-z\.-]+)     #email provider
    \.                #single period
    ([a-z\.]{2,6})$   #com, org, net, etc. 
""", re.VERBOSE)

parttern2 = re.compile(r"""
    ^([a-z0-9_\.-]+) #first part of email
    @                 #single @ sign
    ([\da-z\.-]+)     #email provider
    \.                #single period
    ([a-z\.]{2,6})$   #com, org, net, etc. 
""", re.X)

parttern3 = re.compile(r"""
    ^([a-z0-9_\.-]+) #first part of email
    @                 #single @ sign
    ([\da-z\.-]+)     #email provider
    \.                #single period
    ([a-z\.]{2,6})$   #com, org, net, etc. 
""", re.X | re.IGNORECASE)

flow = parttern3.search("Rdobmkk@gmail.com")
#print(flow.group(0))
#print(flow.groups(0))

# 353. Regex Substitution Basics
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

#pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.I)
pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.I)
#print(pattern.findall(text))
#print(pattern.search(text).group())
#result = pattern.sub("REDACTED", text)
result = pattern.sub("\g<1> \g<2>", text)
#print(result) #Last night REDACTED and REDACTED murdered REDACTED



# 355. Swapping File Names


titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

titles.sort()
fixed_titles = []
#print(titles)

#pattern = re.compile(r"(^[\w ]+) \((\d{4})\)")
pattern = re.compile(r"(?P<title>^[\w ]+) \((?P<date>\d{4})\)")

for book in titles:
    #result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)


