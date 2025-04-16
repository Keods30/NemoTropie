from yt_dlp import YoutubeDL
import cv2
import hashlib

def get_stream_url(youtube_url):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_url = info_dict['url']
        return video_url

def capture_entropy_from_stream(stream_url):
    """
    Captures a single frame from a video stream and computes its entropy hash.

    This function connects to a video stream source, captures a single frame, 
    and computes a SHA3-512 hash of the frame's raw binary data to generate
    an entropy value.

    Args:
        stream_url (str): URL or identifier of the video stream to capture from.

    Returns:
        str: A hexadecimal string representing the SHA3-512 hash of the captured frame.

    Raises:
        Exception: If the video stream cannot be accessed or if frame capture fails.

    Examples:
        >>> entropy = capture_entropy_from_stream("http://example.com/video_stream")
        >>> print(len(entropy))
        128
    """
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        raise Exception("Impossible d'accéder au stream vidéo.")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("Erreur lors de la capture de la frame.")
    frame_bytes = frame.tobytes()
    entropy = hashlib.sha3_512(frame_bytes).hexdigest()
    return entropy

if __name__ == "__main__":
    youtube_link = "https://www.youtube.com/watch?v=yuhnCtTPtZo"
    stream_url = get_stream_url(youtube_link)
    entropy = capture_entropy_from_stream(stream_url)
    print("✨ Clé aléatoire générée depuis l'aquarium :", entropy)
