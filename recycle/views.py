from django.shortcuts import render
import pandas as pd
import json
import folium
import datetime
from .models import Machine, Partner, BottleClass, Bottle, RUser

def chart(request):
    return render(request, 'recycle/chart.html')

def table(request):

    return render(request, 'recycle/table.html')

def machine_list(request):
    queryset = Machine.objects.all().order_by('-class1_full_rate')

    m_list = []

    for m_data in queryset:
        m_list.append({
            'id': m_data.id,
            'local1': m_data.local1,
            'local2': m_data.local2,
            'class1': m_data.class1_full_rate*20,
            'class2': m_data.class2_full_rate*20,
            'class3': m_data.class3_full_rate*20,
            'partner': m_data.partner.manager,
            'tel': m_data.partner.tel,
        })

    context = {
        "m_list" : m_list,
    }

    return render(request, 'recycle/machine_list.html', context)

def machine_info(request):
    pk = request.GET.get("pk")
    queryset = Bottle.objects.filter(machine_id=pk).order_by('datetime')
    m_queryset = Machine.objects.filter(id=pk)

    for m_data in m_queryset:
        class1 = m_data.class1_full_rate
        class2 = m_data.class2_full_rate
        class3 = m_data.class3_full_rate
        lat = m_data.lat
        lng = m_data.lng

    b_list = []
    total_mile = 0
    pie_data = [0,0,0]
    # 1 : 130원  4:10원  9:5원  12:100원 14:5원 15:5원
    # 1: 맥주병(1) 2:베지(2) 3: 쓰-베지(3)
    # 4: 유리병(2) 5:쓰-유리병(3) 6:empty(3)
    # 7: 유리잔(3) 8:쓰-유리잔(3) 9:투명드링크병(2)
    # 10: 쓰-투명드링크병(3) 11: 화장병(3) 12:소주(1)
    # 13: 갈색드링크병(2) 14:와인병(2) 15:쓰-와인병(3)
    for b_data in queryset:
        total_mile += b_data.bottle_c.point
        if b_data.bottle_c.recycle_class == 1:
            pie_data[0] += 1
        elif b_data.bottle_c.recycle_class == 2:
            pie_data[1] += 1
        else:
            pie_data[2] += 1

        b_list.append({
            'datetime': b_data.datetime,
            'b_class': b_data.bottle_c.bottle_class,
            'r_class' : b_data.bottle_c.recycle_class,
            'mile': b_data.bottle_c.point,
            'image': b_data.image,
            'user': b_data.rUser.nickname,
        })

    context = {
        "id" : pk,
        "b_list" : b_list,
        "total_mile":total_mile,
        "pie_data":pie_data,
        "class1" : class1 * 20,
        "class2": class2 * 20,
        "class3": class3 * 20,
        "lat" : lat,
        "lng" : lng,

    }
    return render(request, 'recycle/machine_info.html', context)

def partner_list(request):
    p_list = Partner.objects.all()

    context = {
        "p_list" : p_list,
    }
    return render(request, 'recycle/partner_list.html', context)

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
    mile = 14500
    bottle_earn = 62150
    total_earn = bottle_earn - mile

    # 병
    gongb = 5423
    yurib = 12341
    trashb = total_trash - gongb - yurib

    # 주간 배출량
    today = datetime.date.today()

    week_list = []
    week_trash_data = [28321, 25442, 23332, 26345, 25886, 30412, total_trash]

    for i in range(6, -1, -1):
        prev_day = today - datetime.timedelta(days=i)
        p_day = prev_day.strftime("%m-%d")
        week_list.append(p_day)



    context = {
        "bar_data": [mile, bottle_earn, total_earn],
        "mile" : mile,
        "total_earn" : total_earn,
        "total_trash" : total_trash,
        "pie_data": [gongb, yurib, trashb],
        "area_data_day":week_list,
        "area_data_trash" : week_trash_data,
    }
    return render(request, 'recycle/index.html', context)



