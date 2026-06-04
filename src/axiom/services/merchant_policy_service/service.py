APPROVED_MERCHANTS = {
    "office depot",
    "staples",
    "travelgear outlet",
}

BLOCKED_MERCHANTS = {
    "unknown vendor",
    "unknown electronics store",
}

def normalize_merchant_name(value: str) -> str:
    return value.strip().lower()


def is_approved_merchant(merchant_name: str) -> bool:
    normalized = normalize_merchant_name(merchant_name)
    return normalized in APPROVED_MERCHANTS


def is_blocked_merchant(merchant_name: str) -> bool:
    normalized = normalize_merchant_name(merchant_name)
    return normalized in BLOCKED_MERCHANTS