from openai import OpenAI
import base64
client = OpenAI()

prompt = """Show a cartoon Of Maduro of Venezuela glowering out of an wooden animal crate stacked with other containers on a cargo ship. Put a direction sign 'Guantanamo Bay 100km' in the sea ahead of the boat.  Caption this with 'You saw it before now watch the sequel:  Extraordinary Rendition II' 
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Rendition.png", "wb") as f:
    f.write(image_bytes)
