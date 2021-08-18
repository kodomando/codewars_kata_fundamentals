song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
songz = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
songz2 = 'AWUBBWUBC'
songz3 = 'AWUBWUBWUBBWUBWUBWUBC'
songz4 = 'WUBAWUBBWUBCWUB'
song_list = ['song', 'songz', 'songz2', 'songz3', 'songz4']

def song_decoder(song):
	song = song.split('WUB')
	result = []

	for chars in song:
		if chars != '':
			result += [chars]

	print( ' '.join(result))

for stuff in song_list:
	song_decoder(eval(stuff))


# def song_decoder(song):
#     song = song.split('WUB')
#     print(song)
#     original_song = []
#     for i in song:
#         if i != '':
#             original_song += [i]
#     return ' '.join(original_song)
#
#
# print(song_decoder(song))

# def song_decoder(song):
# 	song = song.replace('WUB', ' ')
# 	print(song)
# 	song = song.split()
# 	print(song)
# 	print(' '.join(song))
#
#
# song_decoder(songz4)


# def song_decoder(song):
# 	answer = None
# 	words = song.replace('WUB', ' ')
# 	words = words.strip()
# 	length = len(words)
# 	print(words)
# 	print('length:' ,length)
#
# 	count = 0
# 	for i, string in enumerate(words):
# 		if string == ' ':
# 			count += 1
# 			if count == 2:
# 				print(words[i])
# 				words.replace(words[i], '')
# 				count = 0
#
#
# 	print(words)
	# return words



# song_decoder(songz2)
# song_decoder(songz3)
# song_decoder(songz4)







# def song_decoder(song):
#     answer = None
#     words = song.replace('WUB', ' ')
#     words = words.strip(' ')
#     length = len(words)
#
#     j = 0
#     if length % 3 == 0:
#         j = -1
#     if length % 3 != 0:
#         j = length - 1
#
#     for i, string in enumerate(words[:j]):
#         if words[i] + words[i + 1] == '  ' or words[i] + words[i - 1] == '  ':
#              answer = words.replace('  ', ' ')
#
#     return answer


# for i, string in enumerate(words[:]):
# 	# if words[i - 1] == None:
# 	# 	answer = words
# 	if words[i] + words[i - 1] == '  ':
# 		answer = words.replace('  ', ' ')
# 	else:
# 		answer = words
