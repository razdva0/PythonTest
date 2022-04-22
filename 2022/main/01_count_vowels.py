def count_vowels(string):
    return len([x for x in string.lower() if x in 'aeiou'])


print(count_vowels('abcd'))
