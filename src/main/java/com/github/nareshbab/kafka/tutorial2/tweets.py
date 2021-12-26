import tweepy

api_key = "kvJ1kQ01W1sIBPEhr2MSM4Oyh"
api_secret = "6DCCIXbdUZ7mJbSzn8GVlmWqCwVW01XTHfuyjWEDIQ5NvX3jOq"

consumer_key = "Y0NSYmJuMF8xd1ZSRXB5VGFId246MTpjaQ"
consumer_secret = "zBIQOKmFs-_mdZWrZdYCLlwjKNHu3zOwmVd2nnrtX-QGpZl5AK"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPHBXQEAAAAAbKgyPphrBceRSJSzr6a%2BRLwPN0Q%3DseZC5sqaoCQQwK328ddhbXUnPQ25ZqthNu67MBqFLOONSn7ZHa"
access_token = "3060134244-TTdbP1em805htDlOLXZBwgyQKZbFlTmx6vdOEGK"
access_token_secret = "gqq4v8KWKAnKDrd0M3Pc3a7Bev46sw1hIRy6LBU9tlwfT"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")