import random
import sys

for i in range(5):
    print(random.randint(1, 10))

while True:
    print('Type exit to Exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
