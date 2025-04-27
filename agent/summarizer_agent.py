from llm.groq_client import groq_client


def summarize_text(text):
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful summarizer."},
            {"role": "user", "content": f"Summarize the following article:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content
