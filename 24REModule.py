# 345. Introduction to the RE Module

#import regex module
import re

#define out phone number Regex
pattern = re.compile(r"\d{3} \d{3}-\d{4}")

# type(pattern)
# help(patter)

#search a string with our regex
#res = pattern.search("Call me at 415 555-4242!")

res = pattern.search("Call me at 415 555-4242")
res.group() # "415 555-4242"

res = pattern.search("Call me at 415 555-4242 or 485 525-4442")
res.group() # "415 555-4242"

res = pattern.findall("Call me at 415 555-4242 or 485 525-4442")
res #['415 555-4242', '485 525-4442']

re.search(r"\d{3} \d{3}-\d{4}", "Call me at 415 555-4242") # <re.Match object; span=(11, 23), match='415 555-4242'>
re.search(r"\d{3} \d{3}-\d{4}", "Call me at 415 555-4242").group() #'415 555-4242'


# 346. Validating Phone Numbers With Python

def extract_phone(input):
    #phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

#print(extract_phone("my number is 432 324-3245"))
#print(extract_phone("my number is 482 394-304534"))
#print(extract_phone("432 324-3245"))
#print(extract_phone("432 324-3245 sdfesd"))

def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)


#print(extract_all_phones("my number is 432 567-8976 or call me at 345 444-6666"))
#print(extract_all_phones("my number is 432 567-8976 or call me at 345 444-66366"))
#print(extract_all_phones("my number is 432 567-897sd6 or call me at 345 444-66366"))

#def is_valid_phone(input):
#    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
#    match = phone_regex.search(input)
#    if match:
#        return True
#    return False


def is_valid_phone(input):
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

#print(is_valid_phone("436 567-9803"))
#print(is_valid_phone("blue card 43432-23904"))
#print(is_valid_phone("432 098-985"))

#url_regx = re.compile(r"https?://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*")
url_regx = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
#match = url_regx.search("http://www.youtube.com/videos/ssdf/sdf/sdsf")
match = url_regx.search("https://www.my-webasite.com/bio?data=blah&cat=yes")
#print(match.group())
#print(match.groups())
#print(match.group(0))
#print(match.group(1))
#print(match.group(2))
#print(match.group(3))

#print(f"Protocol: {match.group(1)}")
#print(f"Domain: {match.group(2)}")
#print(f"Everything Else: {match.group(3)}")

def parse_name(input):
    #name_regex = re.compile(r"(Mr\.|Mrs\.|Ms\.|Mdame\.) ([A-Za-z]+) ([A-Za-z]+)$")
    name_regex = re.compile(r"(Mr\.|Mrs\.|Ms\.|Mdame\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$")
    matches = name_regex.search(input)
    #print(matches.groups())
    #print(matches.group(2))
    print(matches.group("first"))
    print(matches.group("last"))

#parse_name("Mrs. Tilda Swinton")




