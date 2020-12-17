import pandas as pd
import json
import folium

# 임시데이터
guname = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구',
          '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
trash_data = [2780, 773, 748, 884, 1496, 707, 1561, 1015, 1265, 485, 1294, 1091, 574, 962, 1930, 1062, 1464, 618, 2034,
              904, 1624, 1873, 1002, 671, 660]


def make_folium_map(guname, trash_data):
    geo_path = 'seoul_geo.json'
    geo_str = json.load(open(geo_path, encoding='utf-8'))

    df = pd.DataFrame({'구별': guname,
                       '배출량': trash_data,
                       })
    map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                     tiles='cartodbpositron')
    fmap = folium.Choropleth(geo_data=geo_str,
                             data=df,
                             columns=['구별', '배출량'],
                             fill_color='PuRd',  # puRd, YlGnBu
                             key_on='feature.properties.name').add_to(map)
    fmap.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=False)
    )

    map.save('../templates/recycle/foliummap.html')

make_folium_map(guname, trash_data)