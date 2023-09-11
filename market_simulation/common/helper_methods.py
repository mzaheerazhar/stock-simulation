
def calculate_price(stock_data, trans):
    if trans.get('transaction_type') == '0':
        return stock_data.low * int(trans.get('transaction_volume'))
    return stock_data.high * int(trans.get('transaction_volume'))
