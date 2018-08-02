"'Taking an input'"
V = input()
VOWELS = 0
for char in V:
    if char in 'aeiou':
        VOWELS = VOWELS+1
print(VOWELS)
