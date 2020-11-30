def groupAnagrams(words):
    word_dict = {}
	# make a dict to store letter combos
    for word in words:
		letters = list(word)
		letters.sort()
		letters = tuple(letters)
		if letters in word_dict:
			word_dict[letters].append(word)
		else:
			word_dict[letters] = [word]
	# append each combo to output
	output = []
	for key in word_dict:
		output.append(word_dict[key])
	return output
