from utilities.accountant import calculate_vat

def test_calculate_vat():
    assert calculate_vat(100) == (121, 21)
    assert calculate_vat(50) == (60.5, 10.5)
    assert calculate_vat(100, 6) == (106, 6)
    assert calculate_vat(30.3, 0) == (30.3, 0)