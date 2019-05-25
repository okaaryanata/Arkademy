def count_vowels(data):
    lowerString = data.lower()
    vowels = ['a','i','u','e','o']
    counter = 0
    for x in lowerString:
        if x in vowels:
            counter += 1
    return counter

print(count_vowels('RobErT'))