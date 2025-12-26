from openai import OpenAI
import base64
client = OpenAI()

prompt = """
Create a cartoon of prime minister Keir as a claw-hammer with his face as the centre of the head and his neck and body the woodden handle of the hammer"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Starmer_tool.png", "wb") as f:
    f.write(image_bytes)
