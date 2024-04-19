import requests

# 图片的url
url = 'https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png'

# 发送请求并获取图片数据
response = requests.get(url)
name = "wallhaven-6do9zx.png"
image = "D:/wallheaven/test/"+name;
# 将图片数据写入本地文件
with open(image, 'wb') as file:
    file.write(response.content)

print('图片下载完成')
if __name__ == "__main__":
    url = 'https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png'

