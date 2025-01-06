from transformers import MusicgenForConditionalGeneration
# Reference: https://github.com/AIAnytime/Text-to-Music-Generation-App/blob/main/app.py

# load pretrained model
# the different models we can load: https://huggingface.co/facebook/musicgen-small
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
print("model loaded successfully")
