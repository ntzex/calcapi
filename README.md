# A simple calculator api (written on python using fastapi)

## Actions
```
sum  (+)
sub  (-)
mult (*)
div  (/)
```

## How to form request
> /action/n1/n2

## How to run (e.g. linux)
```bash
# Setup venv and activate it (optional)
python3 -m venv .
source Scripts/activate

# Install deps
pip install -r requirements.txt

# Run it
uvicorn main:api --reload
```
