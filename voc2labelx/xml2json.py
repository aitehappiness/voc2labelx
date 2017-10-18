# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import sys


def xml2json(xmlname):
    result = {
        'ops': 'download()',
        'type': 'image',
        'label': {'detect': {'general_d': {'bbox': []}}},
        'source_url': ''
    }

    DOMTree = xml.dom.minidom.parse(xmlname)
    collection = DOMTree.documentElement

    imgname = str(collection.getElementsByTagName("filename")[0].childNodes[0].data)
    result['url'] = imgname

    objects = collection.getElementsByTagName("object")
    detections = []
    for object in objects:
        bndbox = {}
        class_name = str(object.getElementsByTagName('name')[0].childNodes[0].data)
        xmin = str(object.getElementsByTagName('xmin')[0].childNodes[0].data)
        ymin = str(object.getElementsByTagName('ymin')[0].childNodes[0].data)
        xmax = str(object.getElementsByTagName('xmax')[0].childNodes[0].data)
        ymax = str(object.getElementsByTagName('ymax')[0].childNodes[0].data)
        bndbox['class'] = class_name
        bndbox['pts'] = [
            [xmin, ymin],
            [xmax, ymin],
            [xmax, ymax],
            [xmin, ymax]
        ]
        detections.append(bndbox)
    result['label']['detect']['general_d']['bbox'] = detections

    return result


if __name__ == '__main__':
    xmlname = sys.argv[1] if len(sys.argv) > 1 else 'annotations-test.xml'
    label = xml2json(xmlname)
    print label

    print 'Done'