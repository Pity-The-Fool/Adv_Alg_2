import argparse

def get_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--message",
                        help="Type a message to sign and verify",
                        dest="message",
                        type=str,
                        default="Cryptographic Message"
                        )

    def parse_args(args=None):
        if args is None:
            return get_parser().parse_args()
        return get_parser().parse_args(args)