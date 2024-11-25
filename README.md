# 2fa-py

A simple Python script to generate 2FA codes for your accounts.

## Steps

1. Create a virtual environment: `python3 -m venv .venv`
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the script: `python main.py -c <code_file> -s <site_name>`

## Example code file

```json
{
    "site1": "SITE1_CODE",
    "site2": "SITE2_CODE"
}
```
