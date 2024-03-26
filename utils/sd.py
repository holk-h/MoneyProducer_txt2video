import requests
import base64

def generate_image(prompt: str, seed: int, width: int, height: int, txt_name, order):
    url = "http://127.0.0.1:7860"
    # print(prompt)
    payload = {
        "prompt": prompt,
        "negative_prompt": "booty, boob, (nsfw), (painting by bad-artist-anime:0.9), (painting by bad-artist:0.9), watermark, text, error, blurry, jpeg artifacts, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, artist name, (worst quality, low quality:1.4), bad anatomy",
        "cfg_scale": 7,
        "steps": 20,
        "seed": seed,  
        "width": width,  
        "height": height,
        "override_settings": {
            "sd_model_checkpoint": "anythingelse-V4_v45",
            # "CLIP_stop_at_last_layers": 2,
        }
    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()

    output_filename = f"./images/{txt_name}/{order}.png"
    with open(output_filename, 'wb') as f:
        f.write(base64.b64decode(r['images'][0]))

# generate_image("(Best Quality), a boy, Anime, sitting, eating, ((masterpiece)) <lora:ChosenChineseStyleNsfw_v20:1>", 114514191981, 540, 960, 'test1', 3)
