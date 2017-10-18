# -*- coding: UTF-8 -*-

from os.path import join, isfile, basename
from os import listdir
from xml2json import xml2json
import json
import argparse


def parse2labelx(vocpath, domain, skip_class=''):
    vocpath = vocpath.rstrip('/')
    print 'start: jsonlist will be saved to', basename(vocpath)+'.detect.json'
    annotations_path = join(vocpath, 'Annotations')

    xmllist = [x
               for x in listdir(annotations_path)
               if isfile(join(annotations_path, x)) and not x[0] == '.']
    jsonlist = []

    for xml in xmllist:
        label = xml2json(join(annotations_path, xml))
        label['url'] = 'http://%s/%s' % (domain, label['url'])

        skip_item = []
        for item in label['label']['detect']['general_d']['bbox']:
            if item['class'] == skip_class:
                skip_item.append(item)
        for item in skip_item:
            label['label']['detect']['general_d']['bbox'].remove(item)

        if label['label']['detect']['general_d']['bbox']:
            jsonlist.append(label)

    if jsonlist:
        r = '\n'.join([json.dumps(item) for item in jsonlist])
        jsonlist_name = basename(vocpath)

        with open(jsonlist_name+'.detect.json', 'w+') as f: f.write(r)
    else:
        print 'valid annotations empty'

    print 'success'


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='voc2labelx')
    parser.add_argument('--vocpath',
                        dest='vocpath',
                        help='voc train data path',
                        type=str)

    parser.add_argument('--domain',
                        dest='domain',
                        help='domain & http://domain/imgname should be available',
                        type=str)

    parser.add_argument('--skip',
                        dest='skip_class',
                        default='',
                        help='skip class',
                        type=str)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()

    parse2labelx(args.vocpath, args.domain, args.skip_class)