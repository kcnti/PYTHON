# Prog-11: Weather report (EP.2)
# 6330573721 Name Apichaya Mongkolphinyopas

import json
import math
    
#use data
def top_K_max_temp_by_region(data, K):
    # region = ['C', 'E', 'N', 'NE', 'S', 'W']
    # res = [x : [] for x in region]
    info = []
#    for i in data:
#        result[data[i]['city']['name']] = data[i]['list'][0]['main']['temp']
    for i in data:
        info.append([i, data[i]['list'][0]['main']['temp'], data[i]['city']['name'], data[i]['list'][0]['dt_txt']])
    # print(info)
    info.sort(key=lambda x:x[1], reverse=True)
    c, e, n, ne, s, w = 0, 0, 0, 0, 0, 0
    direct = {}
    for i in info:
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'C' and c < K:
            if 'C' in direct:    
                direct['C'].append(i)
                c+=1
            else:
                direct['C'] = i
                c+=1
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'E' and e < K:
            if 'E' in direct:    
                direct['E'].append(i)
                e+=1
            else:
                direct['E'] = i
                e+=1
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'N' and n < K:
            if 'N' in direct:    
                direct['N'].append(i)
                n+=1
            else:
                direct['N'] = i
                n+=1
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'NE' and ne < K:
            if 'NE' in direct:    
                direct['NE'].append(i)
                ne+=1
            else:
                direct['NE'] = i
                ne+=1
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'S' and s < K:
            if 'S' in direct:    
                direct['S'].append(i)
                s+=1
            else:
                direct['S'] = i
                s+=1
        if data[i[0]]['city']['name'] == i[2] and data[i[0]]['city']['region'] == 'W' and w < K:
            if 'W' in direct:    
                direct['W'].append(i)
                w+=1
            else:
                direct['W'] = i
                w+=1
    return direct

#use data
def average_temp_by_date(data, region):
    res = []
    average_temp = []
    k = 0
    temp_date = data['1149698']['list'][0]['dt_txt'].split()[0]
    for i in data:
        print(i)
        # print(data[i]['list'][k]['dt_txt'])
        # k+=1
        # print(data[i]['city']['region'])
        # print(data[i]['list'][14]['dt_txt'])
        
        for j in data[i]:
            if data[i]['city']['region'] == region:
                # print(data[i]['list'][k]['dt_txt'].split()[0] != temp_date)
                # print(res)
                try:
                    if data[i]['list'][k]['dt_txt'].split()[0] != temp_date:
                        res.append((temp_date, sum(average_temp)/len(average_temp)))
                        average_temp = []
                        temp_date = data[i]['list'][k]['dt_txt'].split()[0]
                    average_temp.append(data[i]['list'][k]['main']['temp'])
                    k+=1
                except:
                    k = 0
    return res

#use data_filtered
def max_rain_in_3h_periods(data, region, date):
    k = 0
    res = []
    zero = [0]
    three = [0]
    six = [0]
    nine = [0]
    twelve = [0]
    fifteen = [0]
    eighteen = [0]
    twenone = [0]

    if region == 'ALL':
        for i in data:
            # print(int(data[i]['list'][k]['dt_txt'].split()[1].split(':')[0]))
            # print((data[i]['list'][k]['rain']['3h']))
            if i['rain3h'] == None:
                continue
            # print(i['hour'], i['rain3h'])
            if int(i['hour']) == 0:
                zero.append(i['rain3h'])
            if int(i['hour']) == 3:
                three.append(i['rain3h'])
            if int(i['hour']) == 6:
                six.append(i['rain3h'])
            if int(i['hour']) == 9:
                nine.append(i['rain3h'])
            if int(i['hour']) == 12:
                twelve.append(i['rain3h'])
            if int(i['hour']) == 15:
                fifteen.append(i['rain3h'])
            if int(i['hour']) == 18:
                eighteen.append(i['rain3h'])
            if int(i['hour']) == 21:
                twenone.append(i['rain3h'])
    else:
        for i in data:
            # print(int(data[i]['list'][k]['dt_txt'].split()[1].split(':')[0]))
            if i['region'] == region:
                for i in data:
                    # print(int(data[i]['list'][k]['dt_txt'].split()[1].split(':')[0]))
                    # print((data[i]['list'][k]['rain']['3h']))
                    if i['rain3h'] == None:
                        continue
                    # print(i['hour'], i['rain3h'])
                    if int(i['hour']) == 0 and i['region'] == region:
                        zero.append(i['rain3h'])
                    if int(i['hour']) == 3 and i['region'] == region:
                        three.append(i['rain3h'])
                    if int(i['hour']) == 6 and i['region'] == region:
                        six.append(i['rain3h'])
                    if int(i['hour']) == 9 and i['region'] == region:
                        nine.append(i['rain3h'])
                    if int(i['hour']) == 12 and i['region'] == region:
                        twelve.append(i['rain3h'])
                    if int(i['hour']) == 15 and i['region'] == region:
                        fifteen.append(i['rain3h'])
                    if int(i['hour']) == 18 and i['region'] == region:
                        eighteen.append(i['rain3h'])
                    if int(i['hour']) == 21 and i['region'] == region:
                        twenone.append(i['rain3h'])
    res.append((0, max(zero)))
    res.append((3, max(three)))
    res.append((6, max(six)))
    res.append((9, max(nine)))
    res.append((12, max(twelve)))
    res.append((15, max(fifteen)))
    res.append((18, max(eighteen)))
    res.append((21, max(twenone)))
    return res

#use data_filtered
def AM_PM_weather_description_by_region(data, date):
    region = ['C', 'E', 'N', 'NE', 'S', 'W']
    res = {x : {'AM' : [], 'PM' : []} for x in region}

    for i in data:
        if i['date'] == date:
            res[i['region']][i['time_type']] += [i['description']]
    for i in res:
        for j in res[i]:
            res[i][j].sort()
    _res = {x : {'AM' : [], 'PM' : []} for x in region}
    for i in region:
        for j in ['AM', 'PM']:
            _res[i][j] = max(res[i][j], key=res[i][j].count)
    return _res

def most_varied_weather_provinces(data):
    province = {i['province'] : set([]) for i in data}
    for i in data:
        province[i['province']].add(i['description'])
    moody = [(i, len(province[i])) for i in province]
    _max = max(moody, key=lambda item: item[1])[1]

    res = set([])
    for i, j in moody:
        if j == _max:
            res.add(i)
    return res

# most_varied_weather_provinces(data)
def main():
    data = json.load(open('th_weather_39.json'))
# data["key"]["list"]["main"] access to information
#                    ["weather"]
#                    ["clouds"]
#                    ["wind"]
#            ["city"]["name"]
#                    ["region"]

#for i in data:
#    for j in data[i]['list']:
#        print(j['dt'])
#        break
#    break

    data_filtered = []
    for i in data:
        region = data[i]['city']['region']
        province = data[i]['city']['name']
        for weather in data[i]['list']:
            description = weather['weather'][0]['description']
            temp = weather['main']['temp']
            date, time = weather['dt_txt'].split()
            y, mon, d = [int(i) for i in date.split('-')]
            h, m, s = [int(i) for i in time.split(':')]
            if 'rain' in weather:
                rain = weather['rain']['3h']
            else:
                rain = None
            if h < 12:
                time_type = 'AM'
            else:
                time_type = 'PM'
            data_filtered += [
                                {
                                'region': region,
                                'province' : province,
                                'description' : description,
                                'temp' : temp,
                                'rain3h' : rain,
                                'year' : y,
                                'month' : mon,
                                'day' : d,
                                'hour' : h,
                                'mins' : m,
                                'sec' : s,
                                'date' : date,
                                'time' : time,
                                'time_type' : time_type,
                                'dt_txt' : weather['dt_txt']
                                }
                            ]
    # print(data_filtered)
    print(top_K_max_temp_by_region(data, 2))
    print()
    print(average_temp_by_date(data, 'W'))
    print()
    print(max_rain_in_3h_periods(data_filtered, 'ALL', '2021-04-07'))
    print()
    print(AM_PM_weather_description_by_region(data_filtered, '2021-04-09'))
    print()
    print(most_varied_weather_provinces(data_filtered))

main()