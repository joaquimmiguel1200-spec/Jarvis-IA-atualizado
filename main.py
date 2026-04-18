# Python 3.12+
import time
import sys
import logging
from core.voice_engine import VoiceEngine
from core.automation import TaskAutomator
from core.monitor import SystemMonitor

class JarvisAI:
    def __init__(self) -> None:
        self.voice = VoiceEngine()
        self.automation = TaskAutomator()
        self.monitor = SystemMonitor()
        self.is_active = True

    def process_command(self, command: str) -> None:
        match command:
            case c if "jarvis" in c and "status" in c:
                status = self.monitor.get_report()
                report = f"Senhor, a CPU está em {status.cpu_usage}%, Memória RAM em {status.ram_usage}%"
                if status.battery:
                    report += f" e bateria em {status.battery}%"
                self.voice.speak(report)

            case c if "modo trabalho" in c:
                self.voice.speak("Ativando protocolos de produtividade. Abrindo VS Code e Slack.")
                self.automation.launch_work_mode()

            case c if "modo lazer" in c:
                self.voice.speak("Entendido. Preparando ambiente de descanso.")
                self.automation.launch_leisure_mode()

            case c if "pesquise por" in c:
                query = c.split("pesquise por")[-1].strip()
                self.voice.speak(f"Pesquisando {query} no Google.")
                self.automation.open_browser_search(query)

            case c if "digite" in c:
                text_to_type = c.split("digite")[-1].strip()
                self.voice.speak("Digitando em 3 segundos. Por favor, foque no campo.")
                time.sleep(3)
                self.automation.type_text(text_to_type)

            case c if "encerrar" in c or "desligar" in c:
                self.voice.speak("Desligando sistemas. Até logo, senhor.")
                self.is_active = False
                sys.exit()

            case _:
                if "jarvis" in command:
                    self.voice.speak("Comando não reconhecido na minha base de RPA, senhor.")

    def run(self) -> None:
        self.voice.speak("Sistemas JARVIS online e operantes.")
        
        while self.is_active:
            raw_command = self.voice.listen()
            
            if raw_command:
                logging.info(f"Ouvido: {raw_command}")
                self.process_command(raw_command)
            
            time.sleep(0.1) # Reduz consumo de CPU

if __name__ == "__main__":
    try:
        jarvis = JarvisAI()
        jarvis.run()
    except KeyboardInterrupt:
        logging.info("Interrupção manual detectada.")