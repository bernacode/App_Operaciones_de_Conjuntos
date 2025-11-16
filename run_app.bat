@echo off
REM -----------------------------------------
REM Run_app_smart.bat - Ejecuta la App de Conjuntos
REM Instala solo lo necesario y abre la app automáticamente
REM -----------------------------------------

SET ROOT_DIR=%~dp0

REM Verificar si Python está instalado
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python no esta instalado o no esta en PATH.
    pause
    exit /b
)

REM Crear entorno virtual si no existe
IF NOT EXIST "%ROOT_DIR%venv\Scripts\activate.bat" (
    echo Creando entorno virtual...
    python -m venv "%ROOT_DIR%venv"
)

REM Activar entorno virtual
call "%ROOT_DIR%venv\Scripts\activate.bat"

REM Verificar si Streamlit está instalado
pip show streamlit >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Streamlit no esta instalado. Instalando...
    pip install streamlit
)

REM Instalar otras dependencias
echo Instalando librerias necesarias...
pip install --upgrade pip
pip install -r "%ROOT_DIR%requirements.txt"

REM Ejecutar la app Streamlit en navegador automáticamente
echo Ejecutando la app...
start "" streamlit run "%ROOT_DIR%src\main.py" --browser.serverAddress=localhost --browser.gatherUsageStats=False

exit