from datetime import datetime

from billing import summarize_monthly

this_month = datetime.now().strftime('%b').lower()
this_month = summarize_monthly()[this_month]

print(f'The total for this month is: ${this_month}')

