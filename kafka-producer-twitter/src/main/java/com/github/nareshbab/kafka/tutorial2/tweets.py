import tweepy


consumer_key = "Baw6s1bPeODLPaUDOKr32PFd6"
consumer_secret = "mxfATysteInhidYTHWXmC1m45lrw4xFR4sTfeDfHqukIvq9zYT"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPHBXQEAAAAAbKgyPphrBceRSJSzr6a%2BRLwPN0Q%3DseZC5sqaoCQQwK328ddhbXUnPQ25ZqthNu67MBqFLOONSn7ZHa"
access_token = "3060134244-B3thADkKhDuqcyZGq6LUvjmTQdgUO92PVGT5tKk"
access_token_secret = "gxTyTOOlSL39wTNLs2siuCME3PPuOVQVvu6a0TFMQqSrA"

"oauth_token=2qrKgwAAAAABXdoTAAABffpZe1o&oauth_verifier=eT0ZSKYXx76UtzXU6NucjVxYrmD7pJSA"
# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print('Error! Failed to get request token.')
# session.set('request_token', auth.request_token)
# # Example using callback (web app)
# verifier = request.GET.get('oauth_verifier')
#
# # Let's say this is a web app, so we need to re-build the auth handler
# # first...
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# token = session.get('request_token')
# session.delete('request_token')
# auth.request_token = token
#
# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print('Error! Failed to get access token.')
#
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# test authentication
api.verify_credentials()