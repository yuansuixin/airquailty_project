"""
功能：AQI的计算
"""
import json
import csv

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


    lines = []
    #第一行数据，列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))


    f = open('aqi.csv','w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()












