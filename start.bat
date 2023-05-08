call ./venv/scripts/activate.bat
call pip install -r requirements.txt
where python > nul
if %errorlevel% equ 0 (
	echo python is installed and in PATH
) else (
	echo python not installed on PATH
	echo visit https://python.org/downloads and get the latest version of python before running this again
	set failed=True
)
where npm > nul
if %errorlevel% equ 0 (
	echo npm is installed and in PATH
) else (
	echo npm is not installed or not in PATH
	echo visit https://nodejs.org/en/download and get the latest version before running this again.
	set failed=True
)
if %failed%==True (
	pause press any key to exit
	exit
)
cd ./react
if exist node_modules/ (
	echo found installed react application
) else (
	npm install
)

cd ../
start cmd /k "python app.py"
start cmd /k "python VideoHandler.py"
start cmd /k "cd ./react && npm run start"