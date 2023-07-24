from frameandgif.core import FFmpeg
from frameandgif.parser import Parser


def main():
    parser = Parser().get_parser()
    args = parser.parse_args()

    core = FFmpeg(
        filename=args.filename,
        method=args.method,
        params=args.params,
        output=args.output
    )

    core.run()

    print(args)


if __name__ == '__main__':
    main()