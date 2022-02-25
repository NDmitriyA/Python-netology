queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
word_count = {}
for q in queries:
    l = len(q.split(' '))
    word_count[l] = word_count.get(l, -1)+1
word_count = {
    f'{k} words in line': f'{v/sum(word_count.values()):.2%}' for k, v in word_count.items()}
print(word_count)
