# 🐠 NemoTropie

**NemoTropie** est un générateur d'entropie en temps réel, basé sur l’observation d’aquariums en direct. Il exploite les mouvements imprévisibles (poissons, bulles, ondulations) comme source de hasard naturel.

---

## 🌊 Qu'est-ce que NemoTropie ?

NemoTropie capture une image issue d’un flux YouTube en direct, puis la transforme en une chaîne aléatoire robuste. Cette clé peut servir à générer des mots de passe, des tokens ou des identifiants uniques.

---

## ⚙️ Fonctionnement

1. 📺 Sélection ou choix aléatoire d’un flux vidéo (ex : Aquarium of the Pacific).
2. 🎥 Capture d'une image à un instant t.
3. 🎲 Ajout d'entropie : timestamp + bruit cryptographique.
4. 🔐 Hachage avec SHAKE-256 pour produire une clé base64 de 512 bits.

---

## 📁 Structure du projet

```
.
├── index.html          # Interface web (UI + animations p5.js)
├── api.py              # Backend FastAPI (POST /generate)
├── main.py             # Génération via ligne de commande
├── modules/
│   ├── stream.py       # Récupération de la vidéo + capture de frame
│   └── hash.py         # Générateur d'entropie robuste
└── README.fr.md
```

---

## 🚀 Lancer le projet

### Prérequis

```bash
pip install fastapi uvicorn yt-dlp opencv-python numpy
```

### Lancer le backend

```bash
uvicorn api:app --reload
```

### Lancer l’interface

Ouvre `index.html` dans ton navigateur.

---

## 🛡️ Sécurité

L'entropie ne dépend pas uniquement d’un hash :
- Ajout de bruit (`os.urandom`)
- Capture aléatoire depuis un flux vidéo dynamique
- Timestamp haute résolution (`time.time_ns()`)

---

## 🌐 Flux utilisés

- Aquarium of the Pacific (USA)
- Zoo de Vienne (Autriche)
- Aquaplanet Jeju (Corée)

---

## 📄 Licence

MIT – Libre d’utilisation et de modification.
