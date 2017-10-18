# voc2labelx
转换voc数据集格式为符合labelx系统输入格式的jsonlist

## Usage
### format
same with voc(2007/2012) datasets
```
<vocdirname>
├── Annotations
│   ├── 000000.xml
│   ├── 000001.xml
│   ├── 000002.xml
│   └── ...
├── ImageSets
│   ├── Main
│   │   ├── test.txt
│   │   ├── train.txt
│   │   ├── trainval.txt
│   │   └── val.txt
├── JPEGImages
│   ├── 000000.jpg
│   ├── 000001.jpg
│   ├── 000002.jpg
│   └── ...
```

### condition
all following image in \<vocdirname\>/JPEGImages should be available
```
http://<domain>/<vocdirname>/JPEGImages/000000.jpg
http://<domain>/<vocdirname>/JPEGImages/000001.jpg
http://<domain>/<vocdirname>/JPEGImages/000002.jpg
...
```

### convert voc data to labelx jsonlist
```python
cd <voc2labelx>/voc2labelx

python parse2labelx.py --vocpath /path/to/voc/data --domain domain

python parse2labelx.py --vocpath /path/to/voc/data --domain domain --skip 'skip_label'
```

