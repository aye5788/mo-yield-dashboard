# Yield regime thresholds (empirical quintiles from your study)
YIELD_BUCKETS = [
    0.07,   # expensive
    0.085,
    0.10,
    0.115,
    0.13    # cheap
]

# Empirical forward 12M return by regime (from your model)
FORWARD_RETURNS = {
    0: 0.02,
    1: 0.08,
    2: 0.12,
    3: 0.20,
    4: 0.25
}

def classify_yield(yield_value):
    for i, threshold in enumerate(YIELD_BUCKETS):
        if yield_value <= threshold:
            return i
    return 4


def expected_return(bucket):
    return FORWARD_RETURNS[bucket]


def price_targets(dividend):
    return {
        "7% Yield": dividend / 0.07,
        "8% Yield": dividend / 0.08,
        "9% Yield": dividend / 0.09,
        "10% Yield": dividend / 0.10,
        "11% Yield": dividend / 0.11,
        "12% Yield": dividend / 0.12,
    }

