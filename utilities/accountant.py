def calculate_vat(net_price, vat_rate=21):

    if isinstance(vat_rate, str):
        if vat_rate == 'standard rate':
            vat_rate = 21
        elif vat_rate == 'reduced rates':
            vat_rate = '6'
        elif vat_rate == 'no vat':
            vat_rate = 0
        
    if isinstance(vat_rate, int):
        vat_amount = (net_price * vat_rate) / 100
        total_price = net_price + vat_amount
        return total_price, vat_amount
    else:
        raise ValueError(f"vat rate unknow: {vat_rate}")
