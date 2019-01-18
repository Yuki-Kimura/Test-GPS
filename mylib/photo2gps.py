from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


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

if __name__ == '__main__':
    file = 'sample_photo/sample_saitama.jpg'
    data = getExif(file)
    for i, v in data.items():
        print(i, v)
