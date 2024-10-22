from transformers import AutoTokenizer, ClapTextModelWithProjection
from sklearn.metrics.pairwise import cosine_similarity

model = ClapTextModelWithProjection.from_pretrained("laion/clap-htsat-unfused")
tokenizer = AutoTokenizer.from_pretrained("laion/clap-htsat-unfused")

raw_inputs = ["a sound of a cat", "a sound of a dog"]

inputs = tokenizer(raw_inputs, padding=True, return_tensors="pt")

outputs = model(**inputs)
text_embeds = outputs.text_embeds.detach().numpy()

s = cosine_similarity(text_embeds)
print(s)