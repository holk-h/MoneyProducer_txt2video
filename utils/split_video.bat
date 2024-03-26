@echo off
setlocal enabledelayedexpansion

REM 设置视频文件路径
set "video_path=xx"
REM 设置临时存储静音检测结果的文件
set "silence_output=silence_detect.txt"
REM 设置输出目录
set "output_dir=output_videos"

REM 使用ffmpeg检测静音
ffmpeg -i "!video_path!" -af silencedetect=noise=-30dB:d=0.5 -f null - 2> "!silence_output!"

REM 创建输出目录
if not exist "!output_dir!" mkdir "!output_dir!"

REM 初始化变量
set /a "count=0"
set /a "split_duration=15*60" REM 15分钟转换为秒
set "last_split=0"

REM 读取静音检测结果并分割视频
for /f "tokens=2 delims=:" %%a in ('findstr "silence_start" "!silence_output!"') do (
    set /a "silence_start=%%a"
    set /a "duration=!silence_start!-!last_split!"
    if !duration! geq !split_duration! (
        REM 计算切分点并切割视频
        set /a "split_point=!last_split!+!split_duration!"
        ffmpeg -i "!video_path!" -ss !last_split! -to !split_point! -c copy "!output_dir!\output_part_!count!.mp4"
        set /a "count+=1"
        set "last_split=!split_point!"
    )
)

REM 处理最后一段视频
ffmpeg -i "!video_path!" -ss !last_split! -c copy "!output_dir!\output_part_!count!.mp4"

echo 完成视频切分。
endlocal
