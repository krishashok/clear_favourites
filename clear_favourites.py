from twython import Twython
import oauth2 as oauth

# Uncomment these lines and fill in your details before running
# access_token_key = <Your access token key>
# access_token_secret <Your access token secret>

# consumer_key = <Your consumer key>
# consumer_secret <Your consumer secret>

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

def clear_favourites():
	t = Twython(consumer_key, consumer_secret, access_token_key, access_token_secret)

	# Let's start at page 1 of your favourites because you know, it's a very good place to start
	count = 1

	# Now, let's start an infinite loop and I don't mean the one with Apple's HQ
	while True:

		# Get your favourites from Twitter
		faves = t.get_favorites(page=count)

		# If there's no favourites left from this page, do the Di Caprio and jump out
		if len(faves) == 0:
			break

		# Programmers have been doing inception for ages before Nolan did. Let's go deeper and get
		# into another loop now
		for fav in faves:
			t.destroy_favorite(id=fav['id'])

		count += 1

		# Now comes the all important part of the code. As my grandmother once told me, it is
		# important to get good sleep, and we shall precisely do that for 15 minutes because you know
		# Twitter mama hates rate-limit violators
		sleep(900)

	

if __name__ == '__main__':
  clear_favourites()


