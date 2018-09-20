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
### 截取视频图像
ffmpeg -i input.mp4 -r 1 -q:v 2 -f image2 pic-%03d.jpeg 

-r 表示每一秒几帧 

-q:v表示存储jpeg的图像质量，一般2是高质量。 

如此，ffmpeg会把input.mp4，每隔一秒，存一张图片下来。假设有60s，那会有60张。


### 每隔1s就抓一帧
可以设置开始的时间，和你想要截取的时间。 

ffmpeg -i input.mp4 -ss 00:00:20 -t 10 -r 1 -q:v 2 -f image2 pic-%03d.jpeg 

-ss 表示开始时间 

-t 表示共要多少时间。 

如此，ffmpeg会从input.mp4的第20s时间开始，往下10s，即20~30s这10秒钟之间，每隔1s就抓一帧，总共会抓10帧。
	
## References
- Action-Decision Networks for Visual Tracking with Deep Reinforcement Learning (CVPR2017) : http://openaccess.thecvf.com/content_cvpr_2017/papers/Yun_Action-Decision_Networks_for_CVPR_2017_paper.pdf
- ADNet Implmentation in Matlab : https://github.com/hellbell/ADNet/
- ADNet Implmentation in Python ：https://github.com/sseung0703/ADNet-tensorflow

