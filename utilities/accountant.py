STANDARD_RATE = 'standard rate'
REDUCED_RATE = 'reduced rates'
NO_VAT = 'no vat'


def calculate_vat(net_price, vat_rate=21):

    if isinstance(vat_rate, str):
        if vat_rate == STANDARD_RATE:
            vat_rate = 21
        elif vat_rate == REDUCED_RATE:
            vat_rate = 6
        elif vat_rate == NO_VAT:
            vat_rate = 0
        
    if isinstance(vat_rate, int):
        vat_amount = (net_price * vat_rate) / 100
        total_price = net_price + vat_amount
        return total_price, vat_amount
    else:
        raise ValueError(f"vat rate unknow: {vat_rate}")
