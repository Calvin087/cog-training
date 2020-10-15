Executing code on a file as if we're making a function using ```with``` and ```as```. This also automatically CLOSES the file once executed.

with open('test.txt') as my_file:
    print(my_file.read())