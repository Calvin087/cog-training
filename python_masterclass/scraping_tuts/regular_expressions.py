import re

string = "call me on the phone at 771-613-2949, phone me early in the morning"

pattern = 'phone'

matched = re.search(pattern, string)
# <re.Match object; span=(15, 20), match='phone'>

print(matched.span())
# (15, 20)
print(matched.start())
# 15
print(matched.end())
# 20
print(re.findall(pattern, string))
# ['phone', 'phone']

for match in re.finditer(pattern, string):
    print(match)
    print(match.group())

    # <re.Match object; span=(15, 20), match='phone'>
    # <re.Match object; span=(38, 43), match='phone'>
    # phone
    # phone

# --------------------------

text_to_search = 'my phone number is 771-613-2949, give me a shot later - 000-613-2949'

phone_pattern = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text_to_search)

print(phone_pattern)
# <re.Match object; span=(19, 31), match='771-613-2949'>

phone_pattern2 = re.search(r'\d{3}-\d{3}-\d{4}', text_to_search)

print(phone_pattern2)
# <re.Match object; span=(19, 31), match='771-613-2949'>

phone_pattern_group = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern_group, text_to_search)

print(f'something new goes here {results.group()}')
# something new goes here 771-613-2949

print(f'something new goes here {results.group(1)}')
# something new goes here 771

# ---------------------------

# OR
search = re.search(r'cat|dog', 'the cat is in the house.')
# cat

# WildCards (.)
# Wildcards grab additional content before the chars i need
# Including spaces, and things i might not want. ie: ...at grabs spaces.
search2 = re.findall(r'.at', 'the cat in the hat sat in the house.')
# ['cat', 'hat', 'sat']

# Starts / ends with.
starts_with = re.findall(r'^\d\d', '12 is a number.')
starts_with2 = re.findall(r'^\d\d', "This doesn't 12 work is a number.")
starts_with3 = re.findall(r'\d\d$', "This doesn't work is a number 30")

print(starts_with)
print(starts_with2)
print(starts_with3)

# ['12']
# [] < --- text to search doesn't START with 12
# ['30']

# ------------------

# Exclusion

phrase = 'There is something 4 inside my 50, dirty washing 2'

exclusion = r'[^\d]'
exclusion2 = r'[^\d]+'
exclusion3 = r'[^!?,. ]+'

print(re.findall(exclusion, phrase))
# ['T', 'h', 'e', 'r', 'e', ' ', 'i', 's', ' ', 's', 'o', 'm', 'e', 't', 'h', 'i', 'n', 'g', ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', 'm', 'y', ' ', ',', ' ', 'd', 'i', 'r', 't', 'y', ' ', 'w', 'a', 's', 'h', 'i', 'n', 'g', ' ']

print(re.findall(exclusion2, phrase))
# ['There is something ', ' inside my ', ', dirty washing ']

remove_puncs = "This, my friend is a sentence. It has loads of !? in it. Right?"

clean = re.findall(exclusion3, remove_puncs)
cleaner = ' '.join(clean)
print(cleaner)

# -------------------

# Inclusion

text_here = 'Only find the hyphen-words in this sentence, but you do not know how long-ish they are'

new_pattern = r'[\w]+-[\w]+'

print(re.findall(new_pattern, text_here))
# ['hyphen-words', 'long-ish']