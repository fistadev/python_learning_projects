counts = dict()
files = open('text.txt')


def readfile(txt):
    for file in files.readlines():
        file.count(file)


def countwords(line):
    for word in words:
        words = files.split()
        counts[word] = counts.get(word, 0) + 1


def main(x):
    print(f'Count: {x}')


if __name__ == '__main__':
    main(counts)
