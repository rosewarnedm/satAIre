from openai import OpenAI
import base64
client = OpenAI()

prompt = """ Create a cartoon of Meghan and Harry playing hide and seek in their Montecito palace trying, but failing, to find a real friend, Meghan saying "H, be a poppet and find me a real 'As Ever' friend" 
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Sussexes_friends.png", "wb") as f:
    f.write(image_bytes)
