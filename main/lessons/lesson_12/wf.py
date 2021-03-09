def main():
    with open('demo.txt') as f:
        for i, line in enumerate(f):
            print(i, line)


if __name__ == '__main__':
    main()
