# 🧩 App de Operaciones de Conjuntos

![Python Streamlit Badge](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Streamlit Badge](https://img.shields.io/badge/Framework-Streamlit-red?style=flat-square&logo=streamlit)
![NumPy Badge](https://img.shields.io/badge/Computing-NumPy-orange?style=flat-square&logo=numpy)
![Pandas Badge](https://img.shields.io/badge/Data-Pandas-lightgrey?style=flat-square&logo=pandas)

Este proyecto es una aplicación interactiva en **Streamlit** que permite gestionar un conjunto principal y 4 subconjuntos por usuario. Los usuarios pueden iniciar sesión, ingresar sus subconjuntos y guardarlos en un archivo CSV.

---

## ⚡ Requisitos

- **Python 3.10+**
- Windows / macOS / Linux
- Conexión a internet (solo si instalas dependencias o usas la app online)

---

## 🚀 Cómo Ejecutar

### 🎯 Opción 1: Usando el .exe (Recomendado)

1. Extrae el proyecto en cualquier carpeta
2. Abre la carpeta `launcher/`
3. Haz doble clic en `abrir_web.exe` (Windows) para abrir la app directamente en tu navegador:

> 🔗 **URL:** https://app-conjuntos.streamlit.app

### ⚙️ Opción 2: Usando el .bat (Alternativa)

1. Abre la carpeta `launcher/`
2. Haz doble clic en `abrir_web.bat`
3. La app se abrirá en el navegador y la ventana mostrará un mensaje de ejecución

---

## 💻 Ejecutar desde el Código Fuente

Si quieres ejecutar la app directamente desde Python y Streamlit:

### Paso 1: Crear y Activar un Entorno Virtual

**Windows:**

```bash
cd Proyecto
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
cd Proyecto
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la app

```bash
streamlit run src/main.py
```

### Paso 4: Notas Importantes

- ✅ La app se abrirá automáticamente en tu navegador
- ❌ Presiona `Ctrl+C` en la terminal para cerrar la app
- 💾 Los datos se guardan en:
  - `src/data/usuarios.csv`
  - `src/data/conjuntos.csv`
- 🔒 Asegúrate de tener permisos de escritura en esa carpeta

---

## 👤 Uso de la App

1. **Inicia sesión** con usuario y contraseña
2. **Si eres admin**, puedes modificar el conjunto principal
3. **Ingresa tus 4 subconjuntos** (elementos dentro del conjunto principal)
4. **Presiona "Guardar Subconjuntos"**:
   - ✅ Se validará que no estén vacíos
   - ✅ Solo se permitirán elementos dentro del conjunto principal
   - 💾 Los datos se guardarán en `src/data/conjuntos.csv`

---

## 📦 Dependencias Principales

- `streamlit==1.51.0`
- `pandas==2.2.3`
- `numpy==2.2.4`
- `altair==5.5.0`
- `pillow==11.1.0`
- `pydeck==0.9.1`
- `streamlit-option-menu==0.4.0`

<details>
<summary>📋 Ver archivo requirements.txt</summary>

```txt
streamlit==1.51.0
pandas==2.2.3
numpy==2.2.4
altair==5.5.0
pillow==11.1.0
pydeck==0.9.1
streamlit-option-menu==0.4.0
</details>
```

---

## 📝 Autor

**Christian Deliso**  
📚 Proyecto Universitario

---

<div align="center">

### ⭐ ¡Si este proyecto te fue útil, considera darle una estrella! ⭐

</div>
