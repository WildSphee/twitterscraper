import snscrape.modules.twitter as sntwitter
import subscription


for user in subscription.users:
    i = sntwitter.TwitterUserScraper.is_valid_username(user)
    print(user, i)
