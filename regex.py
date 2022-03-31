import re

'''
REGEX FUNCTIONS:
match  -> match the pattern only if it is  in the beginning of the line
search -> match the pattern if presents anywhere in the string but it will match only one matches
findall ->match the pattern if presents anywhere and matches all the matched pattern

compile-finditer
'''
mystr="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

~!@#$%^&*(()_+


https://www.amazon.com
http://www.flipkart.com
https://amazon.com
https://www.snaptool.co.us

893-321-3213
434 434 4323
544.654.6454
423_745_6352

Ha HaHa

rohit_tech@gmail.com
rohit.tech@gmail.com
rohit.tech@yagoo.co.in
+91-9898837399
9898837399


"""

#pattern=re.compile(r'https?://(w{3}\.)?\w+\.com?(\.us)?')
#pattern=re.compile(r'\d{3}[\-\s\.]\d{3}[\-\s\.]\d{4}')
#pattern=re.compile(r'\bHa\b')
#pattern=re.compile(r'(\w+)?\.?\w+@\w+\.com?(\.in)?')
pattern=re.compile(r'(\+91\-)?[9]\d{9}')
matches=pattern.finditer(mystr)
for match in matches:
    print(match.group())


# data="pet:cat I love cat pet:dog i love dog"
#
# #res=re.match('pet:dog',data)
# #res=re.search('pet:...',data)
# res=re.findall('pet:...',data)
# print(res)