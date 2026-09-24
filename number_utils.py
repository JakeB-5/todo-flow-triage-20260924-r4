def safe_divide(numerator, denominator, fallback=None):
    """Divide unless the denominator is zero, in which case return fallback."""
    if denominator == 0:
        return fallback
    return numerator / denominator
