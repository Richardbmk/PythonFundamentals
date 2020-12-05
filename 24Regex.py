# 341. Regex Basics: Quantifiers


k\w+ 

\w{5}

\w{5,7}

\w{3,}

ab*c*d

\d{3} \d{3}-?\d{4}

[aeiou]
[aeiou]{2}
[a-z]
[a-z]{2,}
[^0-9aeiou @]

^\d{3} \d{3}-?\d{4}


^\d{3} \d{3}-?\d{4}$

\b\w+\b

(\(\d{3}\)|\d{3}) \d{3} \d{4}

(Mr\.|Mrs\.) ([A-Za-z]+ [A-Za-z]+)
(Mr\.|Mrs\.) ([A-Za-z]+) ([A-Za-z]+)

https?://[A-Za-z_-]+\.[A-Za-z]+
(https?://)([A-Za-z_-]+\.[A-Za-z]+)



"""
hello worl aaabbbbcccccdddeeef ffggg
Ilike dogs and kittens :) :)
PURPLE 415 412-9876
kitty@gmail.com
310 467-9876
She is 49 years old. I am 75 years old. He is 3 3.
podfspdfkspdf415 412-9876sdlfjsldflskf
423 234 2345
(423) 234 2345
Mr. Luca Guadangino
Mrs. Tilda Swinton
https://pythex.org
http://google.com
"""


# 354. Regex Profanity Filter

import re
 
def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)