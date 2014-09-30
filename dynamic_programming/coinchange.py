def minimum_coins(value, available_coins):
    """
    Computes minimum coins required to match the value
    Args:
        value: Input value for which change is required
        available_coins: List of change coins available_coins
    Returns:
        Count of minimium no of coins required to match the value
    Exception:
        None
    """
    if value == 0:
        return 0
    elif value < min(available_coins):
        return 0
    elif value in available_coins:
        return 1
    else:
        return (min(minimum_coins(value - coin, available_coins) for coin in available_coins if coin < value) + 1)


if __name__=='__main__':
    coins = [1, 2, 3]
    for value in range(-1, 11):
        result = minimum_coins(value=value, available_coins=coins)
        print result
