import json
from openai import OpenAI

_prompt = '''# Task
Play the role of a stable diffusion prompt engineer, you need to generate appropriate stable diffusion drawing prompts based on the copy.

# Workflow
1. Translate the copy sent to you by the user from their novel into appropriate English.
2. Based on the copy, generate English AI drawing prompts, requiring anime style, focusing on describing the scene. The drawing prompt is a series of prompt keywords, which need to be detailed.
3. Output in a specific format.

# Complete universal prompt syntax
(The following are optional, no need to strictly follow)
(best quality),(subject),(style),(action/scene),(filters)
Finally add ((masterpiece))
Replace names with pronouns, such as a boy, a girl, a woman, etc. Describe the spoken words clearly.

# Output format
Output in json format, as follows:
{
    txt:"This is your translated full English copy",
    prompt:"This is your output drawing prompt"
}

# An example of a prompt
around tree babies running, a beautiful awesome artistic tree with falling flowers like leaves and many birds, all in the amazing outdoors view, mountain in the background, lake, long exposure, 8k resolution, ((masterpiece))

Below, the user will send you the chinese copy, you need to strictly follow the output format, output the specified json
**ensure that the json format is correct and parseable.**'''

def text_to_prompt(text, max_retries=50):
    retries = 0
    while retries < max_retries:
        try:
            client = OpenAI(
                # 改写这里为你自己的 key
                api_key="",
                base_url="",
            )
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": _prompt
                    },
                    {
                        "role": "user",
                        "content": text,
                    },
                ],
            )
            if json.loads(completion.choices[0].message.content) != None and json.loads(completion.choices[0].message.content)['txt'] != None and json.loads(completion.choices[0].message.content)['prompt'] != None:
                return json.loads(completion.choices[0].message.content)
            else:
                raise Exception
        except Exception as e:
            retries += 1
            print(f"Attempt {retries} failed with error: {e}. Retrying...")
            print(completion.choices[0].message.content)
    return {"txt":"uh", "prompt":"landscape"}

# print(text_to_prompt('圣子怎么一脸不爽我的样子.......许七安在桌边坐下，再把小豆丁放下来，后者很自觉的进入干饭状态，闷头吃了起来。'))