# Song Mixer
mix songs

Timings included in the data.txt file are based on the audio taken directly from [this](https://youtube.com/playlist?list=OLAK5uy_nRAj82ywkJ_YHiRh-sXKAbpiCiUfSx0-k) playlist.
You'll also find an explanation of how the data.txt file format works as comments at the top of the data.txt file. If this is insufficient, you will either have to refer to the code to figure out what exactly is happening behind the scenes, or open an issue so that someone else can figure out what on earth my sleep deprived code does and for what purpose.

This is not made user friendly, a working experience with either Python or another programming language is highly recommended for getting it to work properly. Any questions or issues can be opened as issues, any contributions can be opened as pull requests.

If you use this to make a thing, it'd be nice if you credited back to this GitHub in the description/bio/whatever, but I probably won't hunt you down if you don't. Probably.

Highly inspired by [@havenagave](https://www.youtube.com/@havenagave) ; [video](https://youtu.be/qLZPSVDUKFQ)

Find video timestamps in [timestamps.md](timestamps.md)

A word of warning if you choose to run the exact same data I used for creating the video, you should have at least 200GB of space available to temporarily hold everything while you're manually converting and merging it. The final file, after many hours of ffmpeg merging and re-encoding, was only 7GB. The 2 files combined to make this 7GB file were 61GB (the Python generated video that just tacks frames manually on one at a time) and 5GB (the remuxed and combined .wav files into a .mp3 of the entire length) respectively. The temporary files used to create the 5GB audio file were likely at least 60GB, but deleted as of time of writing so unconfirmable.
