user_0 = {
    'username': 'rpadilla',
    'first': 'Rodolfo',
    'last': 'Padilla',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

favorite_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erin': 'java',
}
for name, language in favorite_langs.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

for name in favorite_langs.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_langs.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_langs[name].title() + '!')

    if 'erin' not in favorite_langs.keys():
        print('Erin, please take our poll!')

for name in sorted(favorite_langs.keys()):
    print(name.title() + ", thank you for taking our poll!")

print('The following languages have been mentioned:')
for language in set(favorite_langs.values()):
    print(language.title())
