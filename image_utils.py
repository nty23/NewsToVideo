from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
from io import BytesIO

def generate_background_image(prompt, size=(1280, 720)):
    # Using Hugging Face inference API for image generation
    API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"
    headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code != 200:
        raise Exception("Image generation failed")
    image = Image.open(BytesIO(response.content)).resize(size)
    path = "background.png"
    image.save(path)
    return path

def generate_image_with_text(text, image_path="background.png", output_path="frame.png"):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)

    wrapper = textwrap.TextWrapper(width=60)
    lines = wrapper.wrap(text=text)
    y = 100
    for line in lines:
        draw.text((100, y), line, font=font, fill="white")
        y += 50

    img.save(output_path)
    return output_path
