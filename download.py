from yt_dlp import YoutubeDL
import os

#audio/nameディレクトリがなければ作成
if not os.path.exists("video"):
    os.mkdir("video")

#最高の画質と音質を動画をダウンロードする
ydl_opts = {}
with  YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=2NeHaKAmm1w'])