import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
import operator


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from StringManipulation import  string_operations


class Train(object,filepath):
	"""docstring for Train."""
	def __init__(self):
		self.EMOTIONAL_SETS = {'happy': {}, 'sad': {}, 'angry': {}, 'fear': {}, 'surprize': {}, 'disgust': {}}

	def Train(self):
		tweets = open('path to tweetsdb','r')
		for line in tweets:
		    try:
				string_operator = StringOperator()
		        tweet = json.loads(line)
		        clean_tweet = tweet['text'].encode("utf-8)
				for emotion in self.EMOTIONAL_SETS.keys():
					emotional_tweet = string_operator.WordInText(emotion,clean_tweet)
		        	if(emotional_tweet != ''):
						if(emotional_tweet.count("#"+emotion)==0):
							continue
						try:
							tokens = nltk.word_tokenize(emotional_tweet)
							tags = nltk.pos_tag(tokens)

							for tag in tags:
								if(re.match('^[\w]+$', tag[0]) is not None and ("_" not in tag[0])):
									if(tag[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
										word = tag[0]
										if(tag in self.EMOTIONAL_SETS[emotion].keys()):
											self.EMOTIONAL_SETS[emotion][word] += 1
										else:
											self.EMOTIONAL_SETS[emotion][word] = 1
						except:
							continue
		    except:
		        continue

		tweets.close()
		return self.EMOTIONAL_SETS

'''
reads from the tweets database and segregates the tweets based on hashtags into
resptive emotion sets.
'''
if __name__ == '__main__':
	modal = Train().Train('path to tweets')
	print(modal)
