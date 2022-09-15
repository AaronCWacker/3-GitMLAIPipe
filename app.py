import gradio as gr
from transformers import pipeline
title = "Transformers 📗 Sentence to Paragraph ❤️ For Mindfulness"
examples = [
    ["Feel better physically by"],
    ["Practicing mindfulness each day"],
    ["Be happier by"],
    ["Meditation can improve health"],
    ["Spending time outdoors"],
    ["Stress is relieved by quieting your mind, getting exercise and time with nature"],
    ["Break the cycle of stress and anxiety"],
    ["Feel calm in stressful situations"],
    ["Deal with work pressure"],
    ["Learn to reduce feelings of overwhelmed"]
]
from gradio import inputs
from gradio.inputs import Textbox
from gradio import outputs

generator2 = gr.Interface.load("huggingface/EleutherAI/gpt-neo-2.7B")
generator3 = gr.Interface.load("huggingface/EleutherAI/gpt-j-6B")
generator1 = gr.Interface.load("huggingface/gpt2-large")
gr.Parallel(generator1, generator2, generator3, inputs=gr.inputs.Textbox(lines=5, label="Enter a sentence to get another sentence."),
            title=title, examples=examples).launch(share=False)
