import sys


def main():
    v = sys.version_info
    print('Python {}.{}.{}'.format(*v))


if __name__ == '__main__':
    main()
