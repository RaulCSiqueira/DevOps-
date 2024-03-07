import json
from pathlib import Path
import sys

def deserialize(data: str) -> dict:
    return json.loads(data)

class BillingSummaryError(Exception): ...

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from None
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from None
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from None
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from None

