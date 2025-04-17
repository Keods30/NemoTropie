# modules/hash.py
import hashlib
import base64
import os
import time
import numpy as np

class EntropyGenerator:
    @staticmethod
    def hash_frame(frame: np.ndarray) -> str:
        """
        Génère une clé d'entropie à partir d'une image, d'un timestamp, et de bruit cryptographique.
        Utilise SHAKE-256 pour un résultat plus résistant aux attaques.
        """
        timestamp = str(time.time_ns()).encode()
        noise = os.urandom(64)
        frame_bytes = frame.tobytes()
        entropy_data = frame_bytes + timestamp + noise
        digest = hashlib.shake_256(entropy_data).digest(64)  # 512 bits
        return base64.b64encode(digest).decode('utf-8')
