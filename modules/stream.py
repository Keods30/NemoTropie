# modules/stream.py
from yt_dlp import YoutubeDL
import cv2

class StreamCapture:
    def __init__(self, youtube_url: str):
        self.youtube_url = youtube_url
        self.stream_url = self._get_stream_url()

    def _get_stream_url(self) -> str:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'quiet': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.youtube_url, download=False)
            return info_dict['url']

    def capture_frame(self):
        cap = cv2.VideoCapture(self.stream_url)
        if not cap.isOpened():
            raise Exception("Impossible d'accéder au stream vidéo.")
        ret, frame = cap.read()
        cap.release()
        if not ret:
            raise Exception("Erreur lors de la capture de la frame.")
        return frame
