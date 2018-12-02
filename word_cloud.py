from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import uuid

def generate_cloud(tokens):
    str = ' '.join(tokens)
    wordcloud = WordCloud(width=1280, height=720,
                    background_color='white',
                    min_font_size=10).generate(str)

    plt.figure(figsize=(16,9), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    fname = uuid.uuid4().hex + ".jpg"
    plt.savefig("static/cloudimgs/" + fname)
    return fname