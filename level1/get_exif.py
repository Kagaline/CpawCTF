import argparse
from pprint import pprint
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def load_exif(path):
    """load exif from image"""
    ifd_dict = {}
    with Image.open(path) as im:
        exif = im.getexif()
    # {タグID: 値}の辞書を{タグ名: 値}の辞書に変換
    ifd_dict["Zeroth"] = {TAGS[tag_id]: value for tag_id, value in exif.items()}
    ifd_dict["Exif"] = {
        TAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8769).items()
    }
    ifd_dict["GPSInfo"] = {
        GPSTAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8825).items()
    }
    return ifd_dict, exif


def main():
    """main"""
    parser = argparse.ArgumentParser(description="Argument Parser")

    parser.add_argument("image_file", help="image file path")

    args = parser.parse_args()

    ifd_dict, _ = load_exif(args.image_file)

    pprint(ifd_dict)


if __name__ == "__main__":
    main()
