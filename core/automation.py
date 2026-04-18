# Python 3.12+
import pyautogui
import webbrowser
import subprocess
import logging
import time
from pathlib import Path

class TaskAutomator:
    """Executa ações diretas no Sistema Operacional (RPA)."""

    def __init__(self) -> None:
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def open_browser_search(self, query: str) -> None:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        logging.info(f"Pesquisando por: {query}")

    def type_text(self, text: str) -> None:
        logging.info(f"Digitando texto: {text[:20]}...")
        pyautogui.write(text, interval=0.05)

    def launch_work_mode(self) -> None:
        """Abre ferramentas de produtividade."""
        try:
            # Exemplo de abertura via subprocess
            subprocess.Popen(["code"]) # VS Code
            webbrowser.open("https://slack.com")
            webbrowser.open("https://stackoverflow.com")
            logging.info("Modo trabalho ativado.")
        except FileNotFoundError as e:
            logging.error(f"Erro ao abrir aplicação: {e}")

    def launch_leisure_mode(self) -> None:
        """Abre ferramentas de lazer."""
        webbrowser.open("https://www.spotify.com")
        webbrowser.open("https://www.youtube.com")
        logging.info("Modo lazer ativado.")

    def press_key_hotkey(self, *keys: str) -> None:
        pyautogui.hotkey(*keys)