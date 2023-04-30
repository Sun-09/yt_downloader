from pytube import YouTube

link = "https://www.youtube.com/watch?v=96YyRY8vkhY&ab_channel=EarCandy"

YouTube_1 = YouTube(link)

print(YouTube_1.title)

print(YouTube_1.thumbnail_url)
videos = YouTube_1.streams.all()
vid = list(enumerate(videos))

for i in vid:
    print(i)

print()

strm = ""
videos[strm].download()
print("Success")