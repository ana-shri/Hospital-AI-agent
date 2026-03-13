import requests

# Load hospital knowledge
with open("knowledge.txt", "r") as f:
    hospital_info = f.read()


def ask_assistant(question):

    prompt = f"""
You are a helpful AI hospital assistant.

Use the hospital information below to answer the patient's question clearly.

Hospital Information:
{hospital_info}

Patient Question:
{question}

Answer clearly in bullet points.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


while True:

    question = input("\nPatient: ")

    if question.lower() == "exit":
        break

    answer = ask_assistant(question)

    print("\nAssistant:")
    print(answer)