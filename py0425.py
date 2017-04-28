#!user/bin/python
#Filename:py0425.py

number=23
running = True



while running:
    guess=int(input("Enter and integet:"))
    if guess==number:
        print('you guessed it.')
        running=False
    elif guess<number:
        print('you guessed small.')
    else:
        print('you guessed large.')
else:
    print('done')



i=5
print(i)
i = i+1
print(i)

s='''This is a muasf string.\
This is second line.'''
print(s)

length = 5
width = 2
area = length*width
print('area is', area)
print('area is \n' + s)

