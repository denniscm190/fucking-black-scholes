
# python-black-scholes

A command line utility to calculate the theoretical call and put price of an European option using the black-scholes model.

## Usage

```bash
fbs --help
```

## Example
Price an European call option with the following data:

Spot price -> $20
Exercise price -> $21
Risk free rate -> 5%
Standard deviation -> 25%
Time to expiration -> 6 months

```bash
fbs \
--spot-price=20.00 \
--exercise-price=21.00 \
--risk-free-rate=0.05 \
--std=0.25 \
--expiration=0.5

---------------------------------------------
European call option price: 1.197698084193286
---------------------------------------------
European put option price: 1.6792062367882679
---------------------------------------------
```

