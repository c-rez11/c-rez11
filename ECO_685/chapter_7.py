print("hello world")
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 309-310-1111 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)
print('done')

import re
PhoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = PhoneNumRegex.search('my number is 111-222-3333')
print('phone number found: ' + mo.group())

PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # adding parenthesis groups chunks of the phone number, as evident in the below print statements
mo = PhoneNumRegex.search('my number is 111-222-3333')
print('phone number found: ' + mo.group(1))
print('phone number found: ' + mo.group(2))
print('phone number found: ' + mo.group(3))

heroRegex = re.compile(r'Batman|Tina Fey') # the 'or' statement. It will match the first result it finds. See example below for how the order of the string affects what is returned
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

heroRegex = re.compile(r'Batman|Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # simplifies the search for things that start with 'Bat'
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

batRegex = re.compile(r'Bat(wo)?man') # optional matching 
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

haRegex = re.compile(r'(ha){3}') #looks for 3 repetitions of 'ha'; returns None if less than 3
mo1 = haRegex.search('hahaha')
mo1.group()

greedyHaRegex = re.compile(r'(Ha){3,5}') # greedy is the default; Python will look for the longest string possible
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') # by adding '?' we make the expression non-greedy, which returns the shortest matching string
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # returns all matches, not just the first one

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups, which affect the findall() by returning tuples
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# For the rest of Chapter 7, refer to the textbook