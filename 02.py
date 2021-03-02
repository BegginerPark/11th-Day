############################## Review start #######################
# import found
# vowels = ['a','e','i','o','u']

# word = "Milliways"

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)

# for vowels in found:
#     print(vowels)

############################### Review end ########################

# nums = [1,2,3,4]
# nums
# nums.remove(3)   # 3을 제거
# nums
# nums.pop() # 끝의 하나를 날린다.(주로 사용한다.)
# nums
# nums.(0)
# nums
# nums = [2]
# nums.extend([3,4]) # 리스트 안에 추가 하기
# nums
# nums.insert(0,1) # 0번째에 1을 추가 하여라.
# nums 
# nums.insert(2,'two-and-a-half') # 글자도 추가 가능하다.
# nums

#############################################################

# phrase = "Don't panic!"
# plist = list(phrase) # 리스트로 만들어 준다.
# phrase
# plist

# for i in range(0,4): # 4번 반복
#     plist.pop()   # 뒤에서 부터 하나씩 제거

# plist.pop(0) # 0번째 리스트 제거
# plist.remove("'") # ' 을 제거 
# plist

#############################################################

# first = [1,2,3,4,5]
# first

# second = first # second 는 first 와 같다.
# second

# second.append(6) # second 에 6을 추가 하여면 first 에서 추가가 되니 조심하여야 한다.
# second
# first

# third = second.copy() # third 를 second 의 카피로 하게 되면은 
# third
# third.append(7) # third 에 추가를 하여도 second 에 추가가 되지 않는다.
# third
# second

#############################################################

# saying = "Don't panic!"
# letters = list(saying)

# letters
# letters[0]
# letters[-1]

#############################################################

# vowels = ['a','e','i','o','u']

# word = input("Provide a word to serch for vowels: ")
# found = []

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)

# for vowels in found:
#     print(vowels)


# found = {}
# found


# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0 
# found['u'] = 0
# found


# found['e'] = found['e'] + 1
# found
# found['e'] += 1  # 위의 함수와 같은 의미이다.
# found

# for k in sorted(found):
#     print(k, 'was found', found[k], 'times(s).') # 몇번 찾았는지 확인 하라.

# for k, v in sorted(found.itmes()):
#     print(k, 'was found', v, 'times(s).')

#############################################################

vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")

found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0 
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'tiems(s). ')

#############################################################


