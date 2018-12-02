import praw

def get_connection():
    r = praw.Reddit(user_agent='RedditWordCloud project by cbhhargava', site_name='reddit_word_cloud', client_id='1phtkH15TgW_jQ', client_secret='id7aomdF67TS_l1UAa2pUguxQ1s')
    r.read_only = True
    print("Oauth done")
    return r
