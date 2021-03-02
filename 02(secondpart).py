# vowels = ['a','e','i','o','u']
# word = input("Provide a word to search for vowels: ")

# found = {}

# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter, 0) # setdefault 를 사용하면 key error 예외를 방지한다.
#         found[letter] += 1

# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'tiems(s). ')


########################################################


# vowels = set('aeiou')
# word = input("Provie a word to search for vowels: ")
# found = vowels.intersection(set(word))
# for vowel in found:
#     print(vowel)

########################################################

def search4vowels(): 
    """ Display any vowels found in an asked-for word"""
    vowels = set('aeiou')
    word = input("Provie a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()

