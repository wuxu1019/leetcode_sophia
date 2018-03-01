from argparse import ArgumentParser
parser = ArgumentParser(description='Get recent Completed metabuilds')
    parser.add_argument(
        '--meta', required=True,
        help='Metabuild from which the GOTA package should be generated.')
args = parser.parse_args()
meta = args.meta
