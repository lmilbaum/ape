#!/usr/bin/env python3

import click
import yaml


@click.command()
@click.option('--dockerfile', default='./Dockerfile', help='Dockerfile path')
def main(dockerfile):
    bom = {}
    with open(dockerfile, 'r') as infile:
        bom['dockerfile'] = infile.read()

    print(yaml.dump(bom, default_flow_style=False))


if __name__ == '__main__':
    main()
