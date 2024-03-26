#!/bin/bash

# 设置视频文件路径
video_path="xx"
# 设置临时存储静音检测结果的文件
silence_output="silence_detect.txt"
# 设置输出目录
output_dir="output_videos"

# 使用ffmpeg检测静音
ffmpeg -i "$video_path" -af silencedetect=noise=-30dB:d=0.5 -f null - 2> "$silence_output"

# 创建输出目录
if [ ! -d "$output_dir" ]; then
  mkdir "$output_dir"
fi

# 初始化变量
count=0
split_duration=$((15*60)) # 15分钟转换为秒
last_split=0

# 读取静音检测结果并分割视频
while IFS=":" read -r label time; do
  if [[ $label == "silence_start" ]]; then
    silence_start=${time%.*} # 移除小数部分
    duration=$((silence_start-last_split))
    if [ $duration -ge $split_duration ]; then
      # 计算切分点并切割视频
      split_point=$((last_split+split_duration))
      ffmpeg -i "$video_path" -ss $last_split -to $split_point -c copy "$output_dir/output_part_$count.mp4"
      ((count++))
      last_split=$split_point
    fi
  fi
done < <(grep "silence_start" "$silence_output")

# 处理最后一段视频
ffmpeg -i "$video_path" -ss $last_split -c copy "$output_dir/output_part_$count.mp4"

echo "完成视频切分。"
