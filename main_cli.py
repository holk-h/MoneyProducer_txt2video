import os
import utils.text_utils as text_utils
import utils.llm as llm
import utils.sd as sd
import utils.tts as tts
import asyncio
import utils.video_util as video_util
from tqdm import tqdm

async def generate_videos(start_chapter, end_chapter, base_txt_dir):
    chapter_files = sorted([f for f in os.listdir(base_txt_dir) if f.startswith('chapters_') and f.endswith('.txt')],
                           key=lambda x: int(x.split('_')[1].split('.')[0]))

    chapter_files = [f for f in chapter_files if start_chapter <= int(f.split('_')[1].split('.')[0]) <= end_chapter]

    for chapter_order, txt_file in enumerate(chapter_files, start=start_chapter):
        txt_name = base_txt_dir + '_' + txt_file.split('.')[0]
        try:
            os.makedirs(f'./audios/{txt_name}/en')
            os.makedirs(f'./audios/{txt_name}/cn')
            os.makedirs(f'./images/{txt_name}', exist_ok=True)
            os.makedirs(f'./output/en', exist_ok=True)
            os.makedirs(f'./output/cn', exist_ok=True)
            os.makedirs(f'./subtitles/{txt_name}', exist_ok=True)
            print(f"Folder '{txt_name}' created successfully.")
        except FileExistsError:
            print(f"Folder '{txt_name}' already exists.")

        txt_path = os.path.join(base_txt_dir, txt_file)
        txt = text_utils.read_txt(txt_path)
        subtitles = []

        for index, text in enumerate(tqdm(txt, total=len(txt))):
            out = llm.text_to_prompt(text)
            subtitles.append(out['txt'])
            await tts.generate_speech(out['txt'], 'en', txt_name, index+1)
            await tts.generate_speech(text, 'cn', txt_name, index+1, 'zh-CN-YunxiNeural')
            sd.generate_image(prompt=out['prompt'], seed=114514, width=405, height=720, txt_name=txt_name, order=index+1)

        try:
            with open(f'./subtitles/{txt_name}/subtitle_{chapter_order}.txt', 'w') as f:
                f.write('\n'.join(subtitles))
        except Exception as e:
            print(e)

        video_util.create_video_with_audio_images(len(txt), txt_name, chapter_order, 'cn')
        video_util.create_video_with_audio_images(len(txt), txt_name, chapter_order, 'en')

async def main():
    # 修改这里的章节数
    await generate_videos(1, 5, 'example_txt')

if __name__ == "__main__":
    asyncio.run(main())
