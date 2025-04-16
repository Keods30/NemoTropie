# main.py
from modules.stream import StreamCapture
from modules.hash import EntropyGenerator

def main():
    youtube_url = "https://www.youtube.com/watch?v=yuhnCtTPtZo"
    
    print("🌊 Connexion au flux vidéo...")
    stream = StreamCapture(youtube_url)
    
    print("📦 Capture d'une frame...")
    frame = stream.capture_frame()
    
    print("🔥 Génération de l'entropie...")
    entropy = EntropyGenerator.hash_frame(frame)
    
    print("✨ Clé aléatoire générée depuis l'aquarium :", entropy)

if __name__ == "__main__":
    main()
