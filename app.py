from flask import Flask, render_template, Response, request
from pytube import YouTube

app = Flask(__name__)

def download(link, quality):
    link = link

    YouTube_1 = YouTube(link)

    videos = YouTube_1.streams.all()
    vid = list(enumerate(videos))

    for i in vid:
        print(i)

    print()

    strm = quality
    videos[strm].download()
    print("Success")

@app.route("/", methods = ['GET', 'POST'])
def hello():
    if request.method=='POST':
        link = request.form['lname']
        filename = request.form['tname']
        location = request.form['fname']
        print(link)
        download(link=link, quality=location)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)  