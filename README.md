An AI-powered assistant designed to help patients prepare for hospitalisation by answering common questions about hospital admission, surgery preparation, discharge procedures, and post-hospital follow-ups.

This project uses a local Large Language Model (Llama3 via Ollama) combined with a custom hospital knowledge base to provide helpful guidance through an interactive Streamlit chatbot interface.

 Features

 AI chatbot for hospital preparation questions

 Guidance on admission documents and requirements

 Advice on what to carry before surgery

 Information about hospital discharge procedures

 Suggestions for post-hospital follow-up care

 Simple and interactive Streamlit web interface

 Runs locally using Ollama (Llama3) — no external API required

 Tech Stack

Python

Streamlit

Ollama

Llama3 (Local LLM)

Requests

 How It Works

The user asks a hospital-related preparation question through the Streamlit interface.

The system combines the question with information from a hospital knowledge base.

The prompt is sent to a local LLM (Llama3) via Ollama.

The AI generates a response and returns it to the user interface.

 Example Questions

What documents are required for hospital admission?

What should a patient carry before surgery?

What happens during hospital discharge?

What follow-ups are required after hospitalisation?

⚠️ Disclaimer

This assistant provides general informational guidance only and should not be considered professional medical advice. Always consult a qualified healthcare provider for medical decisions.
