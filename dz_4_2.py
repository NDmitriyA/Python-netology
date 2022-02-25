ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
cop_ids = set()
for vol in ids.values():
    for v in vol:
        cop_ids.add(v)
print(list(cop_ids))
