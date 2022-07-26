import tweepy

from app import db
from app.models import Podcaster
from app.podcast.tomedia import giftSpeaking, translate_text,generateAudio, generateNewAudiogram
from app.podcast.animatext import generate_animator

api_key = 'kt59fV1XXOQQyBqkcTC74n8xD'
api_secret = 'FxCw8C7P2ZmFPDJQS5mPqrB5Z5iHSKOaNjURJGV0vBKKXdFEUu'

access_key = '1344699439122952192-9pvZcQFBHEkKrx9pJuaEa0wTIHJNcp'
access_secret = '09yonlWqcgUGywg2oSfZT9pAMPMPsw87A7em8OGraZtre'
bearer = 'AAAAAAAAAAAAAAAAAAAAAObVbwEAAAAA2KHfEgRt8ukB8VYQbPTLD64sg2U%3Do44bNlL2hhTIAXn1q5lheQCDkDCYu1Jv83W9fX8Rgpcm4tT0Zs'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True) 

# Unroll Thread
def unroll_thread(tweetId):
    thread = []
    hasReply = True
    res = api.get_status(tweetId, tweet_mode='extended')
    allTillThread = get_all_tweets(res)
    thread.append(res)
    if allTillThread[-1] > res.id:
        print("Not able to retrieve so older tweets")
        return thread
    print("downloaded required tweets")
    startIndex = allTillThread.index(res.id)
    print("Finding useful tweets")
    quietLong = 0
    while startIndex!=0 and quietLong<20:
        nowIndex = startIndex-1
        nowTweet = api.get_status(allTillThread[nowIndex], tweet_mode='extended')
        if nowTweet.in_reply_to_status_id == thread[-1].id:
            quietLong = 0
            print("Reached a useful tweet to be included in thread")
            # screenshootTweet(nowTweet.in_reply_to_status_id)
            thread.append(nowTweet)
        else:
            quietLong = quietLong + 1
        startIndex = nowIndex
    return thread

def getAllTweetsInThreadAfterThis(tweetId):
    thread = []
    hasReply = True
    res = api.get_status(tweetId, tweet_mode='extended')
    allTillThread = get_all_tweets(res)
    thread.append(res)
    if allTillThread[-1] > res.id:
        print("Not able to retrieve so older tweets")
        return thread
    print("downloaded required tweets")
    startIndex = allTillThread.index(res.id)
    print("Finding useful tweets")
    quietLong = 0
    while startIndex!=0 and quietLong<20:
        nowIndex = startIndex-1
        nowTweet = api.get_status(allTillThread[nowIndex], tweet_mode='extended')
        if nowTweet.in_reply_to_status_id == thread[-1].id:
            quietLong = 0
            print("Reached a useful tweet to be included in thread")
            # screenshootTweet(nowTweet.in_reply_to_status_id)
            thread.append(nowTweet)
        else:
            quietLong = quietLong + 1
        startIndex = nowIndex
    return thread

def getAllTweetsInThreadBeforeThis(tweetId):
    thread = []
    hasReply = True
    res = api.get_status(tweetId, tweet_mode='extended')
    while res.in_reply_to_status_id is not None:
        res = api.get_status(res.in_reply_to_status_id, tweet_mode='extended')
        thread.append(res)
    return thread[::-1]

def getAllTweetsInThread(tweetId):
    tweetsAll = []
    print("Getting all tweets before this tweet")
    tweetsAll = getAllTweetsInThreadBeforeThis(tweetId)
    print(len(tweetsAll))
    print("Getting all tweets after this tweet")
    tweetsAll.extend(getAllTweetsInThreadAfterThis(tweetId))
    return tweetsAll

def threadIds(thread):
    ids = []
    for tweetId in range(len(thread)):
        ids.append(thread[tweetId].id_str) 
    return ids

def threadText(thread):
    text = []
    for tweetId in range(len(thread)):
        text.append(thread[tweetId].full_text ) 
    return text

def get_all_tweets(tweet):
    screen_name = tweet.user.screen_name
    lastTweetId = tweet.id
    #initialize a list to hold all the tweepy Tweets
    allTweets = []
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    allTweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = allTweets[-1].id - 1
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0 and oldest >= lastTweetId:
        print(f"getting tweets before {oldest}")
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        #save most recent tweets
        allTweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest =allTweets[-1].id - 1
        print(f"...{len(allTweets)} tweets downloaded so far")
    outtweets = [tweet.id for tweet in allTweets]
    return outtweets


def podcast_generator(link, language= '', voice=''):
    language='en'
    # /^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)$/
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',link,language, voice)
    # global tweet
    tweetId = link.split('/')[-1]
    thread = unroll_thread(tweetId)
    ids = threadIds(thread)
    text = threadText(thread) 
    translated = translate_text(text, language)
    tweetId ='synthentic_test'
    podcast = generateAudio(tweetId, translated, voice, language)

    player = Podcaster(
            user_id=12,
            code= tweetId,
            language=language,
            speaker=voice,
            content=translated,
            podcast = podcast
    )   
    db.session.add(player)
    db.session.commit()
    # generate_animator(tweetId,tweet, 'mossholder')
    # generateNewAudiogram(tweetId)
    

tweet = """5 Things Every Woman Should Do Immediately After Having Intercourse To Keep The Vagina Healthy

A thread
1. Use the bathroom before and after intercourse

You can reduce your risk of contracting urinary tract infections and regulate your lady's part pH level by using the bathroom after having intercourse.
2. Make sure you wipe from front to back

The right way to wipe after having intercourse to prevent the building up of harmful bacteria that may probably cause UTIs is frm front to bck.This is because if U are wiping from the back to the front, U may contaminate the lady's part
3. Always let yourself dry off after you take a shower

It is important to note that excess moisture and warmth are a breeding ground for infections, so make sure your female organ is not left moist before you put on your panties.
4. Gently clean the area

All you will need for the cleaning up should be mild soap and water. You can gently wash out sweat, semen, and bacteria by wiping from front to back using mild soap and water.
5. Avoid douching with all possible efforts
Douching is a very bad habit and should be avoided by every lady. One of the bad effects of douching is that it removes the healthy bacteria in your female organ thereby making it prone to infections and diseases."""
