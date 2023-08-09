# python-black-scholes model 



## Installation

### Using pip

```bash
pip3 install fucking-black-scholes
```

## Usage

```bash
fbs --help
```

### Examples

Price a European call option with the following data:
- Spot price = $20
- Exercise price = $21
- Risk free rate = 5%
- Standard deviation = 25%
- Time to expiration = 6 months

#### Command

```bash
fbs \
--spot-price=20.00 \
--exercise-price=21.00 \
--risk-free-rate=0.05 \
--std=0.25 \
--expiration=0.5
```

#### Output

```bash
---------------------------------------------
European call option price: 1.197698084193286
---------------------------------------------
European put option price: 1.6792062367882679
---------------------------------------------
```
