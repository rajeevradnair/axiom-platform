import json
from typing import Any
from datetime import date, datetime, timezone
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel
from axiom.domain.models import IntentMandate
from axiom.domain.enums import IntentType

def normalize_for_json(value: Any) -> Any:

    if isinstance(value, BaseModel):
        return normalize_for_json(value.model_dump())
    
    if isinstance(value, list):
        return [normalize_for_json(item) for item in value]
    
    if isinstance(value, dict):
        return {str(key):normalize_for_json(value[key]) for key in sorted(value.keys())}
    
    if isinstance(value, Decimal):
        return format(value, "f")

    if isinstance(value, datetime):
        return value.isoformat()

    if isinstance(value, date):
        return value.isoformat()

    if isinstance(value, Enum):
        return value.value
    
    return value
    
def to_canonical_json(value: Any) -> str:
    normalized = normalize_for_json(value)

    return json.dumps(
        normalized,
        sort_keys=True,
        separators=(",",":"),
        ensure_ascii=False
    )