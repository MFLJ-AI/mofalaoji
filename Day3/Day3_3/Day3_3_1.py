# 此设备：魔法老姬
# 开发时间：2025/6/30 10:08
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import re
import traceback

# 论文列表
papers = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface",
    "The origin of planetary impactors in the inner solar system",
    "Deep learning based systems for crater detection: A review",
    "A preliminary study of classification method on lunar topography and landforms",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution",
    "Fast r-cnn",
    "You only look once: Unified, real-time object detection",
    "Attention is all you need",
    "End-to-end object detection with transformers"
]

# 存储BibTeX结果
bibtex_entries = []

# 连接到您当前使用的浏览器
try:
    print("尝试连接到您当前的浏览器...")
    # 使用Chrome DevTools Protocol连接到现有浏览器
    options = webdriver.ChromeOptions()
    options.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=options)
    print("✅ 成功连接到现有浏览器会话")
except Exception as e:
    print(f"❌ 无法连接到浏览器: {str(e)}")
    print("请确保您已经启动了支持远程调试的浏览器:")
    print("对于Chrome: 关闭所有Chrome实例，然后运行:")
    print('    chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_profile"')
    print("对于Edge: 关闭所有Edge实例，然后运行:")
    print('    msedge.exe --remote-debugging-port=9222 --user-data-dir="C:\temp\edge_profile"')
    traceback.print_exc()
    exit(1)

# 打开谷歌学术
try:
    print("正在访问谷歌学术...")
    driver.get("https://scholar.google.com")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    print("✅ 谷歌学术加载成功")
except Exception as e:
    print(f"❌ 无法打开谷歌学术: {str(e)}")
    driver.quit()
    exit(1)


# 随机延迟函数
def random_delay(min_t=1, max_t=3):
    time.sleep(random.uniform(min_t, max_t))


def has_captcha():
    """检查是否有验证码出现"""
    page_source = driver.page_source.lower()
    return any(text in page_source for text in ["captcha", "verify", "robot", "sorry", "检测到异常流量", "not a robot"])


def search_paper(paper_title):
    """搜索论文并返回是否成功"""
    try:
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()

        # 模拟人工输入 - 逐字符输入
        for char in paper_title:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.02, 0.08))

        random_delay(0.3, 0.7)
        search_box.submit()
        return True
    except Exception as e:
        print(f"搜索失败: {str(e)}")
        return False


def get_bibtex():
    """获取BibTeX引用"""
    try:
        # 尝试找到并点击引用按钮
        cite_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//a[contains(@class, "gs_or_cit") or contains(@class, "gs_nph") or contains(@aria-label, "Cite") or contains(text(), "引用")]')))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", cite_btn)
        cite_btn.click()
        random_delay(0.5, 1.5)

        # 选择BibTeX格式
        bibtex_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "BibTeX")]')))
        bibtex_option.click()
        random_delay(1, 2)

        # 获取BibTeX内容
        bibtex_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "pre"))).text

        # 清理BibTeX中的无效字符
        bibtex_content = re.sub(r'^\s*%.*?\n', '', bibtex_content, flags=re.MULTILINE)
        return bibtex_content.strip()
    except TimeoutException:
        return None
    except Exception as e:
        print(f"获取BibTeX时出错: {str(e)}")
        return None
    finally:
        # 尝试关闭引用窗口
        try:
            driver.back()
            random_delay(0.5, 1)
        except:
            try:
                close_btn = driver.find_element(By.XPATH,
                                                '//button[contains(@aria-label, "Close") or contains(@aria-label, "关闭")]')
                close_btn.click()
            except:
                pass


def return_to_home():
    """返回谷歌学术首页"""
    try:
        driver.get("https://scholar.google.com")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        return True
    except:
        try:
            driver.refresh()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            return True
        except:
            print("⚠️ 无法返回主页")
            return False


try:
    for i, paper in enumerate(papers):
        print(f"\n📄 处理论文 {i + 1}/{len(papers)}: {paper[:50]}{'...' if len(paper) > 50 else ''}")
        success = False

        for attempt in range(3):  # 最多尝试3次
            try:
                # 搜索论文
                if not search_paper(paper):
                    print(f"⚠️ 搜索失败，尝试 {attempt + 1}/3")
                    if not return_to_home():
                        driver.refresh()
                    random_delay(2, 3)
                    continue

                # 等待结果加载
                random_delay(2, 3)

                # 检查是否有验证码
                if has_captcha():
                    print("🛑 检测到人机验证，请手动完成验证后按回车继续...")
                    input("完成后按回车继续爬取...")
                    # 重新提交搜索
                    search_box = driver.find_element(By.NAME, "q")
                    search_box.submit()
                    random_delay(2, 3)

                # 获取BibTeX
                bibtex_content = get_bibtex()

                if bibtex_content:
                    bibtex_entries.append(bibtex_content)
                    print(f"✅ 成功获取BibTeX格式")
                    success = True
                    break
                else:
                    print(f"⚠️ 未找到论文或元素加载超时，尝试 {attempt + 1}/3")

            except Exception as e:
                print(f"❌ 处理论文时出错: {str(e)}")
                traceback.print_exc()

            # 返回主页进行下一次尝试
            if not return_to_home():
                driver.refresh()

        if not success:
            print(f"❌ 无法获取论文的BibTeX: {paper[:30]}...")
            bibtex_entries.append(f"% 未找到论文: {paper}")

        # 随机暂停防止被封
        nap = random.randint(5, 10)
        print(f"⏸️ 暂停 {nap} 秒防止被封...")
        time.sleep(nap)

except Exception as e:
    print(f"❌ 爬取过程中发生严重错误: {str(e)}")
    traceback.print_exc()
finally:
    # 保存结果到文件
    with open("scholar_bibtex.bib", "w", encoding="utf-8") as f:
        for entry in bibtex_entries:
            f.write(entry + "\n\n")

    print(f"\n✅ 完成! 已保存 {len(bibtex_entries)} 篇论文的BibTeX到 scholar_bibtex.bib")

    # 不要关闭浏览器，保持它打开
    print("浏览器保持打开状态")