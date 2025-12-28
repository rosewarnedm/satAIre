from openai import OpenAI
import base64
client = OpenAI()

prompt = """Show our Prime Minister Keir as having an archery target for a body with arrows sticking out at various points including the bulls-eye.  Make the background a green and pleasant land in which dogs and monkeys roam dressed as humans.  Caption the picture with 'Bullseye'
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Keir_target.png", "wb") as f:
    f.write(image_bytes)
