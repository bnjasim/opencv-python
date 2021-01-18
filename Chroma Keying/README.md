# Chroma Keying

The code is written in opencv python

run: python chroma.py

It reads the foreground video and a background image and output a series of frames by blending the foreground object with the new background.

As I was having trouble making the video writer work, I used ffmpeg to combine these frames into a single video
ffmpeg -r 60  -i %d.jpg -vcodec libx264 -crf 25  -pix_fmt yuv420p output.mp4

Watch the output video here: https://youtu.be/tBXsnxHT_dQ