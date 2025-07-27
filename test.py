from smolagents import LiteLLMModel, CodeAgent, WebSearchTool

# Define the model (connected to your local Ollama server)
# model = LiteLLMModel(
#     model_id="ollama_chat/qwen2:7b",         # Prefix "ollama_chat/" tells LiteLLM it's local Ollama
#     api_base="http://127.0.0.1:11434",       # Local Ollama server
#     num_ctx=8192                             # Max context tokens
# )

model = LiteLLMModel(
    model_id="ollama_chat/phi3:mini",
    api_base="http://127.0.0.1:11434",
    num_ctx=4096,
)


# Create a simple agent
# agent = CodeAgent(tools=[], model=model)

# Add more authorized imports for web scraping or API calls:
agent = CodeAgent(
    # tools=[WebSearchTool()], 
    tools = [],
    model=model,
    # additional_authorized_imports=["requests", "wikipedia", "json"]
)


# Run the agent with a task
response = agent.run("Summarize the key benefits of using Ollama locally.")

print(response)
# This code initializes a LiteLLMModel connected to a local Ollama server and creates a SmolAgent to run a task.