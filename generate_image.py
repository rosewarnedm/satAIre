from openai import OpenAI
import base64
client = OpenAI()

prompt = """Show a cartoon of Nigel, leader of the Reform Party revelling on New Year's eve with four smoking cigarettes in his mouth, a lighted cigar in one hand with a pint of beer in a handled mug and his arm around a nice looking woman 
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Nigel_NYE.png", "wb") as f:
    f.write(image_bytes)
