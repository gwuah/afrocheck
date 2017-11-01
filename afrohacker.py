import tweepy

# api keys/tokens here pls
# I am not father christmas
API_KEY = '8Qvtc4uE2aVeRnQ0c1WMMBm2o'
API_TOKEN = 'JVMdC3WNs6ytxIT7itJU4icOZuCC4rPjaZSseqZigALPD0Pbzr'
ACCESS_TOKEN = '822769558931079169-eycjRZ8Yb9LTV7MSUASVWmpuqmzX5iV'
ACCESS_TOKEN_SECRET = 'FmEJf5U9OlWv7bkcNPwszAPo8euB3ZUQTZHcn0dn56Loi'

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
