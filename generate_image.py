from openai import OpenAI
import base64
client = OpenAI()

prompt = """
A black and white cartoon showing a glum fat shirtless grey haired prince in a jail cell with sweat showering from his armpits'.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Andrew_MBW.png", "wb") as f:
    f.write(image_bytes)
