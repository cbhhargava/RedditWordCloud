from praw.models import MoreComments
import process_text

def get_corpus(reddit, post_link):
    clean_tokens = []
    submission = reddit.submission(url=post_link)
    submission.comments.replace_more(limit = 5)
    for comment_queue1 in submission.comments:
        if isinstance(comment_queue1, MoreComments):
            continue
        clean_tokens.extend(process_text.get_tokens(comment_queue1.body))
        if(len(clean_tokens)>1000):
            break
    for comment_queue1 in submission.comments:
        for comment_queue2 in comment_queue1.replies:
            if isinstance(comment_queue2, MoreComments):
                continue
            clean_tokens.extend(process_text.get_tokens(comment_queue2.body))
            if(len(clean_tokens)>1000):
                break
    for comment_queue1 in submission.comments:
        for comment_queue2 in comment_queue1.replies:
            for comment_queue3 in comment_queue2.replies:
                if isinstance(comment_queue3, MoreComments):
                    continue
                clean_tokens.extend(process_text.get_tokens(comment_queue3.body))
                if(len(clean_tokens)>1000):
                    break
    print(clean_tokens)
    return clean_tokens