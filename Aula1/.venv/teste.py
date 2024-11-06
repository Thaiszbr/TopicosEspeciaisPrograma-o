import os
#set para inserir a API KEY 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
#Echo para mostrar a API KEY
from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Crie uma historia infantil em 4 paragrafos",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)