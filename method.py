from pytube import YouTube
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = ROOT_DIR + "\media"

def Download(link, dirlocation=MEDIA_DIR):
    if dirlocation != MEDIA_DIR:
        dirlocation = dirlocation+"/"
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio= True)
    try:
        file = youtubeObject[0].download(dirlocation)
        # print("file :",file)
        base, ext = os.path.splitext(file)
        # print("base :", base)
        new_file_name = base +'.mp3'
        # print("new file name :",new_file_name)
        os.rename(file, new_file_name)
  
    except Exception as e:
        raise e