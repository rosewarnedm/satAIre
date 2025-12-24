from openai import OpenAI
import base64

client = OpenAI()

prompt = ('''
Make me a cartoon with a battered Jake Paul and Einstein in a maths competition.  They are in a boxing ring.  Einstein is in front of a blackboard with Tensor calculus.  Jake Pauls board says '1 on 1 = $92 000 000'

'''
)

response = client.responses.create(
    model="gpt-5",
    input=prompt,
    tools=[{"type": "image_generation"}],
)

# Extract base64 image from the response
image_base64 = None
for output in response.output:
    if output.type == "image_generation_call":
        image_base64 = output.result
        break

if image_base64:
    with open("Einstein_Jake_Paul.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
    print("Saved christmas_doghouse.png")
else:
    raise RuntimeError("No image returned from GPT-5 image generation")
