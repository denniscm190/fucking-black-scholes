from unittest import TestCase
from fbs.helpers import Option


class TestOption(TestCase):
    option = Option(
        spot_price=20.00,
        exercise_price=21.00,
        risk_free_rate=0.05,
        std=0.25,
        expiration=0.5  # 6 month (half year)
    )

    def test_compute_eu_call_price(self):
        price = self.option.compute_eu_call_price()
        price = round(price, 2)

        self.assertEqual(price, 1.20, 'EU call price is not equal to 1.20')

    def test_compute_d1(self):
        d1 = self.option.compute_d1()
        d1 = round(d1, 2)

        self.assertEqual(d1, -0.05, 'D1 coefficient is not equal to -0.05')

    def test_compute_d2(self):
        d2 = self.option.compute_d2()
        d2 = round(d2, 2)

        self.assertEqual(d2, -0.22, 'D2 coefficient is now equal to -0.22')
