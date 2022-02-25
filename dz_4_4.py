stats = {'facebook': 55, 'yandex': 120, 'vk': 115,
         'google': 99, 'email': 42, 'ok': 98}
max_chan = ''
for chan in stats.keys():
    if stats[chan] > stats.get(max_chan, 0):
        max_chan = chan
print(max_chan)
