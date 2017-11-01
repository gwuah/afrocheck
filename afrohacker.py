import tweepy

# api keys/tokens here pls
# I am not father christmas
API_KEY = ''
API_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# twitter handle of the colony leaders!
KINGS_NAME = "gwuah_"
QUEEN_NAME = "Afrohacker"

# handle basic auth
def authenticate():
	auth = tweepy.OAuthHandler(API_KEY, API_TOKEN)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return tweepy.API(auth)

def main(): 
	# handle the f*cking authentication
	try:
		api = authenticate()
		griffith = api.get_user(KINGS_NAME)
	except Exception as e:
		print(e)

	# bond strength algorithm :)
	for friend in griffith.friends():
		if friend.screen_name == QUEEN_NAME:
			return True

	return False

if __name__ == '__main__':
	print("Gimme a minute lemme check if she's still following you\n")
	if main():
		print("The queen is still following you!")
		input("press any key to quit ..")
	else:
		print("You lost her!! :()")
		input("press any key to quit ..")
