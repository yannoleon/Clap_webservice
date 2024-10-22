from fastapi import FastAPI, Response
from transformers import AutoTokenizer, ClapTextModelWithProjection
from sklearn.metrics.pairwise import cosine_similarity
from pydantic import BaseModel

# ----------------------------MODEL-----------------------------------------------------

model = ClapTextModelWithProjection.from_pretrained("laion/clap-htsat-unfused")
tokenizer = AutoTokenizer.from_pretrained("laion/clap-htsat-unfused")

# -----------------------------APP------------------------------------------------------

app = FastAPI()

class Text_entry(BaseModel):
    text: list[str]

@app.post('/text_cosine', response_model=Text_entry)
def text_cosine(text_entry:Text_entry):

    inputs = tokenizer(text_entry.text, padding=True, return_tensors="pt")

    outputs = model(**inputs)
    text_embeds = outputs.text_embeds.detach().numpy()

    s = str(cosine_similarity(text_embeds))

    texts_str = ''.join([t + '\n' for t in text_entry.text])

    res = f"<h1> Cosine similarities between:\n {texts_str} is:\n {s} </h1>"

    return Response(res)
