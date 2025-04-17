# modules/hash.py
import hashlib
import base64

class EntropyGenerator:
    @staticmethod
    def hash_frame(frame) -> str:
        """
        Prend une image (frame OpenCV) et retourne une chaîne aléatoire encodée en base64.

        Args:
            frame (np.ndarray): image capturée

        Returns:
            str: chaîne aléatoire plus lisible, encodée en base64
        """
        frame_bytes = frame.tobytes()
        hash_bytes = hashlib.sha3_512(frame_bytes).digest()
        base64_entropy = base64.b64encode(hash_bytes).decode('utf-8')
        return base64_entropy
