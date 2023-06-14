import openai
openai.api_key = "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"

prompt = "The quick brown fox"
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  max_tokens=50
)

generated_text = response.choices[0].text.strip()
print(generated_text)
