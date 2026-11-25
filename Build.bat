rem install Python install manager / https://www.python.org/downloads/
rem py -m pip install pyinstaller

rem --icon=myicon.ico

cd /d "%~dp0RRFMCLI"
py -m PyInstaller --onefile --console --name RRFMCLI RRFMCLI.py

copy *.md .\RRFMCLI\dist /Y
copy *.txt .\RRFMCLI\dist /Y
