# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


first_song = my_favorite_songs [:my_favorite_songs.find(',')]

last_song = my_favorite_songs [my_favorite_songs.find('N'):]

second_song = my_favorite_songs[my_favorite_songs.find('S'):
my_favorite_songs.find(', A')]

secondend_song = my_favorite_songs [my_favorite_songs.find('Star'):
my_favorite_songs.find(', N')]


print(first_song,'\n', last_song,'\n',  second_song,'\n', secondend_song)

