import os
import re

def remove_unwanted_text(text):
    """移除章节标题、空行和空格"""
    # 移除章节标题
    text = re.sub(r'\d+\.第\d+章.*?[\r\n]+', '', text, flags=re.DOTALL)
    # 移除所有空行
    text = re.sub(r'\n\s*\n', '\n', text)
    # 移除所有行首和行尾的空格（包括文本中间的空行）
    text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)
    return text

def split_and_save_chapters(file_path):
    # 获取文件夹名（不含扩展名）
    folder_name = os.path.splitext(os.path.basename(file_path))[0]
    # 如果文件夹不存在，则创建
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 打开并读取原始文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 移除不需要的文本：章节标题、空行和空格
    content_cleaned = remove_unwanted_text(content)
    
    # 使用分界线分割文本，移除分界线本身
    chapters = content_cleaned.split('===')
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]  # 移除空白章节
    
    # 初始化文件计数器
    file_count = 1
    
    for i in range(0, len(chapters), 10):
        # 每十章作为一组，提取这十章（如果不足十章，则提取剩余的所有章节）
        chapters_group = chapters[i:i+10]
        
        # 定义新文件名，格式为 "chapters_1.txt"、"chapters_2.txt" 等
        new_file_name = os.path.join(folder_name, f'chapters_{file_count}.txt')
        
        # 保存当前章节组到新文件中，不包括原分界线
        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            # 将章节组合并成一个字符串，每章之间用一个换行符分隔
            new_file.write('\n'.join(chapters_group))
        
        # 文件计数器递增，准备下一组章节的保存
        file_count += 1

# split_and_save_chapters('example.txt')
