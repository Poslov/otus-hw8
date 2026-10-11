from ollama_client import OllamaClient


def test_model_returns_consistent_answers():
    client = OllamaClient()

    prompt = (
        "What is the capital of France? "
        "Answer in one word."
    )

    answers = []

    for _ in range(3):
        response = client.generate(prompt)

        assert response.status_code == 200

        answer = response.json()["response"].strip().lower().rstrip(".")
        answers.append(answer)

    assert len(set(answers)) == 1, (
        f"Model returned inconsistent answers: {answers}"
    )

    assert answers[0] == "paris", (
        f"Model returned an incorrect answer: {answers[0]}"
    )