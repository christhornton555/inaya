import ollama

stream = ollama.chat(
    model='deepseek-r1:8b',
    messages=[{'role': 'user', 'content': 'Who is the current president of the USA?'}],
    stream = True
)

for chunk in stream:
    print(chunk['message']['content'], end = '', flush = True)
    