import requests
import os
import time

if __name__ == '__main__':
    if not os.path.exists('./img'):
        os.makedirs('./img')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    hero_list = requests.get(url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js',
                             headers=headers).json().get('hero')
    for hero in hero_list:
        hero_id = hero['heroId']
        hero_name = hero['name']
        hero_title = hero['title']

        img_url = './img/' + hero_name + '-' + hero_title
        if not os.path.exists(img_url):
            os.makedirs(img_url)
        url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/%d.js' % int(hero_id)
        skins = requests.get(url=url, headers=headers).json().get('skins')
        for skin in skins:
            image_url = skin['mainImg']
            if image_url != '':
                image_name = skin['name']
                time.sleep(1)
                image_data = requests.get(url=image_url, headers=headers).content
                img_path = img_url + '/ ' + image_name + '.jpg'
                with open(img_path, 'wb') as f:
                    f.write(image_data)
                    print(image_name, '>>> 下载完成！！！')
