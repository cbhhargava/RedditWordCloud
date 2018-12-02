from flask import Flask, flash, redirect, render_template, request, session, abort
import oauth, fetch, word_cloud, urllib.parse, os

IMGS_FOLDER = os.path.join('static', 'cloudimgs')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMGS_FOLDER

@app.route("/redditcloud")
def render_img():
    redurlenc = request.args.get("redurlenc")
    if redurlenc is None:
        return render_template('index.html',cloudimg='')
    red = oauth.get_connection()
    redurl = urllib.parse.unquote(redurlenc)
    tok = fetch.get_corpus(red, redurl)
    fname = word_cloud.generate_cloud(tok)
    img = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    print(fname)
    return render_template("index.html", cloudimg = img)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)