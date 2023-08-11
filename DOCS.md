
# Table of Contents

1.  [Usage](#org9bd323d)
    1.  [Example](#orga21d4a0)


<a id="org9bd323d"></a>

# Usage

    fbs --help


<a id="orga21d4a0"></a>

## Example

Price a European call option with the following data:

-   Spot price -> $20
-   Exercise price -> $21
-   Risk free rate -> 5%
-   Standard deviation -> 25%
-   Time to expiration -> 6 months

    fbs \
    --spot-price=20.00 \
    --exercise-price=21.00 \
    --risk-free-rate=0.05 \
    --std=0.25 \
    --expiration=0.5

Output:

    ---------------------------------------------
    European call option price: 1.197698084193286
    ---------------------------------------------
    European put option price: 1.6792062367882679
    ---------------------------------------------

