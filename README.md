# Tasty Analyzer
Library for ingesting a CSV file containing your trade history and displaying it's
content and performing simple analysis on your trades.  The CSV can be obtained
from your TastyWorks account.  






*** Still under development ***

## Environment
Requires Python 3.

## Execution
Direct execution of the CLI menu:
`python tasty_analyzer/menu.py`

From the menu you can load a CSV file into memory and display it's contents.


## TastyWorks CSV
A transaction in the TastyWorks CSV contains the following fields.  There are few
special cases that do not strictly adhere to this pattern.

- Date:   `12017-12-26T13:15:04-0500`
- Type:   `Trade`
- Action: `SELL_TO_CLOSE`
- Symbol: `AMZN  180119C01280000`
- Instrument Type: `Equity Option`
- Description: `Sold 1 AMZN 01/19/18 Call 1280.00 @ 1.27`
- Value: `127.00`
- Quantity: `1.0`
- Average Price: `127.00`
- Commissions: `0.00`   <----  No commission on close!
- Fees: `-0.15`
- Multiplier: `100`
- Underlying Symbol: `AMZN`
- Expiration Date: `1/19/18`
- Strike Price: `1280.0`
- Call or Put: `CALL`

Example:
`2017-12-26T13:15:04-0500,Trade,SELL_TO_CLOSE,AMZN  180119C01280000,Equity Option,Sold 1 AMZN 01/19/18 Call 1280.00 @ 1.27,127.00,1.0,127.00,0.00,-0.15,100,AMZN,1/19/18,1280.0,CALL`
`
