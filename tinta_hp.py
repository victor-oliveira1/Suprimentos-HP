#!/bin/python3
#victor.oliveira@gmx.com
import urllib.request
import xml.etree.ElementTree as ET
import argparse

def get_colors(host):
    url = 'http://{}/DevMgmt/ProductUsageDyn.xml'.format(host)
    req = urllib.request.urlopen(url)
    raw_xml = req.read().decode()
    xml = ET.fromstring(raw_xml)
    colors = dict()
    for root in xml:
        if 'ConsumableSubunit' in root.tag:
            for ink in root:
                for item in ink:
                    if 'MarkerColor' in item.tag:
                        name = item.text
                    elif 'ConsumableRawPercentageLevelRemaining' in item.tag:
                        percentage = item.text
                colors.update({name : percentage})
    return colors

parser = argparse.ArgumentParser(description='Retorna o nível de tinta das impressoras em rede da HP')
parser.add_argument('host', help='Endereço IP da impressora')
parser.add_argument('-t', '--tinta', help='Número da tinta', type=int)
args = parser.parse_args()

try:
    colors = get_colors(args.host)
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
