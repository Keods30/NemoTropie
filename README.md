# 🐠 NemoTropie

**NemoTropie** is an original entropy generator that uses a live stream of an aquarium as a physical source of randomness. Inspired by chaotic natural movements such as fish swimming, bubbles rising, and light refraction, NemoTropie extracts high-quality entropy from visual noise.

---

## 🌊 What is NemoTropie?

NemoTropie captures frames from a live video stream of an aquarium and converts the pixel data into a cryptographically secure hash. This provides a unique and non-deterministic random seed, ideal for generating keys, tokens, or any use case requiring high-quality entropy.

---

## 🔧 How It Works

1. Connects to a live video stream (e.g. public webcam of an aquarium).
2. Captures one or more frames at a random or regular interval.
3. Extracts raw pixel data from the image.
4. Hashes the data using a secure function (e.g. SHA-256 or BLAKE2).
5. Optionally combines it with other entropy sources (system time, urandom...).
6. Outputs a unique random string.

