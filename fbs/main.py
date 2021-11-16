import click
from fbs.helpers import Option


@click.command()
@click.option('--spot-price', type=float, required=True, help='Spot price of the underlying asset.')
@click.option('--exercise-price', type=float, required=True, help='Exercise price of the option.')
@click.option('--risk-free-rate', type=float, required=True, help='Risk free rate.')
@click.option('--std', type=float, required=True, help='Standard deviation.')
@click.option('--expiration', type=float, required=True, help='Time to expiration.')
def cli(spot_price, exercise_price, risk_free_rate, std, expiration):
    option = Option(spot_price, exercise_price, risk_free_rate, std, expiration)

    # Format output
    output = 'European call option price: {}'.format(option.compute_eu_call_price())
    output_length = len(output)
    line = ''.join('-' for _ in range(output_length))

    # Output
    click.echo(line)
    click.echo(output)
    click.echo(line)


if __name__ == '__main__':
    cli()
