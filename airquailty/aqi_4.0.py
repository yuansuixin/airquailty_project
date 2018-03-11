"""
功能：AQI的计算
"""
import json
import csv
import os

def process_json_file(filepath):
    with open(filepath,mode='r',encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    with open(filepath,mode='r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))




def main():
    filepath = input('请输入文件名称：')

    filename ,file_txt = os.path.splitext(filepath)

    if file_txt == '.json':
        process_json_file(filepath)
    elif file_txt == '.csv':
        process_csv_file(filepath)
    else:
        print('这是一个不支持的文件名称。')




if __name__ == '__main__':
    main()












