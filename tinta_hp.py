#!/bin/python3
#victor.oliveira@gmx.com
import urllib.request
import xml.etree.ElementTree as ET
import argparse

def get_colors(xml):
    colors = dict()
    for i in xml[2]:
        name = i[0].text
        percentage = i[4].text
        colors.update({name : percentage})
    return colors

def get_xml(host):
    url = 'http://{}/DevMgmt/ProductUsageDyn.xml'.format(host)
    req = urllib.request.urlopen(url)
    raw_xml = req.read().decode()
    xml = ET.fromstring(raw_xml)
    return xml

parser = argparse.ArgumentParser(description='Retorna o nível de tinta das impressoras em rede da HP')
parser.add_argument('host', help='Endereço IP da impressora')
parser.add_argument('-t', '--tinta', help='Número da tinta', type=int)
args = parser.parse_args()

try:
    xml = get_xml(args.host)
    colors = get_colors(xml)
    if args.tinta or args.tinta == 0:
        colors = list(colors.items())[args.tinta]
        print('{}: {}%'.format(colors[0], colors[1]))
    else:
        for color in colors:
            print('{}: {}%'.format(color, colors[color]))
except IndexError:
    print('ERRO: Número da tinta incorreto')
except:
    print('ERRO: Não é uma impressora HP ou esta não é suportada')
