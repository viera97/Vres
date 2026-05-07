import ffmpeg
import os
import sys
import argparse

def calres(x, y):
    if x >= 7680 and y >= 4320:
        return "8k"
    elif x >= 3840 and y >= 2160:
        return "4k"
    elif x >= 2560 and y >= 1440:
        return "2k"
    elif x >= 1920 and y >= 1080:
        return "FHD"
    elif x >= 1280 and y >= 720:
        return "HD"
    elif x >= 854 and y >= 480:
        return "SD"
    else:
        return "SD"

video_formats = ["avi","mpg","mp4","mkv","vob"]

parser = argparse.ArgumentParser(description='Analize videos resolution')
parser.add_argument('folder', nargs='?', default='.', help='Target folder')
parser.add_argument('-r', '--recursive', action='store_true', help='Search recusibly')
args = parser.parse_args()

def get_video_stream(probe):
    for stream in probe.get('streams', []):
        if stream.get('codec_type') == 'video':
            return stream
    return None


def scan_folder(folder):
    for i in os.listdir(folder):
        path = os.path.join(folder, i)
        if os.path.isdir(path):
            if args.recursive:
                scan_folder(path)
        elif i.split(".")[-1].lower() in video_formats:
            try:
                probe = ffmpeg.probe(path)
            except ffmpeg.Error as e:
                print(f"Title: {path}")
                print(f"Error probing file: {e}")
                continue

            video_stream = get_video_stream(probe)
            print(f"Title: {path}")
            if video_stream and 'width' in video_stream and 'height' in video_stream:
                print(calres(video_stream['width'], video_stream['height']))
            else:
                print("Unknown video stream or missing resolution info")


scan_folder(args.folder)
