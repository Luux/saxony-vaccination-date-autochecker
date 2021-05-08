# Saxony Vaccination Date Autochecker
-------------------------------------

**Deutsche Anleitung:** https://github.com/Luux/saxony-vaccination-date-autochecker/blob/master/LIESMICH.md
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------



This tool periodically checks free vaccination dates of vaccination centers in Saxony by accessing the information available at https://www.countee.ch/app/de/counter/impfee/_iz_sachsen. If there are more vaccination dates available than at the last time checked, you'll get a notification.

This tool does NOT register you for an appointment. But you can let it run in the background and don't have to monitor the countee page by yourself all day.

![image](https://user-images.githubusercontent.com/15156652/117510088-b9f3a700-af8b-11eb-84c4-11c531d17c4c.png)




Installation (Standalone)
------------------------

1. Download the latest standalone release at https://github.com/Luux/saxony-vaccination-date-autochecker/releases
2. Either run it via command line (see options at the bottom of this README) or by double-clicking on a .bat starter

If you don't want to use the command line, you can use a .bat file to start the program.
As examples, you can just double-click dresden.bat or leipzig.bat and you're ready to go (what the names mean should be self-explanatory).

If you want to check other vaccination centers, you can just modify a .bat file (right click -> edit) and specify the name of your vaccination center of choice as shown at https://www.countee.ch/app/de/counter/impfee/_iz_sachsen (for example "Annaberg IZ").


My Antivirus/Smart Screen complains, what should I do?
------------------------------------------------------

No worries, these are false positives. The .exe is build using pyinstaller, which just bundles the script from this repository along with all dependencies including the python runtime into a single executable. Executables build by pyinstaller being suspected by Windows SmartScreen or antivirus solutions is a recurring issue (see for example https://github.com/pyinstaller/pyinstaller/issues/4852).

If this happens:

![image](https://user-images.githubusercontent.com/15156652/117507377-389a1580-af87-11eb-885d-5a48d432eb9b.png)

Right-click on the .bat of choice -> Properties -> Allow -> OK

![image](https://user-images.githubusercontent.com/15156652/117539365-9ae82a00-b00a-11eb-9f2e-24b8fdad8e7b.png)





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
