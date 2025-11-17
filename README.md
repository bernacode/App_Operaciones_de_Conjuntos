# 🧩 App de Operaciones de Conjuntos

Este proyecto es una aplicación interactiva en **Streamlit** que permite gestionar un conjunto principal y 4 subconjuntos por usuario. Los usuarios pueden iniciar sesión, ingresar sus subconjuntos y guardarlos en un archivo CSV.

---

## 📁 Estructura del proyecto

Proyecto/
│
├─ launcher/ # Scripts para abrir la app
│ ├─ abrir_web.bat # Abre la app online en el navegador
│ └─ abrir_web.exe # Versión compilada del .bat con icono
│
├─ src/ # Código fuente
│ ├─ data/ # Bases de datos
│ │ ├─ conjuntos.csv # Se guardan los subconjuntos
│ │ └─ usuarios.csv # Se guardan los usuarios
│ ├─ interfaces/ # Interfaces de la app
│ │ ├─ establecer_subconjuntos.py
│ │ ├─ login.py
│ │ ├─ principal.py
│ │ └─ resultados.py
│ ├─ logic/ # Lógica de operaciones
│ │ └─ operaciones.py
│ └─ main.py
│
├─ requirements.txt # Librerías necesarias
└─ README.md # Este archivo

## ⚡ Requisitos

- **Python 3.10+**
- Windows / macOS / Linux
- Conexión a internet (solo si instalas dependencias o usas la app online)

---

## 🚀 Cómo ejecutar

1️⃣ Usando el .exe (recomendado)

1. Extrae el proyecto en cualquier carpeta.
2. Abre la carpeta launcher/.
3. Haz doble clic en abrir_web.exe (Windows) para abrir la app directamente en tu navegador:
   https://app-conjuntos.streamlit.app

2️⃣ Usando el .bat (alternativa)

1. Abre la carpeta launcher/.
2. Haz doble clic en abrir_web.bat.
3. La app se abrirá en el navegador y la ventana mostrará un mensaje de ejecución.

---

## 💻 Ejecutar desde el código fuente

Si quieres ejecutar la app directamente desde Python y Streamlit:

- Paso 1: Crear y activar un entorno virtual

# Windows:

cd Proyecto
python -m venv venv
venv\Scripts\activate

# macOS / Linux:

cd Proyecto
python3 -m venv venv
source venv/bin/activate

- Paso 2: Instalar dependencias

pip install -r requirements.txt

- Paso 3: Ejecutar la app

streamlit run src/main.py

- La app se abrirá automáticamente en tu navegador.
- Presiona Ctrl+C en la terminal para cerrar la app.

* Paso 4: Notas importantes

- Los datos se guardan en:

src/data/usuarios.csv
src/data/conjuntos.csv

- Asegúrate de tener permisos de escritura en esa carpeta.

---

## 👤 Uso de la app

1. Inicia sesión con usuario y contraseña.
2. Si eres admin, puedes modificar el conjunto principal.
3. Ingresa tus 4 subconjuntos (elementos dentro del conjunto principal).
4. Presiona **Guardar Subconjuntos**:
   - Se validará que no estén vacíos.
   - Solo se permitirán elementos dentro del conjunto principal.
   - Los datos se guardarán en `src/data/conjuntos.csv`.

---

## 📦 Dependencias principales

- streamlit==1.51.0
- pandas==2.2.3
- numpy==2.2.4
- altair==5.5.0
- pillow==11.1.0
- pydeck==0.9.1
- streamlit-option-menu==0.4.0

---

## 📝 Autor

Christian Deliso
Proyecto universitario
