from e2b_code_interpreter import Sandbox

import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Ensure the E2B_API_KEY is set
# e2b_api_key = os.getenv("E2B_API_KEY")
# if not e2b_api_key:
#     raise ValueError("E2B_API_KEY is not set in the environment variables.")

# Create the sandbox
sandbox = Sandbox()
# sandbox = Sandbox()
# print("✅ Sandbox created!")

# Install required packages
sandbox.commands.run("pip install smolagents 'smolagents[litellm]' 'smolagents[e2b]'")

def run_code_raise_errors(sandbox, code: str, verbose: bool = False) -> str:
    execution = sandbox.run_code(
        code,
        envs={'HF_TOKEN': os.getenv('HF_TOKEN'), 
              'E2B_API_KEY': os.getenv('E2B_API_KEY')},
    )
    if execution.error:
        execution_logs = "\n".join([str(log) for log in execution.logs.stdout])
        logs = execution_logs
        logs += execution.error.traceback
        raise ValueError(logs)
    return "\n".join([str(log) for log in execution.logs.stdout])

# Define your agent application
agent_code = """
import os
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel
from dotenv import load_dotenv
load_dotenv()

# Ensure the E2B_API_KEY is set
# e2b_api_key = os.getenv("E2B_API_KEY")
# if not e2b_api_key:
#     raise ValueError("E2B_API_KEY is not set in the environment variables.")
    
model = LiteLLMModel(
    model_id="ollama_chat/phi3:mini",   # Or "ollama_chat/mistral"
    # api_base="http://localhost:11434",  # Default Ollama port
    api_base="https://0fda724485d8.ngrok-free.app",  # Use your ngrok URL here
)

# Initialize the agents
agent = CodeAgent(
    # model=InferenceClientModel(token=os.getenv("HF_TOKEN"), provider="together"),
    model = model,
    executor_type="e2b",
    # executor_type="local",
    executor_kwargs={'api_key': os.getenv('E2B_API_KEY')},
    # executor_kwargs={"api_key": e2b_api_key},
    tools=[],
    name="coder_agent",
    description="This agent takes care of your difficult algorithmic problems using code."
)

manager_agent = CodeAgent(
    # model=InferenceClientModel(token=os.getenv("HF_TOKEN"), provider="together"),
    model=model,
    # executor_type="e2b",
    tools=[],
    managed_agents=[agent],
)

# Run the agent
response = manager_agent.run("What's the 20th Fibonacci number?")
print(response)
"""

# Run the agent code in the sandbox
execution_logs = run_code_raise_errors(sandbox, agent_code)
print(execution_logs)
