import requests


class OllamaClient:
    BASE_URL = "http://localhost:11434"
    MODEL = "llama3"

    def generate(self, prompt: str) -> requests.Response:
        return requests.post(
            url=f"{self.BASE_URL}/api/generate",
            json={
                "model": self.MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "seed": 42
                }
            },
            timeout=120
        )