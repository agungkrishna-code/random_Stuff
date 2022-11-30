from pytube import YouTube

def Download(link):
  YouTubeObject = YouTube(link)
  YouTubeObject = YouTubeObject.streams.get_highest_resolution()
  try:
    YouTubeObject.download()
  except:
    print("error downloading video")
  print("download completed")

link = input("Put your youtube link here!! URL: ")
Download(link)
