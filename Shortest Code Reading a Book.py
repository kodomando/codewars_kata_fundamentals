def reverse_words(text):
	split = [words for words in text.split()]
	answer = [rev_[::-1] for rev_ in split]
	return ' '.join(answer)


