from openai import OpenAI
import base64
client = OpenAI()

prompt = """
A cartoon of a muscled guy in sunglasses trying to park his Ferrari and berating a wizened pensioner in a disabled parking space standing by an old-style beat up rusty mini with the speech bubble 'Hop it old timer, this is my Motability space'"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Motability.png", "wb") as f:
    f.write(image_bytes)
