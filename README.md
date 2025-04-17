# 🐠 NemoTropie

**NemoTropie** is a real-time entropy generator based on natural chaos observed in live aquarium streams. It extracts randomness from unpredictable elements like fish movements, bubble trails, or wave distortions.

---

## 🌊 What is NemoTropie?

NemoTropie captures a frame from a YouTube livestream and processes it to create a cryptographically robust entropy string. This key can be used in cryptographic contexts, secure token generation, or as a unique identifier.

---

## ⚙️ How It Works

1. 📺 Select or randomly choose a livestream (e.g., Aquarium of the Pacific).
2. 🎥 Capture a frame from the stream.
3. 🎲 Add entropy: current timestamp + secure random bytes.
4. 🔐 Apply SHAKE-256 to generate a 512-bit base64 encoded output.

---

## 📁 Project Structure

```
.
├── index.html          # Web interface (UI + p5.js animations)
├── api.py              # FastAPI backend (POST /generate)
├── main.py             # CLI version for entropy generation
├── modules/
│   ├── stream.py       # Handles YouTube stream and frame capture
│   └── hash.py         # Builds entropy with noise + hashing
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install fastapi uvicorn yt-dlp opencv-python numpy
```

### Run backend

```bash
uvicorn api:app --reload
```

### Launch frontend

Open `index.html` in a browser.

---

## 🛡️ Security Note

This project does **not rely solely on hash functions**. Entropy is enhanced with:
- Cryptographic noise (`os.urandom`)
- Real-time frame randomness
- Time-based salt (`time.time_ns()`)

---

## 🌐 Credits

Live streams used for entropy:
- Aquarium of the Pacific (California)
- Vienna Zoo (Austria)
- Jeju Aquarium (Korea)

---

## 📄 License

MIT – Free to use and modify.
