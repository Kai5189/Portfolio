from pytube import YouTube

url = 'https://www.youtube.com/watch?v=RgFTkKSvyDY'
Video= YouTube(url)

print(Video.title)

print(Video.thumbnail_url)

Video = Video.streams.get_highest_resolution()

Video.download()