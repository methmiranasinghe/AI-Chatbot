# Troubleshooting

## `pyaudio` installation fails
- Install system packages: `sudo apt install -y portaudio19-dev python3-dev`
- Try binary wheels: `pip install --only-binary=:all: pyaudio || pip install pyaudio`

## No microphone found / permission denied
- Verify your microphone is connected and selected as default input.
- On Linux, ensure user is in `audio` group and PulseAudio/PipeWire is running.

## Assistant does not hear me
- Check that "Listening..." appears.
- Reduce background noise or move closer to the mic.
- Increase ambient noise adjustment duration in `takeCommand` if needed.

## "SAPI5" engine error on non-Windows platforms
- `pyttsx3.init('sapi5')` is Windows-only. On Linux or macOS, use:
```python
engine = pyttsx3.init()
```

## `os.startfile` not found on Linux/macOS
- `os.startfile` is Windows-only. Replace with `subprocess` or `xdg-open`/`open` as appropriate.

## Wikipedia errors or rate limits
- Try different queries; ensure internet connectivity.
- Catch exceptions around `wikipedia.summary` and provide fallback messages.
