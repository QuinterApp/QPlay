rmdir /S /Q windist
mkdir windist
xcopy /Q /E c:\tempbuild\QPlay.dist windist /Y
xcopy /Q /E docs windist /Y
xcopy /Q *.dll windist /Y
xcopy /Q /E ..\QPlayfiles windist /S /Y
rmdir /S /Q c:\tempbuild
del windist\t*86t.dll
pause