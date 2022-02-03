def checkvowels(x):
    if (x>='A' and x<='Z') or (x>='a' and x<='z'):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        if c in vowels:
            print('This letter is vowel')
        else:
            print('This letter is not vowel')

print(end='Enter a character')
c = input()
if len(c) > 1 or c.isdigit():
    print('Kindly enter only character')
else:
    checkvowels(c)


