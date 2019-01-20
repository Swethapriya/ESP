#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "2354690352-tEK26HCzhIutNTc88m2QZ2PIFkylIxxhvi7oEDi"
access_token_secret = "Dubgmq88BUj0yhmRhirOChG0hY5qgNR8YMcxBaWnXi9TY"
consumer_key = "ixSJS9ZdWg557X61nCo3LBI0X"
consumer_secret = "W7qOlh1OBqd7kA4bZFRM5ZlgWTYV2gTDDuJWQdGNhO1nrDbO2r"

F = open("path to tweets base","a")

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        F.write(data)
        return True

    def on_error(self, status):
        F.close()
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#sad', '#angry', '#disgust', '#surprise', '#fear'])
