@echo off


:start
cls

cd app
@RD /S /Q dependencies
pip install -t dependencies -r requirements.txt
pip install -t dependencies .

cd dependencies
tar.exe -a -cf ..\dependencies.zip *

cd ..
echo F| xcopy /y dependencies.zip ..\shared_core\dependencies.zip
del dependencies.zip