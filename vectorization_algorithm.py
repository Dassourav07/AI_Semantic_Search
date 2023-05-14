import openai

# Set OpenAI API key
openai.api_key = "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"

def encode_text(text):
    # Encode text into vector representation using OpenAI's latest text embeddings
    vector = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Encode the following text into a vector representation:\n{text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    ).choices[0].text
    return vector