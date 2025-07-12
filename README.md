<p align="center">
  <img src="assets/eliz_cover.png" width="400"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
  <img src="https://img.shields.io/badge/Project-Active-brightgreen"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Voice-Japanese_Anime_Style_Coming_Soon-red?style=for-the-badge&logo=coqui"/>
</p>


# 🤖 ELIZ - Smart Voice Bot (Online Version)

`smart_voice_bot_online.py` is a voice assistant that listens, understands, responds, and speaks back in natural language using online tools. Built with Python, ELIZ is your AI companion that answers questions, tells jokes, opens websites, and even controls your PC.

---

## 🛠 Features Implemented

### 🎤 1. Voice Input (Speech Recognition)

* Library: `speech_recognition`
* Captures audio from the microphone.
* Uses Google’s online speech recognition API to convert speech to text.

### 🗣️ 2. Voice Output (Speech Synthesis)

* Library: `pyttsx3`
* Offline text-to-speech engine using SAPI5 (Windows)
* Supports voices like David, Zira, Hazel

### 🔍 3. Wikipedia Search

* Library: `wikipedia`
* Extracts short summaries based on your queries
* Example: "Who is Nikola Tesla?"

### 🌐 4. Web Browsing

* Library: `webbrowser`
* Opens websites like Google, YouTube, etc.

### 🤪 5. Fun Mode - Jokes

* Uses `random.choice()` to respond with fun jokes.

### 🧠 6. System Control Commands

* Library: `os`, `ctypes`
* Lock screen, shutdown, open applications, etc.

### 🛑 7. Wake Word (Planned Feature)

* Planned wake word detection using `Vosk` or keyword spotting.
* Trigger phrase: "Hey Eliz"

---

## 🚀 Tech Stack

* Python 3.x
* `speech_recognition`
* `pyttsx3`
* `wikipedia`
* `webbrowser`, `os`, `random`, `ctypes`

---

## 🔮 Future Features (Planned)

* ✅ Face Recognition with YOLO integration (to greet Dabi)
* ✅ Anime-style voice using Coqui TTS (`xtts_v2`, `kokoro`)
* ✅ Voice cloning / personality customization
* ✅ Context memory (ELIZ remembers previous interactions)
* ✅ GUI / Mobile controller

---

## 📦 How to Run

1. Install dependencies:

```bash
pip install pyttsx3 speechrecognition wikipedia
```

2. Run the Python file:

```bash
python smart_voice_bot_online.py
```

---

## 👤 Made By

**Vasudev Saras (aka Dabi)**
B.Tech Robotics and Automation, Saintgits College of Engineering
Languages: English | Malayalam | Hindi

---

Let’s build ELIZ into a fully functional anime-style AI assistant 💬🎧
