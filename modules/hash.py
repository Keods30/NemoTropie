# modules/hash.py
import hashlib

class EntropyGenerator:
    @staticmethod
    def hash_frame(frame) -> str:
        """
        Prend une image (frame OpenCV) et retourne son hash SHA3-512.

        Args:
            frame (np.ndarray): image capturée

        Returns:
            str: hash hexadécimal de la frame
        """
        frame_bytes = frame.tobytes()
        return hashlib.sha3_512(frame_bytes).hexdigest()
