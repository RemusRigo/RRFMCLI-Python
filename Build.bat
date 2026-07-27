rem isntall Python install manager / https://www.python.org/downloads/
rem pip install pyinstaller

rem --icon=myicon.ico

cd rrfmcli
%LocalAppData%\Python\pythoncore-3.14-64\Scripts\pyinstaller --onefile --console rrfmcli.py

@pause