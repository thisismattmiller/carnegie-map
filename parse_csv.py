from dateutil import parser
import json
import time

inflationCalc = {
	1913: 24.76,
	1914: 24.51,
	1915: 24.27,
	1916: 22.49,
	1917: 19.15,
	1918: 16.23,
	1919: 14.17,
	1920: 12.26,
	1921: 13.69,
	1922: 14.59,
	1923: 14.33,
	1924: 14.33,
	1925: 14.01
}

total = 0

with open('data.csv') as f:

	datas = []
	for line in f:

		data = line.strip().split('\t')


		if data[1] != '':
			date = data[1]
		else:
			date = data[0]	 
		



		timestamp = int(parser.parse(date).timestamp())
		year = parser.parse(date).year

		cash = data[2].replace('$','').replace(',','')
		if cash == '' or cash =='—':
			cash = '0'

		cash = int(cash)

		updawg = inflationCalc[1913] if year not in inflationCalc else inflationCalc[year]

		inflation = int(cash*updawg)
		total=total+inflation
		try:
			lat, lng = data[3].split(',')
		except:
			continue

		data = {
			"date" : date,
			"time" : timestamp,
			"money" : cash,
			"lat" : lat.strip(),
			"lng" : lng.strip(),
			"1913_inflation" : inflation
		}
		datas.append(data)

	

datas.sort(key = lambda x: x['time'])
for d in datas:
	print(d)

json.dump(datas,open('data.json','w'))		



