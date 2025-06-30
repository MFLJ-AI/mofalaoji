# 此设备：魔法老姬
# 开发时间：2025/6/30 9:53
import requests
from lxml import etree
import os
import time
from urllib.parse import urljoin


def download_images():
    # 创建保存图片的文件夹
    if not os.path.exists('bian_images'):
        os.makedirs('bian_images')

    # 配置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://pic.netbian.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive'
    }

    # 目标URL
    url = "https://pic.netbian.com/"

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers)
        print(f"响应状态码: {response.status_code}")

        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return

        # 解析HTML内容
        html = etree.HTML(response.content)

        # 查找所有图片项 - 使用XPath定位缩略图
        image_items = html.xpath('//div[@class="slist"]/ul/li')[:10]

        if not image_items:
            print("未找到图片信息，可能是页面结构变化")
            return

        print(f"共找到 {len(image_items)} 张图片，开始下载...")

        # 提取并下载图片
        for idx, item in enumerate(image_items, 1):
            try:
                # 获取图片详情页链接
                detail_url = item.xpath('./a/@href')[0]
                full_detail_url = urljoin(url, detail_url)

                # 请求图片详情页
                detail_response = requests.get(full_detail_url, headers=headers)
                detail_html = etree.HTML(detail_response.content)

                # 提取高清图片URL
                img_src = detail_html.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
                full_img_url = urljoin(url, img_src)

                # 提取图片标题
                img_title = detail_html.xpath('//div[@class="photo-hd"]/h1/text()')[0].strip()

                # 下载图片
                img_data = requests.get(full_img_url, headers=headers).content

                # 生成文件名（替换非法字符）
                safe_title = "".join(
                    [c for c in img_title if c.isalpha() or c.isdigit() or c in [' ', '_', '-']]).rstrip()
                filename = f"bian_images/{idx}_{safe_title}.jpg"

                # 保存图片
                with open(filename, 'wb') as f:
                    f.write(img_data)

                print(f"已下载图片 {idx}: {img_title}")

                # 添加延时避免请求过快
                time.sleep(1)

            except Exception as e:
                print(f"下载第{idx}张图片时出错: {str(e)}")

        print("图片下载完成！请查看 'bian_images' 文件夹")

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    download_images()