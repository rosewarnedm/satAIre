from openai import OpenAI
import base64
client = OpenAI()

prompt = """
A cartoon showing the English cricket team looking dejected and sooty with flames in the background at an Australian cricket ground. The crowd is holding banners saying
'Take that Poms' and 'Something to whinge about'.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Ashes.png", "wb") as f:
    f.write(image_bytes)
