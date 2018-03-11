"""
功能：AQI的计算
"""
import json


def process_json_file(filepath):
    f = open(filepath,mode='r',encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    # filepath = input('请输入json文件名称：')
    filepath = 'beijing_aqi.json'
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    # print(city_list)
    top5_list = city_list[:5]

    f = open('top5_aqi.json',mode='w',encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()












