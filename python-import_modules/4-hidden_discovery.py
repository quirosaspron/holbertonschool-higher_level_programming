#!/usr/bin/python3
import hidden_4


def main():
    length = dir(hidden_4)
    for i in range(len(length)):
        if(lenght[i][0] != '_'):
            print("{}".format(length[i]))


if __name__ == "__main__":
    main()
