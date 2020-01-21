'''
图像处理：
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow
可以实现图像压缩和图像处理等各种操作

image.show() ------ 显示图片
ImageFilter 是滤镜效果要用的
'''

from PIL import Image, ImageFilter

image = Image.open('G:\\照片\\1533054321647.jpg')     # 图片位置


# 1.图片的格式，大小，颜色
'''
print(image.format, image.size, image.mode) 
image.show()                                
'''

# 2.剪裁图片
'''
rect = 80, 20, 310 360
image.crop(rect).show()
'''

# 3.生成缩略图
'''
size = 128, 128
image.thumbnail(size)
'''

# 4.旋转和翻转
'''
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
'''

# 5.操作像素
'''
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y),(128, 128, 128))
'''

# 6.滤镜效果
'''
image.filter(ImageFilter.CONTOUR).show()
'''
# 注意：------这里图片的格式决定能不能进行滤镜效果