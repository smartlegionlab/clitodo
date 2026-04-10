# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2026, Alexander Suvorov
# All rights reserved.
# --------------------------------------------------------
import click

from clitodo.manager import AppMan


@click.command()
@click.version_option(version=f'{AppMan.name} {AppMan.version}; {AppMan.copyright};')
def cli():
    AppMan.show_head(char='-')
    AppMan.commander.run()
    AppMan.show_footer()
