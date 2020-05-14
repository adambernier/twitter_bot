import os, pickle, random, redis, tweepy 

r = redis.from_url(os.environ.get("REDIS_URL"))

# twitter 
auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), 
                           os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), 
                      os.environ.get("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

chain = pickle.loads(r.get('chain'))

new_review = []
sword1 = "BEGIN"
sword2 = "RIGHT"
sword3 = "MEOW"
  
while True:
    sword1, sword2, sword3 = sword2, sword3, random.choice(chain[(sword1, sword2, sword3)])
    if sword3 == "END":
        break
    new_review.append(sword3)
  
print(' '.join(new_review))
api.update_status(' '.join(new_review))
