from utilities.accountant import (
    calculate_vat, STANDARD_RATE, REDUCED_RATE, NO_VAT)

def test_calculate_vat_int():
    assert calculate_vat(100) == (121, 21)
    assert calculate_vat(50) == (60.5, 10.5)
    assert calculate_vat(100, 6) == (106, 6)
    assert calculate_vat(30.3, 0) == (30.3, 0)


def test_calculate_str():
    assert calculate_vat(100, STANDARD_RATE ) == (121, 21)
    assert calculate_vat(50, STANDARD_RATE) == (60.5, 10.5)
    assert calculate_vat(100, REDUCED_RATE) == (106, 6)
    assert calculate_vat(200, REDUCED_RATE) == (212, 12)
    assert calculate_vat(30.3, NO_VAT) == (30.3, 0)