import os, pickle, random, redis, tweepy 

r = redis.from_url(os.environ.get("REDIS_URL"))

# twitter 
auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), 
                           os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), 
                      os.environ.get("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

#conn = redis.Redis(host='ec2-52-22-113-93.compute-1.amazonaws.com',
#                   port=14719,
#                   password='p5fbb6f2876f58aed4b4718076994ea36966ef20e196a5d968d49f12484456d5f')
#r = redis.from_url('redis://h:p5fbb6f2876f58aed4b4718076994ea36966ef20e196a5d968d49f12484456d5f@ec2-52-22-113-93.compute-1.amazonaws.com:14719')

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
