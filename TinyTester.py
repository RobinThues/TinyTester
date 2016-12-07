""" this program tests shortend urls for actual content behind them.
it also saves the content url to a file """
import string
import random
import datetime
import urllib
import sys
import getopt


def generate_path(length=7, charset=string.ascii_letters + string.digits):
    """ generate paths part of urls to check """
    return ''.join(random.choice(charset) for _ in range(length))

def generate_timestring():
    """ return formatted time """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def test_one_url(host='http://bit.ly/', path='1234567'):
    """ test a single URL+path """
    try:
        url = urllib.urlopen(host+path)
        if url.geturl() != (host+path):
            return url.geturl()
        else:
            return host + path + ' found nothing'
    except Exception as exception:
        return host + path + ' error: ' + exception


def log_single_response(entry='placeholder'):
    """ appends a single entry to a log """
    with open('log', 'a') as logfile:
        logfile.write(generate_timestring() + ' ' + entry + '\n')

def handle_arguments(argv):
    """ handles commandline arguments """
    try:
        opts, args = getopt.getopt(argv, )
    except getopt.GetoptError:
        print 'tinytester.py -u <URL>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-u', '--url'):
            return arg
        elif opt in ('-h', '--help'):
            print 'Use -u <URL> to specify URL'
            sys.exit()

def main(argv):
    """ starting """
    #handle_arguments(argv)
    for counter in range(100):
        tested = test_one_url('http://tinyurl.com/', generate_path(6,))
        if ' ' not in tested:
            log_single_response(tested)
        print str(counter) + ' done'


if __name__ == '__main__':
    main(sys.argv[1:])
