from django.shortcuts import render
import pandas as pd
import json
import folium
from .models import Machine, Partner, BottleClass, Bottle

def chart(request):
    return render(request, 'recycle/chart.html')

def table(request):

    return render(request, 'recycle/table.html')

def machine_list(request):
    queryset = Machine.objects.all().order_by('class1_full_rate')

    m_list = []

    for m_data in queryset:
        m_list.append({
            'id':m_data.id,
            'local1': m_data.local1,
            'local2': m_data.local2,
            'class1' : m_data.class1_full_rate*20,
            'class2': m_data.class2_full_rate*20,
            'class3': m_data.class3_full_rate*20,
            'partner':m_data.partner.manager,
        })

    context = {
        "m_list" : m_list,
    }

    return render(request, 'recycle/machine_list.html', context)

def partner_list(request):

    return render(request, 'recycle/partner_list.html')

def foliummap(request):

    return render(request, 'recycle/foliummap.html', None)

def index(request):
    # 지도
    geo_path = 'recycle/seoul_geo.json'
    geo_str = json.load(open(geo_path, encoding='utf-8'))

    # 임시데이터
    guname = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구',
              '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
    trash_data = [2780, 773, 748, 884, 1496, 707, 1561, 1015, 1265, 485, 1294, 1091, 574, 962, 1930, 1062, 1464, 618,
                  2034,
                  904, 1624, 1873, 1002, 671, 660]

    total_trash = sum(trash_data)

    def make_folium_map(guname, trash_data):
        df = pd.DataFrame({'구별': guname,
                           '배출량': trash_data,
                           })
        map = folium.Map(location=[37.5602, 126.982], zoom_start=10,
                         tiles='cartodbpositron')
        fmap = folium.Choropleth(geo_data=geo_str,
                                 data=df,
                                 columns=['구별', '배출량'],
                                 fill_color='PuRd',  # puRd, YlGnBu
                                 key_on='feature.properties.name').add_to(map)
        fmap.geojson.add_child(
            folium.features.GeoJsonTooltip(['name'], labels=False)
        )

        map.save('templates/recycle/foliummap.html')

    make_folium_map(guname, trash_data)

    # 수익
    mile = 10000
    bottle_earn = 30000
    total_earn = bottle_earn - mile

    gongb = 5423
    yurib = 12341
    trashb = total_trash - gongb - yurib

    context = {
        "bar_data": [mile, bottle_earn, total_earn],
        "mile" : mile,
        "total_earn" : total_earn,
        "total_trash" : total_trash,
        "pie_data": [gongb, yurib, trashb]
    }
    return render(request, 'recycle/index.html', context)



