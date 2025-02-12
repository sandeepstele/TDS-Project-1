# TDS-Project-1
- Create Codespaces on evaulate branch and do the following
- first install uv , then create enviroment and then uv pip install -r requirements.txt
- then install ollama and olllama serve and then ollama pull qwen2.5 model
- then cd into app and uvicorn main:app --reload and in another terminal run ollama model and yet in another terminal run evaluate script(modified for testing)
- notes: task 8 is cheating i need to use multimodal, email_from_text task sometimes lucks out, task a9 for embedding also needs call to gpt-4o-mini

## Commands to run 
- Terminal 1
Should see started app started sucessfully
```bash
pip install uv
uv venv 
source venv/bin/activate
uv pip install -r requirements.txt
cd app
uvicorn main:app --reload 
```
-Terminal 2
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
ollama pull qwen2.5:3b
```

-Terminal 3
```bash
python evaluate.py
```
Note that ollama should be running on port 11434, uvicorn on 8000