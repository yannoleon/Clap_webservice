from datasets import load_dataset
from transformers import ClapAudioModelWithProjection, ClapProcessor

model = ClapAudioModelWithProjection.from_pretrained("laion/clap-htsat-fused")
processor = ClapProcessor.from_pretrained("laion/clap-htsat-fused")

dataset = load_dataset("ashraq/esc50")
audio_sample = dataset["train"]["audio"][0]["array"]

inputs = processor(audios=audio_sample, return_tensors="pt")
outputs = model(**inputs)
audio_embeds = outputs.audio_embeds
print(audio_embeds)