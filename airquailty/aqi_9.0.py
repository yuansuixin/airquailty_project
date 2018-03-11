
import pandas as pd

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5)) # 前5个值
    # print(aqi_data[['City','AQI']]) # 传进去一个列表，就是代表多列
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 基本的统计
    print('AQI最大值：',aqi_data['AQI'].max())
    print('AQI最小值：',aqi_data['AQI'].min())
    print('AQI均值：',aqi_data['AQI'].mean())


    # 排序
    top_10 = aqi_data.sort_values(by=['AQI']).head(10) # 升序
    print('空气质量最好的10个城市：')
    print(top_10)

    # 后10
    bottom_10 = aqi_data.sort_values(by=['AQI']).tail(10)
    # top_10 = aqi_data.sort_values(by=['AQI'],ascending=False).head(10) # 降序
    print('空气质量最差的10个城市：')
    print(bottom_10)

    # 保存数据csv文件
    top_10.to_csv('top_10.csv',index=False) # 默认是带着索引号的
    bottom_10.to_csv('bottom_10.csv',index=False)


if __name__ == '__main__':
    main()












