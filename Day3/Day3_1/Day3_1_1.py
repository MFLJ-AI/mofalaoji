# 此设备：魔法老姬
# 开发时间：2025/6/30 9:27
import requests
from bs4 import BeautifulSoup

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 发送HTTP请求
url = 'https://movie.douban.com/top250'
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有电影项（限制前10个）
    movie_items = soup.find_all('div', class_='item')[:10]

    print("豆瓣电影Top250前十名：")
    for index, item in enumerate(movie_items, 1):
        # 提取电影标题（包含<span class="title">的标签）
        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            print(f"{index}. {title}")
else:
    print(f"请求失败，状态码: {response.status_code}")