import random
comp = random.randint(1,100)
if comp>= 1 and comp <= 25:
    sym = 'r'
    
elif comp >= 26 and comp <= 75:
    sym = 's'

else:
    sym = 'p'
    
user = input('Put \'p\' for paper \'s\' for scissor and \'r\' for rock: ')
if user == sym:
    print(f'You = {user}, System = {sym}')
    print('It\'s a tie')
else:
    if user == 'p' and sym == 's':
        print(f'You = {user}, System = {sym}')
        print('You Lost')
    elif user == 'p' and sym == 'r':
        print(f'You = {user}, System = {sym}')
        print('You Won')
    elif user == 's' and sym == 'p':
        print(f'You = {user}, System = {sym}')
        print('You Won')
    elif user == 's' and sym == 'r':
        print(f'You = {user}, System = {sym}')
        print('You Lost')
    elif user == 'r' and sym == 's':
        print(f'You = {user}, System = {sym}')
        print('You Won')
    elif user == 'r' and sym == 'p':
        print(f'You = {user}, System = {sym}')
        print('You Lost')
