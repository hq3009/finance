import sys
import os
p = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'lib')
if p in sys.path:
    pass
else:
    sys.path.append(p)
from aggregate import Aggregator

def aggregate(aggregator, filename, range=2):
    result = aggregator.summarize(range=range)
    p = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'data',
        filename)
    result.to_csv(p, sep="\t", index_label="Code")

def main():
    c_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(c_dir, '..')
    data_dir = os.path.join(base_dir, 'data')
    stock_list = os.path.join(data_dir,
                              'stocks.txt')

    aggregator = Aggregator(stock_list, data_dir)
    aggregate(aggregator, 'summary.csv', range=2)
    aggregate(aggregator, 'summary_15.csv', range=15)
    aggregate(aggregator, 'summary_30.csv', range=30)

if __name__ == '__main__':
    argsmin = 0
    version = (3, 0)
    if sys.version_info > (version):
        if len(sys.argv) > argsmin:
            result = main()
            if result:
                sys.exit(0)
            else:
                sys.exit(1)
        else:
            print("This program needs at least %(argsmin)s arguments" %
                  locals())
    else:
        print("This program requires python > %(version)s" % locals())
