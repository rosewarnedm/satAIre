from openai import OpenAI
import base64
client = OpenAI()

prompt = """
A cartoon of the Prime Minister yoked to a plough as a beast of burden (horses body and Keir's head) and ploughing a deep U-shaped furrow whilst farmers look on derisively"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Keir_U_turn.png", "wb") as f:
    f.write(image_bytes)
