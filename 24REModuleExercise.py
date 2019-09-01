# Time Validatin EXERCISE!!
import re

def is_valid_time(input):
    time_regex = re.compile(r"((\d{1}|\d{2}):\d{2})\b")
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False


# COLT SOLUTION!!
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

#print(is_valid_time("10:45"))
#print(is_valid_time("1:32"))
#print(is_valid_time("10.45"))
#print(is_valid_time("100:45"))
#print(is_valid_time("10045"))

# Parsing Bytes EXERCISE!!!

def parse_bytes(input):
    binary_regex = re.compile(r"\b[0-1]{8}\b")
    return  binary_regex.findall(input)

# COLT SOLUTION!!
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results

#print(parse_bytes("11010101 101 323"))
#print(parse_bytes("my data is: 10101010 11000100"))
#print(parse_bytes("asdsa"))

# DATE PARSING EXERCISE
def parse_date(input):
    date_regex = re.compile(r"\b([0-9]{2})/([0-9]{2})/([0-9]{4})\b")
    match = date_regex.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

# COLT SOLUTION
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

#print(parse_date("01/22/1999"))
#parse_date("01,22,1999")
#parse_date("01.22.1999")
#parse_date("01/22/10999")

# REGEEX PROFANITY FILTER EXERCISE
#COLT SOLUTION
def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)

print(censor("Frack you"))
#censor("I hope you fracking die")
#censor("You gracking Frack")






