import asyncio

import click
from click import Group
from litestar.plugins import CLIPluginProtocol

from src.infrastructure.database.seeders.run_seeder import run


class CLIPlugin(CLIPluginProtocol):
    """Custom command for seeders running."""

    def on_cli_init(self, cli: Group) -> None:
        """Run seeders in async mode."""

        @cli.command()
        def run_seeders() -> None:
            asyncio.run(run())
            click.echo("Seeders executed successfully!")
