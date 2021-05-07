Installation (Standalone)
------------------------

1. Download the latest standalone release at
2. Either run it via command line (see options below) or .bat

If you don't want to use the command line, you can use a .bat file to start the program.
As examples, you can just double-click dresden.bat or leipzig.bat and you're ready to go (what the names mean should be self-explanatory).

If you want to check other vaccination centers, you can just modify a .bat file (right click -> edit) and specify the name of your vaccination center of choice as shown at https://www.countee.ch/app/de/counter/impfee/_iz_sachsen (for example "Annaberg IZ").


My Antivirus/Smart Screen complains, what should I do?
------------------------------------------------------

No worries, these are false positives. The .exe is build using pyinstaller - those being suspected by Windows SmartScreen or antivirus solutions is a recurring issue (see for example https://github.com/pyinstaller/pyinstaller/issues/4852).

You can also just run it from source as written below.


Installation (Source)
---------------------

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
                        Example: "Dresden IZ".

optional arguments:
  -h, --help            show this help message and exit
  --intervall INTERVALL
                        Check intervall in minutes (default: 10).
```
