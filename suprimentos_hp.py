#!/bin/python3
#victor.oliveira@gmx.com
import urllib.request
import xml.etree.ElementTree as ET
import argparse

def get_colors(host):
    colors = dict()
    try:
        url = 'http://{}/DevMgmt/ProductUsageDyn.xml'.format(host)
        req = urllib.request.urlopen(url)
        raw_xml = req.read().decode()
        xml = ET.fromstring(raw_xml)
        for root in xml:
            if 'ConsumableSubunit' in root.tag:
                for ink in root:
                    for item in ink:
                        if 'MarkerColor' in item.tag:
                            name = item.text
                        elif 'ConsumableRawPercentageLevelRemaining' in item.tag:
                            percentage = item.text
                    colors.update({name : percentage})
    except:
        url = 'http://{}/index.htm?cat=info&page=printerInfo'.format(host)
        req = urllib.request.urlopen(url)
        page = req.read().decode()
        if 'blackink=' in page:
            black_index = page.find('blackink=')
            black_level = page[black_index:black_index + 11].split('=')[1].split(';')[0]
        if 'colorink=' in page:
            color_index = page.find('colorink=')
            color_level = page[color_index:color_index + 11].split('=')[1].split(';')[0]
        colors.update({'Black' : black_level,
                       'Tricolor' : color_level})
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
