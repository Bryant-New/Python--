from MyQR import myqr
import os

myqr.run(
    words='https://github.com/Bryant-New',
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平,范围：L、M、Q、H,从左到右依次升高
    picture='灌篮高手.gif',  # 图片所在目录，可以是动图
    contrast=1.0,  # 调节图片对比度，1.0表示原图片，默认为1.0
    colorized=True,  # 黑白False 彩色True
    brightness=1.0,  # 用于调节图片亮度
    save_name='Python.gif',
)