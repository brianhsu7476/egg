from PIL import Image

def process_image(image_path, output_path, p):
	# 開啟圖片
	img = Image.open(image_path).convert("RGBA")
	width, height = img.size
	pixels = img.load()
	
	# 創建輸出圖片
	output_img = Image.new("RGBA", (width, height))
	output_pixels = output_img.load()
	
	T=60
	y0=(height+T)*p-T

	for y in range(height):
		for x in range(width):
			# 獲取像素值 (R, G, B, A)
			pixel = pixels[x, y]
			x0=x%(T*2)
			if x0//T==0:
				y1=y0+x0
			else:
				y1=y0+T*2-x0
			if pixel[3] > 0 and y>y1:  # 如果非透明
				output_pixels[x, y] = (255, 255, 255, 255)	# 設為白色
				# print(f"座標 ({x}, {y}): {pixel}")  # 列印座標與像素值
			else:
				output_pixels[x, y] = pixel  # 保留透明像素
	
	# 儲存輸出圖片
	output_img.save(output_path)

# 使用範例
input_image = "arctan.png"	 # 輸入圖片路徑

for i in range(61):
	process_image(input_image, "egg"+str(i)+".png", i/60)
	print(i)

