# 5-5
plain = {
    'a': 1,
    'b': 2,
    'c': 3,
    }
print(plain)

# 5-6
from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

fancy = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
    ])
print(fancy)

# 5-7
from collections import defaultdict
dict_of_lists = defaultdict(list)
#dict_of_lists['a'] = ['something for a']
dict_of_lists['a'].append('something for a')
print(dict_of_lists)
