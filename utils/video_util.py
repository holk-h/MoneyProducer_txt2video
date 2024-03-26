from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def create_video_with_audio_images(length, txt_name, order, lang):
    """
    根据提供的图片集长度，生成一个视频。
    图片和音频列表将在函数内部生成。

    Parameters:
    - length: 图片集的长度，也是音频文件的数量。
    - txt_name: 视频名称。
    - lang: 音频的语言（'en' 或 'cn'）。
    """
    # 根据长度和语言生成图片和音频文件的路径列表
    images = [f'./images/{txt_name}_chapters_{order}/{i}.png' for i in range(1, length + 1)]
    audios = [f'./audios/{txt_name}_chapters_{order}/{lang}/{i}.mp3' for i in range(1, length + 1)]

    # 创建视频片段列表
    clips = []

    for img_path, audio_path in zip(images, audios):
        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(img_path).set_duration(audio_clip.duration).set_audio(audio_clip)
        clips.append(image_clip)

    # 连接视频片段
    final_clip = concatenate_videoclips(clips, method="compose")

    # 输出最终视频
    final_clip.write_videofile(f"./output/{lang}/{txt_name}_chapters_{order}.mp4", fps=24)

# 调用函数示例，为英文和中文音频分别创建视频
# create_video_with_audio_images(2, 'test1', 'en')  # 为英文音频创建视频
# create_video_with_audio_images(2, 'test1', 'cn')  # 为
# create_video_with_audio_images(821, '万古狂帝', 1, 'en')