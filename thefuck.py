import sys
import re

from llama_cpp import Llama


MODEL_PATH="<path_to_gguf>"

PROMPT = """Respond only with corrected command.
Command entered by user: `{}`
Error message:
```
{}
```
Corrected command:
"""


llm = Llama(
      model_path=MODEL_PATH,
      n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      #n_ctx=8192, # Uncomment to increase the context window
      verbose=False
)


def correct_command(command: str, error_message: str, prompt: str) -> str:
    output = llm(
        prompt.format(command, error_message),
        max_tokens=8192,
        echo=False, # Echo the prompt back in the output
        top_p=0.14,
        top_k=49,
        min_p=0.,
        repeat_penalty=1.17,
        temperature=0,
        #stop=["\n"]
    )
    output_str = output["choices"][0]["text"]
    #print(output_str)
    output_str = re.sub("\*\*[Gg]uess:\*\*\s*", "", output_str)

    try:
        return re.search("```\n.*?(.*)\n```", output_str).group(1)
    except AttributeError:
        try:
            return re.search("```.*?(.*)\n```", output_str).group(1)
        except AttributeError:
            try:
                return re.search("`(.*)`", output_str).group(1)
            except AttributeError:
                return output_str.strip()


def read_logfile(filename: str) -> (str, str):
    with open(filename, "r") as f:
        content = f.read()
    split_content = content.split("\n", 1)
    command = split_content[0]
    stderr_output = split_content[1]
    return command, stderr_output


if __name__ == "__main__":
    log_file = sys.argv[1]
    command, stderr_output = read_logfile(log_file)
    print(correct_command(command, stderr_output, PROMPT))
