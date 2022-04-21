import json
import requests
import xmltodict
from dicttoxml import dicttoxml


def request_creator(x):
    address = x['address']
    address = create_add(address)
    format = x['output_format']
    url = 'https://maps.googleapis.com/maps/api/geocode/' + format \
        + '?address=' + address \
        + '&key=AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'
    return url


def create_add(s):
    text = s.replace(' ', '+').replace('#', '')
    return text


def getinfojson(x):
    z = request_creator(x)
    res = requests.get(z)
    coords = res.json()['results'][0]['geometry']['location']
    content = {'coordinates': coords, 'address': x['address']}
    return content


def getinfoxml(x):
    z = request_creator(x)
    res = requests.get(z)
    dict_data = xmltodict.parse(res.content)
    coords = dict(dict_data['GeocodeResponse']['result']['geometry'
                  ]['location'])
    content = {'address': x['address'], 'coordinates': coords}
    xml = dicttoxml(content, attr_type=False)
    return xml
