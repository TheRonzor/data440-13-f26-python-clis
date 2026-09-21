import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=int, default=1, choices=[1,2,3])
    args = parser.parse_args()

    print(f'Running in mode: {args.mode}')

if __name__ == '__main__':
    main()