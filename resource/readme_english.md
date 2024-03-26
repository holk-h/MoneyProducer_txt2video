# MoneyProducer_txt2video

## Project Introduction

`MoneyProducer_txt2video` is capable of using stable diffusion (or any AI drawing technology, provided it offers an API) and large language models (LLM) to automatically convert novel texts into AI-illustrated audiobook videos with just one click.

Example output video:
[](./resource/example.mp4)

## Feature Highlights

- **Text-to-Video Conversion**: Automatically transforms novel texts into audiobook videos with visual content.
- **Multilingual Support**: Supports the conversion of novels in both Chinese and English, meeting the needs of different users.

## Installation Guide

1. **Clone the Repository**

```bash
git clone https://github.com/holk-h/MoneyProducer_txt2video.git
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Project**

```bash
python main_cli.py
```

## Usage Instructions

1. Split the novel text file (you can use or modify the `utils/split_txt.py` tool), and place them in a directory in the format of `chapters_x.txt`.
2. Modify the API address of [stable-diffusion-web-ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) in `utils/sd.py` (remember to start it with the `--api --listen` parameter).
3. Change the key in `utils/llm.py` to your own key (or switch to a different llm API).
4. Execute the `python main_cli.py` command in the root directory.
5. Video files will be generated in the `output` directory.
6. If the video is too long, you can use `utils/split_video.sh` or `utils/split_video.bat` to split the video.

## Contribution Guide

Any form of contribution is welcome, whether it's suggesting new features, fixing bugs, or improving the documentation. Please follow these steps:

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push your changes to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.