# thefuck-gpt

A silly little project trying to emulate the magnificent [thefuck](https://github.com/nvbn/thefuck) using a local LLM (GGUF only). 

![thefuck](https://github.com/user-attachments/assets/71579992-3835-4791-a56d-6b59a7476326)

## Installation
### Requirements
- Python 3.8+
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

Steps to install:
1. Clone this project
2. Change the variable `MODEL_PATH` in `thefuck.py` to the absolute path of the GGUF file of the LLM you want to use. Some model recommendations:  
	- [Qwen2.5-Coder-7B-Instruct](https://huggingface.co/bartowski/Qwen2.5-Coder-7B-Instruct-GGUF)
	- [gemma-2-2b-it](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF)
3. Replace the placeholder in `guessed_command` inside `fuck.sh` with the absolute path to `thefuck.py`
4. Add `source <absolute_path_to>/fuck.sh` to your `.bashrc` or `.zshrc`