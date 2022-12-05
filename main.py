import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import warnings
import re

import mailsender
import subscription

# for every user, their max count of tweets can be fetched (pretty much useless unless they're spamming)


def getTweets(user: str, since: dt) -> pd.DataFrame():

    collector = pd.DataFrame.from_dict({
        'User': [],
        'Content': [],
        'Likes': []
    })

    for i, tweet in zip(range(subscription.maxcount), sntwitter.TwitterUserScraper(user).get_items()):

        # check if the user has made tweet within the timeframe
        if tweet.date < since:
            if i == 0:
                print(user, 'has no tweets in the timeframe')
            return collector


        # filter out any tweet with query items
        txt = tweet.content.lower()

        for q in subscription.query:
            if bool(re.search(q, tweet.content)):
                break
        else:
            continue

        # print(user)
        # print(txt)
        # print(tweet.date)
        # print(tweet.media, type(tweet.media))

        collector = collector.append({'User':user, 'Content':tweet.content, 'Likes':tweet.likeCount}, ignore_index=True)
        # collector = pd.concat([collector, pd.DataFrame([user, tweet.content, tweet.likeCount])], ignore_index=True)

    # return df

def gettime(minsago=5):
    timenow = dt.utcnow() + relativedelta(minutes=-minsago)
    timenow = timenow.replace(tzinfo=datetime.timezone.utc)
    return timenow


def m_fetchData() -> tuple:
    df = pd.DataFrame()
    for user in subscription.users:
        df = pd.concat([df, getTweets(user, gettime(subscription.mins_ago))])

    # try sorting it
    try:
        df = df.sort_values('Likes', ascending=False)
    except Exception:
        print('empty df')

    df = df.reset_index(drop=True)

    isempty = df.empty
    # filename = 'output_' + str(dt.utcnow())[5:13].replace(' ', '_') + '.csv'
    # use a more simple filename to save space
    filename = 'output.csv'

    df.to_csv(filename)
    return (isempty, filename)

def main():

    data = m_fetchData()

    if data[0]:
        print('No data within the timeframe')
        return
    else:

        df = pd.read_csv(data[1])
        print('filename:', data[1])
        print(df)

        body = f'{len(df)} tweets were made in the past {subscription.mins_ago/60} hours -\n\n'


        for i, row in df.iterrows():

            body += str(row['User']) + ' - ' + str(row['Likes']) + ' likes\n'
            body += str(row['Content']) + '\n\n'


        if mailsender.sendMail(f'{str(dt.utcnow())[5:13]} Crypto Feed :)', body):
            print('mail sent :)')
        else:
            print('an error occured when sending the mail :(')

if __name__ == '__main__':
    main() # returns a tuple (isempty, filename)
