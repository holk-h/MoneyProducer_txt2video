# MoneyProducer_txt2video

[English Readme](resource/readme_english.md)

## 项目简介

使用 stable-diffusion（或者任意 AI 绘图平台，更改 api 即可）和大语言模型（LLM），一键将小说文本自动转换成 AI 配图的有声小说视频。

示例输出视频：


https://github.com/holk-h/MoneyProducer_txt2video/assets/29571233/47e0d9e2-e0e4-4546-9747-a8ad35af4b73



## 功能特色

- **文本到视频转换**：自动将小说文本转换为配有视觉内容的有声小说视频。
- **多语言支持**：支持中文和英文小说的转换，满足不同用户的需求。

## 安装指南

1. **克隆仓库**

```bash
git clone https://github.com/holk-h/MoneyProducer_txt2video.git
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **运行项目**

```bash
python main_cli.py
```

## 使用说明

1. 将小说文本文件拆分（可使用或魔改 `utils/split_txt.py` 工具），按照 `chapters_x.txt` 的格式，放置于某个目录下，文件夹命名为小说名字。
2. 启动 [stable-diffusion-web-ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)，修改 `utils/sd.py` 中的 api 地址（记得启动的时候加上 `--api --listen` 参数）
3. 修改 `utils/llm.py` 中的 key 为你自己的 key（或者自己换不同的 llm api）
4. 在根目录执行 `python main_cli.py` 命令，小说名字（文件夹名）、生成的章节范围均可更改。
5. 视频文件将生成在 `output` 目录中。
6. 若视频过长，可使用 `utils/split_video.sh` 或者 `utils/split_video.bat` 切分视频
7. 英文字幕会生成在 `subtitle` 文件夹里（中文字幕直接就是原始文本），可以使用剪映等软件识别并创建字幕

## 贡献指南

欢迎任何形式的贡献，无论是新功能的建议、bug修复，还是文档的改进。请遵循以下步骤：

1. Fork 项目仓库。
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 将您的更改推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开一个Pull Request。

