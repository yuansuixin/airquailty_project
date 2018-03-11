import requests



def get_html_text(url):
    """
    返回url的文本
    :param url:
    :return:
    """
    r = requests.get(url,timeout=30)
    print(r.status_code)
    return r.text


def main():
    city_pinyin = input('请输入城市的拼音：')
    url = 'http://pm25.in/'+city_pinyin
    url_text = get_html_text(url)
    # print(url_text)  # 显示的就是网页的html内容

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index+2
    aqi_value = url_text[begin_index:end_index]
    print('空气质量为：{}'.format((aqi_value)))


if __name__ == '__main__':
    main()












