import typer

from database_sampler import __version__
from database_sampler.sampler import app as sampler_app

app = typer.Typer()
app.add_typer(sampler_app)


@app.command()
def version():
    print(__version__)
