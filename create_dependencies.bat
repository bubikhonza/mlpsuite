@echo off


:start
cls

cd pipeline_engine
@RD /S /Q dependencies
py -m pip install -t dependencies -r requirements.txt
py -m pip install -t dependencies .

cd dependencies
tar.exe -a -cf ..\dependencies.zip *

cd ..
echo F| xcopy /y dependencies.zip ..\shared/core\dependencies.zip
del dependencies.zip