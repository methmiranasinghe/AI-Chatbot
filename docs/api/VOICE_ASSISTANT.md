# Voice Assistant API Reference

This project exposes a voice-driven command loop in `jarvis.py`. Below are the public functions and their behavior, with usage examples.

## Module: `jarvis.py`

### `speak(text: str) -> None`
Converts `text` to speech using `pyttsx3` and waits until the utterance completes.

- Raises: Any `pyttsx3` runtime errors if the TTS engine fails.
- Side effects: Speaks out loud.

Example:
```python
from jarvis import speak
speak("Hello world")
```

### `wishMe() -> None`
Greets the user based on current time (morning/afternoon/evening/night) and prompts for help.

- Depends on: `datetime.datetime.now()` and `speak`.
- Side effects: Speaks greeting out loud.

Example:
```python
from jarvis import wishMe
wishMe()
```

### `takeCommand() -> str`
Listens through the default system microphone and returns recognized text in English (India locale) using Google Speech Recognition.

- Calibrates for ambient noise for ~1 second.
- Returns the recognized string, or the literal string "None" if recognition fails.

Example:
```python
from jarvis import takeCommand
query = takeCommand()
if query != "None":
    print("You said:", query)
```

### Command loop (script entry point)
When run as a script, `jarvis.py`:
1. Calls `wishMe()`
2. Enters an infinite loop:
   - `query = takeCommand().lower()`
   - Matches keywords to perform actions:
     - `wikipedia <topic>`: speaks Wikipedia summary
     - `open youtube`: opens YouTube
     - `open google maps`: opens Google Maps
     - `play music`: opens Spotify web
     - `play video`: opens first file in `F:\\Video` (Windows-specific)
     - `open code`: starts VS Code at `C:\\...Code.exe` (Windows-specific)
     - `open camera`: starts `C:\\Windows\\camera.exe` (Windows-specific)
     - `what is your name`: speaks its name
     - `goodbye`: says goodbye and exits
     - default: says it did not recognize the command

## Platform Notes
- The current configuration uses `pyttsx3.init('sapi5')` which is Windows-only.
- File launching with `os.startfile` is Windows-only.

## Extending Commands
Add new `elif` blocks inside the `while True` loop after obtaining `query`.

Example - open Twitter:
```python
elif 'open twitter' in query:
    webbrowser.open('https://twitter.com')
```

Example - robust Wikipedia handling:
```python
elif 'wikipedia' in query:
    speak('Searching Wikipedia')
    try:
        topic = query.replace('wikipedia', '').strip()
        result = wikipedia.summary(topic, sentences=2)
        speak('According to Wikipedia')
        speak(result)
    except Exception:
        speak('Sorry, I could not fetch a summary right now')
```
