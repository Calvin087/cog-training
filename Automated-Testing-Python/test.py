my_string = 'Secret agents are super good at staying hidden'

for word in my_string.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

# >> Secret
# >> super
# >> staying

code = [x[0] for x in my_string.split()]

print(code)

# >> ['S', 'a', 'a', 's', 'g', 'a', 's', 'h']