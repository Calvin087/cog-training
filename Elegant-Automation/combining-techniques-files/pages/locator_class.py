from collections import namedtuple

# Why a whole file is necessary to achieve visually appealing code
# I'm not sure.
# Does it make it more functional / reusable?

Locator = namedtuple('Locator', ['by', 'value'])