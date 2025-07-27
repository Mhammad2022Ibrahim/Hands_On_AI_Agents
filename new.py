from langchain.tools import tool

@tool
# @tool(parse_docstring=True)
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

# print(calculator.to_string())
# print(calculator.args_schema.model_json_schema())
      
print(f"Tool name: {calculator.name}")
print(f"Tool description: {calculator.description}")
print(f"Tool args: {calculator.args}")
print(f"Result: {calculator.run({'a': 5, 'b': 3})}")