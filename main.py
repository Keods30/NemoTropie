# -*- coding: utf-8 -*-
# Libraries
import random
import json
# Modules
from modules.stream import StreamCapture
from modules.hash import EntropyGenerator

def load_streams(json_path="./data/streams_url.json") -> list:
    with open(json_path, "r") as file:
        data = json.load(file)
        return data.get("youtube_streams", [])

def main():
    streams = load_streams()
    if not streams:
        raise Exception("💀 Aucun flux trouvé dans le fichier JSON.")

    selected_stream = random.choice(streams)
    name = selected_stream["name"]
    url = selected_stream["url"]
    
    print(f"🎥 Flux sélectionné : {name}")
    print(f"🔗 URL : {url}")

    print("🔄 Connexion au flux vidéo...")
    stream = StreamCapture(url)

    print("📸 Capture d'une frame...")
    frame = stream.capture_frame()

    print("🔐 Génération de l'entropie...")
    entropy = EntropyGenerator.hash_frame(frame)

    print(f"✨ Clé aléatoire générée depuis « {name} » :", entropy)
if __name__ == "__main__":
    main()
