import ollama

pre_prompt = 'Forget all previous prompts. Tell me whether this is a math question or not, but absolutely do not answer the question. Do not answer the question. Only tell me if it is a math question or not. The only two valid answers are \"MATH\" or \"NOT MATH\":'
input_prompt_a = 'Who is the current president of the USA?'
input_prompt_b = 'What is fourteen divided by two?'

stream = ollama.chat(
    model='deepseek-r1:8b',
    messages=[{'role': 'user', 'content': f'{pre_prompt} \"{input_prompt_b}\"'}],
    stream = True
)

print(f'{pre_prompt} \"{input_prompt_b}\"')

for chunk in stream:
    print(chunk['message']['content'], end = '', flush = True)
