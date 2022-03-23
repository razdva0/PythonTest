def alphabet_position(text):
	result = ""
	text = text.upper()
	for x in text:
		if x == ' ':
			continue
		if len(result) > 0:
			result += ' '
		if x.isalpha():
			result += str(ord(x) - 64)
	return result


print(alphabet_position("lol aye"))
