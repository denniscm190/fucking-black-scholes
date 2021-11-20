import click
from fbs.helpers import Option
from fbs.helpers import format_output


@click.command()
@click.option('--spot-price', type=float, required=True, help='Spot price of the underlying asset.')
@click.option('--exercise-price', type=float, required=True, help='Exercise price of the option.')
@click.option('--risk-free-rate', type=float, required=True, help='Risk free rate.')
@click.option('--std', type=float, required=True, help='Standard deviation.')
@click.option('--expiration', type=float, required=True, help='Time to expiration.')
def cli(spot_price, exercise_price, risk_free_rate, std, expiration):
    option = Option(spot_price, exercise_price, risk_free_rate, std, expiration)

    line, call_output = format_output(
        text='European call option price',
        price=option.compute_eu_call_price()
    )

    _, put_output = format_output(
        text='European put option price',
        price=option.compute_eu_put_price()
    )

    # Output call
    click.echo(line)
    click.echo(call_output)

    # Output put
    click.echo(line)
    click.echo(put_output)
    click.echo(line)


if __name__ == '__main__':
    cli()
