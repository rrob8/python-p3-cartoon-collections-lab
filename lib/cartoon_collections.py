def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf)+1}. {dwarf}')

def summon_captain_planet(planeteers):
    calls = []
    for element in planeteers:
        calls.append(f"{element.capitalize()}!")
    return calls

def long_planeteer_calls(list):
    value = ''
    for word in list:
        if len(word) > 4:
            value = True
            break
        else:
            value = False

    return value

def find_the_cheese(strings):
    for item in strings:
        if item == 'gouda' or item ==  'cheddar' or  item == 'camembert':
            return item
