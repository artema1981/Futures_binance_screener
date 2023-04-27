def shorten_number(value):
    if isinstance(value, (int, float)):
        if value >= 1000000000:
            value = f'{value / 1000000000:.1f}_B'
        elif value >= 1000000:
            value = f'{value / 1000000:.1f}_M'
        elif value >= 1000:
            value = f'{value / 1000:.0f}_K'
        return value
