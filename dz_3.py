boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys) == len(girls):
    new_dating = zip(boys, girls)
    print('Идеальные пары:')
    for perfect_matches in new_dating:
        print(perfect_matches[0], 'и', perfect_matches[1])
else:
    print('Кто-то может остаться без пары!')
