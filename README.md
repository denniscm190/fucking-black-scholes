# fucking-black-scholes model

I'm a finance student trying to stop procrastinating and start studying my derivatives lectures. So, in order to
understand the Black-Scholes model, I built this simple command line tool. Which is far more interesting than memorizing
stupid stuff from the professor's slides.

## Installation

### Using PIP

```bash
pip install fucking-black-scholes
```

### Manual

```bash
git clone https://github.com/denniscm190/fucking-black-scholes.git
cd fucking-black-scholes
python setup.py install
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
fbs --spot-price=20.00 --exercise-price=21.00 --risk-free-rate=0.05 --std=0.25 --expiration=0.5
```

#### Output

```bash
---------------------------------------------
European call option price: 1.197698084193286
---------------------------------------------
```