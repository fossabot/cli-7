# -*- coding: utf-8 -*-

import click

from .. import cli


@cli.Cli.command()
@click.option('--follow', '-f', is_flag=True, help='Follow the logs')
def logs(follow):
    """
    Show compose logs
    """
    assert cli.user()
    assert cli.running()
    cli.track('Show Logs')
    if follow:
        Cli.stream(f'{Cli.dc} logs -f')
    else:
        click.echo(Cli.run('logs').out)