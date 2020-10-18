from bs4 import BeautifulSoup, SoupStrainer
import requests

res = requests.get('https://www.thegoldbugs.com/blog', 'html.parser')

soup = BeautifulSoup(res.text)

blog = soup.select('.sqs-block-content > pre')
# pre doesn't have an ID that I can use so i'm blogbing the pre from inside the sqs-block class.

blog_text = blog[0] # gives me the first element inside the list of pre
string_version = blog_text.contents[0] # gives me a list of the content inside the pre tags ie actual text i want.
# then i can index into it with 0

# All the content has -----hdipiscing infront of every char that i wnt. So i need to split this up

split_content = string_version.split('-----')[1:]
# This creates a list of text that is broken up based on the ---
# and the first one is blank, so i'm slicing from 1 onwards.

result = ''

for sentence in split_content:
    result = result + sentence[0]

print(result)