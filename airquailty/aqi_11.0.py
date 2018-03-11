
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5)) # 前5个值
    # print(aqi_data[['City','AQI']]) # 传进去一个列表，就是代表多列
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())


    # 数据清洗
    # 只保留AQi>0的数据
    # filter_condition = aqi_data['AQI']>0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI']>0]


    # 基本的统计
    print('AQI最大值：',clean_aqi_data['AQI'].max())
    print('AQI最小值：',clean_aqi_data['AQI'].min())
    print('AQI均值：',clean_aqi_data['AQI'].mean())


    # 排序
    # 数据可视化,折线图
    top_50 = clean_aqi_data.sort_values(by=['AQI']).head(50)  # 升序
    top_50.plot(kind='line', x='City', y='AQI', title='空气质量最好的50个城市',
                figsize=(20, 10),grid=True)
    x = range(len(aqi_data.head(50)['City']))
    plt.xticks(x,aqi_data.head(50)['City'],rotation=90) # 设置横坐标的显示城市
    plt.savefig('top50_aqi_bar.png')
    plt.show()



if __name__ == '__main__':
    main()












