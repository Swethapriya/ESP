import re


class StringOperator(object):

	def Clean(text):
        # takes tweet(type:str) as input and
        # returns a clean tweet(type:str)
        if(text[0:3].decode("utf-8") == "rt "):
			text = text[3:]
		text = text.decode("utf-8").encode("ascii", errors="ignore").decode()
		text = ' '.join(list(filter(lambda x:x[0]!='@', text.split())))
		text = text.strip("$")
		words = text.split(" ")
		length = len(words)
		for i in range(0,length):
			if(words[i][0:4] == "http"):
				words[i] = "url"
		text = ' '.join(words)
		text = ' '.join(list(filter(lambda x:x[0:3]!='&gt', text.split())))
		text = ' '.join(list(filter(lambda x:x[0:3]!='^^', text.split())))
		return text

	def WordInText(word, text):
        # checks it word(type:str) is a substring of text(type:str)
        # returns(type:str) text is yes else empty string
		word = word.lower()
		text = text.lower()
		text = Clean(text)
		match = re.search(word, text)
		if match:
			return text
		return ""
