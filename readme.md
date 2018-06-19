### 直接运行
	python tracker.py
### 所需依赖
	自己试试吧，缺什么装什么！！ 哈哈
### 视频转换
	FFMPEG  -i  uploadfile/video/test.wmv -c:v libx264 -strict -2 -s 1280x720 -b 1000k uploadfile/mp4/test.mp4

	FFMPEG  -i  3.avi -c:v libx264 -strict -2 -s 720x480 -b 1000k 3.mp4

https://www.cnblogs.com/frost-yen/p/5848781.html

### 序列帧与视频的相互转换

把darkdoor.[001-100].jpg序列帧和001.mp3音频文件利用mpeg4编码方式合成视频文件darkdoor.avi：
	$ ffmpeg -i 001.mp3 -i darkdoor.%3d.jpg -s 1024x768 -author fy -vcodec mpeg4 darkdoor.avi

	ffmpeg  -i %4d.jpg -s 50x100 -vcodec mpeg4 darkdoor.avi

### 还可以把视频文件导出成jpg序列帧：

	$ ffmpeg -i bc-cinematic-en.avi example.%d.jpg
	
	ffmpeg -i "你是我的小呀小苹果儿.mp4" -r 1 -q:v 2 -f image2 image-3%d.jpeg
	
	ffmpeg -i b2.mp4 -q:v 2 -f image2 %4d.jpg

### 剪切视频
	ffmpeg -i 3.avi -ss 00:00:00 -t 00:00:06 -acodec copy -vcodec copy output.mp4
	ffmpeg -ss 00:00:00 -t 00:00:05 -i 3.avi -vcodec copy -acodec copy output1.mp4

### 截取从头开始的30s
ffmpeg -ss 00:00:00 -t 00:00:06 -i 3.avi -vcodec copy -acodec copy split.mp4
### 截取从30s开始的30s
ffmpeg -ss 00:00:30 -t 00:00:30 -i keyoutput.mp4 -vcodec copy -acodec copy split1.mp4
### 进行视频的合并
ffmpeg -f concat -i list.txt -c copy concat.mp4

