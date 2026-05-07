# Voice Assistant using Python 🎙️🤖

A simple AI Voice Assistant built using Python that can recognize voice commands and perform basic tasks like opening websites, telling the time, and launching applications.

## Features ✨

* Voice Recognition using SpeechRecognition
* Text-to-Speech using pyttsx3
* Open websites like:

  * YouTube
  * Google
  * Facebook
  * ChatGPT
  * Cyberbots
* Tell the current time
* Open Calculator
* Exit with voice command (`bye`)

---

## Technologies Used 🛠️

* Python
* SpeechRecognition
* pyttsx3
* datetime
* webbrowser

---

## Installation 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/Mugilan-Theroboticist/web_Assistant.git
cd web_Assistant
```

### 2. Install Required Libraries

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

> Note: If `pyaudio` gives installation errors on Windows, install it using:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## How to Run ▶️

Run the Python file:

```bash
python assistant.py
```

The assistant will start listening for voice commands.

---

## Supported Voice Commands 🎤

| Command           | Action                  |
| ----------------- | ----------------------- |
| "hello"           | Greets the user         |
| "time"            | Tells current time      |
| "open youtube"    | Opens YouTube           |
| "open google"     | Opens Google            |
| "open facebook"   | Opens Facebook          |
| "open calculator" | Opens Calculator        |
| "cyber"           | Opens Cyberbots website |
| "chatgpt"         | Opens ChatGPT           |
| "bye"             | Stops the assistant     |

---

## Project Structure 📂

```bash
├── web_assistant.py
└── README.md
```

---

## Future Improvements 🚀

* Add weather updates
* Add WhatsApp automation
* Add AI chatbot integration
* Add music playing feature
* Add system control commands
* Add GUI interface

---

## Example Output 💻

```bash
Listening...
You said: open youtube
Opening YouTube
```

---

## Author 👨‍💻

Developed by Mugilan
Robotics & AI Enthusiast 🤖
