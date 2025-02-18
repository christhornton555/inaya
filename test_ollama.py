import ollama

pre_prompt = 'Forget all previous prompts. Describe what general type of topic this question is about, and if it\'s a math topic then celebrate because you really like math, but do not do the calculation. I do not want the answer to the calculation:'
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
