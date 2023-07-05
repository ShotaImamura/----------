import subprocess
import os

# Define the video file
name = "rkmtlabMeeting616"

video_file = "video/{}.mp4".format(name)

# Define the output audio file
audio_file = "audio/{}.mp3".format(name)

audio_short_file = "audio/{}/%03d.mp3".format(name)

#audio/nameディレクトリがなければ作成
if not os.path.exists("audio/{}".format(name)):
    os.mkdir("audio/{}".format(name))

# Run ffmpeg to extract audio
command = f"ffmpeg -i {video_file} -ab 160k -ac 2 -ar 44100 -vn {audio_file}"
subprocess.call(command, shell=True)

# Run ffmpeg to split audio
command = f"ffmpeg -i {audio_file} -f segment -segment_time 600 -c copy {audio_short_file}"
subprocess.call(command, shell=True)
