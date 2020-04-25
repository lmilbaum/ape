#!/usr/bin/env python3

import click
import yaml
from dockerfile_parse import DockerfileParser


@click.command()
@click.option(
    '--path', default='.', help='Dockerfile path'
)
def main(path):
    bom = {}
    dfp = DockerfileParser(path=path)

    bom['dockerfile'] = dfp.content
    bom['parent_image'] = dfp.baseimage
    print(yaml.dump(bom, default_flow_style=False))


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
