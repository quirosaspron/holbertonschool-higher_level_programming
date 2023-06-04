#!/usr/bin/python3
import hidden_4


def main():
    direc = dir(hidden_4)
    for i in range(len(direc)):
        if(direc[i][0] != '_'):
            print("{}".format(direc[i]))


if __name__ == "__main__":
    main()
