#!/usr/bin/env python


def do_nothing():
    pass

do_nothing()


def make_a_sound():
    print("quack")

make_a_sound()


def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))


def commentary(color):
    if color == "red":
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)

print(do_nothing())


def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))


def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
# return ['a', 'b']
buggy('b')


def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


def knights(saying):
    def inner(quote):
        return "Wea are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))


# Closure
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
type(a)
type(b)
print(a)
print(b)
print(a())
print(b())


# Lambda function
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, lambda word: word.capitalize() + '!')


# Generater
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
for x in ranger:
    print(x)


# Decolator
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_int(a, b):
    return a + b


cooler_add_ints = document_it(add_int)
cooler_add_ints(3, 5)


@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)


@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)


# Namespace and Scope
animal = 'fruitbat'
print('global:', animal, id(animal))


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))
    print('locals:', locals())

change_local()


def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal, id(animal))
    print('locals:', locals())

change_and_print_global()
print('global:', animal, id(animal))
print('globals', globals())


# Handling exceptions
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)


class UppercaseException(Exception):
    pass

''''
words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
'''

# 4-1 - 4-2
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

# 4-3 - 4-7
for i in [3, 2, 1, 0]:
    print(i)

evens = [int for int in range(10) if int % 2 == 0]
print(evens)

squares = {int: int ** 2 for int in range(10)}
print(squares)

odd = {int for int in range(10) if int % 2 == 1}
print(odd)

my_range = ('Got ' + str(int) for int in range(10))
for s in my_range:
    print(s)


# 4-8
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 4-9
get_odds = (odd for odd in range(10) if odd % 2 == 1)
list2 = []
for i in get_odds:
    list2.append(i)

print(list2[2])


# 4-10
def test(func):
    def tested_func(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return tested_func

test_good = test(good)
test_good()


# 4-11
class OopsException(Exception):
    pass

try:
    oops = 'something is wrong'
    raise OopsException(oops)
except OopsException as err:
    print('Caught an oops:', oops)


# 4-12
titles = [
    'Creature of Habit',
    'Crewel Fate'
    ]
plots = [
    'A nun turns into a monster',
    'A haunted yarn shop'
    ]
print(dict(zip(titles, plots)))
