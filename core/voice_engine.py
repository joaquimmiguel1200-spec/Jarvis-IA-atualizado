# Python 3.12+
import pyttsx3
import speech_recognition as sr
import logging
from typing import Self

logging.basicConfig(level=logging.INFO)

class VoiceEngine:
    """Responsável pela audição (STT) e fala (TTS) do JARVIS."""
    
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self._setup_voice()

    def _setup_voice(self) -> None:
        voices = self.engine.getProperty('voices')
        # Tenta encontrar uma voz masculina/formal
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 0.9)
        if len(voices) > 0:
            self.engine.setProperty('voice', voices[0].id)

    def speak(self, text: str) -> None:
        logging.info(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> str | None:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                logging.info("Ouvindo...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio, language="pt-BR")
                return command.lower()
            except sr.UnknownValueError:
                return None
            except Exception as e:
                logging.error(f"Erro na escuta: {e}")
                return None