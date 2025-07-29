import json
import sys

def clean_notebook_metadata(notebook_path):
    """Remove widget metadata that causes Git issues"""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Remove widget metadata from notebook metadata
    if 'metadata' in notebook:
        if 'widgets' in notebook['metadata']:
            del notebook['metadata']['widgets']
    
    # Clean cell metadata
    for cell in notebook.get('cells', []):
        if 'metadata' in cell:
            # Remove widget references
            if 'colab' in cell['metadata']:
                if 'referenced_widgets' in cell['metadata']['colab']:
                    del cell['metadata']['colab']['referenced_widgets']
        
        # Clean outputs that contain widget data
        if 'outputs' in cell:
            cleaned_outputs = []
            for output in cell['outputs']:
                if 'data' in output:
                    if 'application/vnd.jupyter.widget-view+json' in output['data']:
                        del output['data']['application/vnd.jupyter.widget-view+json']
                    # Only keep the output if it still has data
                    if output['data']:
                        cleaned_outputs.append(output)
                else:
                    cleaned_outputs.append(output)
            cell['outputs'] = cleaned_outputs
    
    # Write back the cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"Cleaned notebook: {notebook_path}")

if __name__ == "__main__":
    notebook_path = "C:\\Users\\user\\Documents\\HuggingFace\\AI_Agent\\AIAgentHandsOn\\SmolAgents\\code_agents.ipynb"
    clean_notebook_metadata(notebook_path)