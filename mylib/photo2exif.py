from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import urllib.request


def getExif(file):
    image = Image.open(file)
    exif = image._getexif()
    if exit is None:
        return

    exif_data = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)

        if tag == "GPSInfo":
            gps_data = {}
            for t in value:
                gps_tag = GPSTAGS.get(t,t)
                gps_data[gps_tag] = value[t]

            exif_data[tag] = gps_data
        else:
            exif_data[tag] = value

    return exif_data

def getDeg(data):
    d = float(data[0][0]) / float(data[0][1])
    m = float(data[1][0]) / float(data[1][1])
    s = float(data[2][0]) / float(data[2][1])
    return d + (m / 60.0) + (s/3600.0)

def getGPS(data):
    lat = getDeg(data['GPSLatitude'])
    lat_ref = data['GPSLatitudeRef']
    if lat_ref != 'N':
        lat = 0 - lat
    lon = getDeg(data['GPSLongitude'])
    lon_ref = data['GPSLongitudeRef']
    if lon_ref != 'E':
        lon = 0 - lon
    return lat, lon

def getMapUrl(data):
    (lat, lon) = getGPS(data['GPSInfo'])
    url = 'http://maps.google.co.jp/maps?q=' + str(lat) + ',' + str(lon)
    return url

if __name__ == '__main__':
    # 画像参考: http://www.ksky.ne.jp/~yamama/jpggpsmap/sample/sample.htm
    # ローカルに画像ファイルがある場合こっち
    # file = 'sample_photo/sample_saitama.jpg'
    # Web上の画像を使う場合こっち
    url = 'http://www.ksky.ne.jp/~yamama/jpggpsmap/sample/AkihabaraKousaten.JPG'
    file = urllib.request.urlopen(url)
    data = getExif(file)
    for i, v in data.items():
        print(i, v)
    map_url = getMapUrl(data)
    print(map_url)