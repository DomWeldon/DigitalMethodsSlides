import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='automatic section producer')

parser.add_argument('output', type=str)
parser.add_argument('prefix', type=str)
parser.add_argument('year_start', type=int)
parser.add_argument('year_end', type=int)

args = parser.parse_args()

of = Path(args.output)
years = [args.year_start + x for x in range(args.year_end+1-args.year_start)]

assert not of.exists()


def section(y, path_prefix='img/kcl_website/kcl_website_'):
    """Create a section for a particular year

    :param path_prefix: prefix for image path
    :param y: the year"""
    return ('<section \n'
            '  data-background-image="{0}{1}.png"\n'
            '  data-background-size="contain">\n'
            '\t<h3>\n'
            '\t\t<span class="dom-black-block">\n'
            '\t\t\t{1}\n'
            '\t\t</span>\n'
            '\t</h3>\n'
            '</secion>').format(path_prefix, y)


with of.open('w') as _:
    _.write('\n'.join([section(y, args.prefix) for y in years]))

print('done')
