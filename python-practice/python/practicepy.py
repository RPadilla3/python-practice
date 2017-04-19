import sys
print(sys.executable)
print(sys.version)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('\nOriginal x-position: ' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print('\nNew x-position: ' + str(alien_0['x_position']))

favorite_langs = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'javascript',
    'nicolas': 'perl',
}

print("\nSarah's favorite language is " +
      favorite_langs['sarah'].title() +
      '!')

friend_id = {
    'first_name': 'rodolfo',
    'last_name': 'padilla',
    'ethnicity': 'hispanic',
    'age': 21,
}

print(friend_id['first_name'].title())
print(friend_id['last_name'].title())
print(friend_id['ethnicity'].title())
print(friend_id['age'])

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
