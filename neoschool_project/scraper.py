from bs4 import BeautifulSoup
import requests
import os
import time
def main():
    folder_name="news_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    url = 'https://news.cnr.cn/native/gd/kx/20260403/t20260403_527572914.shtml'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}\
    print("Retrieving data from China National Radio website...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('h1')
            title = title_tag.get_text(strip=True) if title_tag else "Unknown Title"
            content_div = soup.find('div', class_='article-content') or soup.find('div', id='content')
            if content_div:
                paragraphs = content_div.find_all('p')
            else:
                paragraphs = soup.find_all('p')
            content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            file_path = os.path.join(folder_name, "food_safety_news.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"Title: {title}\n\n")
                file.write(content)
            print(f"Data saved to {file_path}")
            print('✅ACCESS!')
    except requests.exceptions.RequestException as e:
        print(f"❌Error retrieving data: {e}")
    time.sleep(3)
if __name__ == "__main__":
    main()