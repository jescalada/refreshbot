import requests
import sys


def main():
    repetitions = sys.argv[1]
    for i in range(int(repetitions)):
        requests.get(sys.argv[2])


if __name__ == '__main__':
    main()
