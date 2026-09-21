import sys

def main(args):

    print(f'The program received {len(sys.argv)} arguments. They were:')
    print(args)
    return

if __name__ == '__main__':
    main(sys.argv)