Installation
------------

1. Install python - latest version is fine: https://www.python.org/

2. Make sure python is added to PATH

3. ```pip install -r requirements.txt```

4. Start the script. Example usage:
```python saxony_vaccination_date_autochecker/autocheck_countee-py "Dresden IZ"```


Options:

```
python .\saxony_vaccination_date_autochecker\autocheck_countee.py --help
usage: autocheck_countee.py [-h] [--intervall INTERVALL] vaccination_center

positional arguments:
  vaccination_center    The vaccination center name as displayed on countee.
                        Example: "Dresden IZ").

optional arguments:
  -h, --help            show this help message and exit
  --intervall INTERVALL
                        Check intervall in minutes (default: 10).
```
