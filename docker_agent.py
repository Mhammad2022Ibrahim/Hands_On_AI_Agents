from smolagents import InferenceClientModel, CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/phi3:mini",   # Or "ollama_chat/mistral"
    # model_id="ollama_chat/qwen2:7b",
    api_base="http://localhost:11434",  # Default Ollama port
)

# with CodeAgent(model=InferenceClientModel(), tools=[], executor_type="docker") as agent:
with CodeAgent(model=model, tools=[], executor_type="docker") as agent:
    agent.run("Can you give me the 100th Fibonacci number?")