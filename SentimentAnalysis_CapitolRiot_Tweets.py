from textblob import TextBlob
consumer_key="gLqBkck5oG3FZkpS0pV7ghrRI"
consumer_secret="dhEXW1WAWoTLyU2AB9vaD09fFt7cAysETFUKuX25rnBG9XMXyD"

access_token="1349743868993032195-X8p4u2VLEgoaXVajDlPQcFSyeBgFgP"
access_token_secret=""

def get_result(annotations):
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
    return sentence_sentiment

def analyze_sentiment(tweet):
    client = language.LanguageServiceClient()
    document = language.types.Document(content=tweet,type=enums.Document.Type.PLAIN_TEXT)
    annotation = client.analyze_sentiment(document=document)
    result = get_result(annotation)
    return result

def get_tweets(api, keyword):	
    with open('tweets_sentiment.json', 'a') as f:
        for tweet in Cursor(api.search, q=keyword, lang='en').items():
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                sent = analyze_sentiment(tweet.text)
                sent2 = TextBlob(tweet.text).sentiment.polarity
                dic={'text': tweet.text, 'created_at': str(tweet.created_at), 'lang':tweet.lang, 'screen_name':tweet.user.screen_name, 'retweets': tweet.retweet_count, 'coordinates':tweet.coordinates, 'favorite_count':tweet.favorite_count, 'sentimentAPI':sent, 'sentimentTextBlob':sent2}
                json.dump(dic, f)
                f.write('\n')
    return True

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    get_tweets(api, 'CapitolRiot')
