from smolagents import LiteLLMModel, CodeAgent
import os
# Load environment variables
from dotenv import load_dotenv
load_dotenv()
# Ensure the E2B_API_KEY is set
e2b_api_key = os.getenv("E2B_API_KEY")
if not e2b_api_key:
    raise ValueError("E2B_API_KEY is not set in the environment variables.")

# Initialize the LiteLLMModel with the E2B API key and Ollama model
model = LiteLLMModel(
    model_id="ollama_chat/phi3:mini",   # Or "ollama_chat/mistral"
    # model_id="ollama_chat/qwen2:7b",
    api_base="http://localhost:11434",  # Default Ollama port
)

with CodeAgent(model=model, tools=[], executor_type="e2b") as agent:
    agent.run("Can you give me the 100th Fibonacci number?")
