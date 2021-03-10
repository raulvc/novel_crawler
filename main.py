import argparse
import os

from src.novel_full_crawler import NovelFullCrawler
from src.royalroad_crawler import RoyalRoadCrawler
from src.oppa_crawler import OppaCrawler


def str2bool(v):
    # https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--initial-page', type=str, help='Initial page for crawling.', required=True)
    parser.add_argument('-o', '--out', type=str, help='Output filepath.', default=os.path.join(os.getcwd(), 'book.txt'))
    parser.add_argument('-a', '--append', type=str2bool, nargs='?',
                        const=False, default=True,
                        help="Append mode.")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    initial_page = args.initial_page
    if "royalroad" in initial_page:
        RoyalRoadCrawler(start_url=args.initial_page, output=args.out, append=args.append).run()
    elif "novelfull" in initial_page:
        NovelFullCrawler(start_url=args.initial_page, output=args.out, append=args.append).run()
    elif "oppatranslations" in initial_page:
        OppaCrawler(start_url=args.initial_page, output=args.out, append=args.append).run()
    else:
        print("website unsupported")
