# 🧩 App de Operaciones de Conjuntos

Este proyecto es una aplicación interactiva en **Streamlit** que permite gestionar un conjunto principal y hasta 4 subconjuntos por usuario. Los usuarios pueden iniciar sesión, ingresar sus subconjuntos y guardarlos en un archivo CSV.

---

## 📁 Estructura del proyecto

Proyecto/
│
├─ src/ # Código fuente
│ ├─ main.py # Script principal de la app
│ └─ interfaces/ # Módulos de la app
│
├─ requirements.txt # Librerías necesarias
├─ run_app.bat # Script para ejecutar la app automáticamente
└─ README.md # Este archivo

## ⚡ Requisitos

- **Python 3.10+**
- Windows / macOS / Linux
- Conexión a internet (solo la primera vez para instalar dependencias)

---

## 🚀 Cómo ejecutar

1. Extrae el proyecto en cualquier carpeta.
2. Abre la carpeta del proyecto.
3. Ejecuta `run_app.bat` (Windows) o, en macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/main.py
```

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
- pandas==2.3.3
- numpy==2.3.4
- streamlit-option-menu==0.4.0
- altair==5.5.0

Las demás dependencias están en `requirements.txt`.

---

## 📝 Autor

Christian Deliso
Proyecto universitario
