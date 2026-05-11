from openai import OpenAI

client = OpenAI()

def explain(row):
    prompt = f"Explain financial discrepancy: {row}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.contents
