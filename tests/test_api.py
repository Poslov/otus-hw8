from ollama_client import OllamaClient


def test_generate_returns_valid_response():
    client = OllamaClient()

    response = client.generate(
        "What is the capital of France? Answer in one word."
    )

    assert response.status_code == 200

    data = response.json()

    assert data["model"].startswith("llama3")
    assert isinstance(data["response"], str)
    assert data["response"].strip()
    assert data["done"] is True