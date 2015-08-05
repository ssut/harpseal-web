""":mod:`harpseal.web` --- Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import argparse

from . import app


def main():
    parser = argparse.ArgumentParser(prog='harpseal-web')
    subparsers = parser.add_subparsers(dest='command')

    server_parser = subparsers.add_parser('server')
    server_parser.set_defaults(function=server_command)
    server_parser.add_argument('-H', '--host',
                               default='0.0.0.0',
                               help="host to listen. [default: %(default)s]")
    server_parser.add_argument('-P', '--port',
                               default='24682',
                               help="port to listen. [default: %(default)s]")

if __name__ == '__main__':
    main()
