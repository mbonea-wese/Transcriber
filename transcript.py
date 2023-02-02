import youtube_dl
import whisper
import uuid


def downloadFile(url):
    fileName = f"{str(uuid.uuid4())}.mp4"
    video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': fileName,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return fileName


def Transcribe(url):

    fileName = downloadFile(url)
    # Select speech recognition model
    name = 'tiny'
    model = whisper.load_model(name, device='cpu')
    result = model.transcribe(fileName)
    print(result['segments'])
