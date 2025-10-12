# Getting Started

## Prerequisites
- Python 3.9+
- Working microphone and audio drivers
- System dependencies for `pyaudio`

On Debian/Ubuntu:
```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-dev
```

## Install Dependencies
Create and activate a virtual environment, then install packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pyttsx3 SpeechRecognition wikipedia pyfiglet pyaudio
```

Note: If `pyaudio` fails to install from wheels, try:
```bash
pip install --only-binary=:all: pyaudio || pip install pyaudio
```

## Run the Assistant
```bash
python jarvis.py
```

You should see an ASCII banner and voice greetings.
