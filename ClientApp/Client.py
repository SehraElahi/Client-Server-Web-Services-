from flask import Flask, request, session, render_template
from decimal import Decimal
import requests
import datetime
import dateutil.parser

app = Flask(__name__)
app.secret_key = 'b"1:\x98\xe6\xb2\x06W\x94\xdf\x86\xe8'

########################################################################################
#obtaining results from own server
@app.route('/')
def index():

    response1 = requests.get('http://127.0.0.1:5050')
    # r_time1 = str(response1.elapsed.total_seconds())
    data_in_json_for_country = response1.json()
    #parsing the data to get the country needed
    session['country_of_travel'] = str(data_in_json_for_country['HotEUCountries'][0]['country'])
    session['country1'] = str(data_in_json_for_country['HotEUCountries'][1]['country'])
    session['country2'] = str(data_in_json_for_country['HotEUCountries'][2]['country'])
    session['country3'] = str(data_in_json_for_country['HotEUCountries'][3]['country'])
    session['country4'] = str(data_in_json_for_country['HotEUCountries'][4]['country'])
    session['temp1'] = str(data_in_json_for_country['HotEUCountries'][0]['average'])
    session['temp2'] = str(data_in_json_for_country['HotEUCountries'][1]['average'])
    session['temp3'] = str(data_in_json_for_country['HotEUCountries'][2]['average'])
    session['temp4'] = str(data_in_json_for_country['HotEUCountries'][3]['average'])
    session['temp5'] = str(data_in_json_for_country['HotEUCountries'][4]['average'])
    # return r_time1
    #session['test'] = "hehehehehe"
    return render_template('index.html', country = session['country_of_travel'], c1 = session['country1'], c2 = session['country2'], c3 = session['country3'], c4 = session['country4'], t1 = session['temp1'],
    t2 = session['temp2'], t3 = session['temp3'], t4 = session['temp4'], t5 = session['temp5'])

########################################################################################
#obtain results from 2nd server
@app.route('/travel')
def travel():

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    #passing session['country_of_travel'] to the api below
    querystring = {"query":session['country_of_travel']}

    headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "bc080d61ffmsh37ba27d1a669acbp1aedb0jsn9d84509016dc"
    }

    response2 = requests.get(url, headers=headers, params=querystring)
    # r_time2 = str(response2.elapsed.total_seconds())
    data_in_json_for_city = response2.json()
    session['city_of_travel'] = str(data_in_json_for_city['Places'][1]['PlaceName'])

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/UK/GBP/en-UK/LHR-sky/LCA-sky/anytime"

    querystring = {"inboundpartialdate":"2020-01-30"}

    headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "bc080d61ffmsh37ba27d1a669acbp1aedb0jsn9d84509016dc"
    }
    response3 = requests.get(url, headers=headers, params=querystring)
    flight_data_json = response3.json()

    price1 = str(flight_data_json['Quotes'][0]['MinPrice'])
    price2 = str(flight_data_json['Quotes'][1]['MinPrice'])
    price3 = str(flight_data_json['Quotes'][2]['MinPrice'])
    date1 = str(flight_data_json['Quotes'][0]['OutboundLeg']['DepartureDate'])
    date2= str(flight_data_json['Quotes'][1]['OutboundLeg']['DepartureDate'])
    date3 = str(flight_data_json['Quotes'][2]['OutboundLeg']['DepartureDate'])
    carrier1 = str(flight_data_json['Carriers'][0]['Name'])
    carrier2 = str(flight_data_json['Carriers'][1]['Name'])
    carrier3 = str(flight_data_json['Carriers'][2]['Name'])
    d1 = dateutil.parser.parse(date1)
    d11 = d1.strftime('%d/%m/%Y')
    d2 = dateutil.parser.parse(date2)
    d22 = d2.strftime('%d/%m/%Y')
    d3 = dateutil.parser.parse(date3)
    d33 = d3.strftime('%d/%m/%Y')

    # return r_time2
    # return session['city_of_travel']
    #str(price1), str(date1), str(carrier1)
    return render_template('travel.html', place = session['city_of_travel'], price1 = price1, price2 = price2, price3 = price3, date1=d11,
    date2 = d22, date3 =d33, carrier1=carrier1, carrier2=carrier2, carrier3=carrier3, country = session['country_of_travel'])

########################################################################################
#obtain results from 3rd server
@app.route('/weather')
def weather():
    #passing session['city_of_travel'] to the api below
    response4 = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+session['city_of_travel']+'&mode=json&units=metric&appid=04191c36eec82c06b2b4306972f6f714')
    # r_time4 = str(response4.elapsed.total_seconds())

    data_in_json_for_weather = response4.json()
    temp = float(data_in_json_for_weather['main']['temp'])

    response5 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=leeds,uk&mode=json&units=metric&appid=04191c36eec82c06b2b4306972f6f714')
    uk_weather_data = response5.json()
    uk_temp = float(uk_weather_data['main']['temp'])
    # return str(temp)
    # return r_time4
    return render_template('weather.html', place = session['city_of_travel'], temp = temp, temp_uk = uk_temp)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
