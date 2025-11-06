# Sketcher
Plug-in for Blender

## Activate Virtual Environment
- In project folder, create a Virtual Environment:
```bash
python -m venv venv
```
- Activate Virtual Environment:
```bash
venv\Scripts\activate
```

## Run Project
```bash
python main.py
```

## Create Object in Blender
### Preprocessing
- Blender uses its own bundled Python. When working with Python scripts inside Blender, it’s important to remember that this Python environment is separate from the system Python. Therefore, any external libraries (e.g., numpy, pandas) must be installed directly in Blender’s Python environment.

- If you need external libraries (numpy, scipy, etc.), install them using Blender’s Python executable:
```bash
"PathTo\Blender\4.2\python\bin\python.exe" -m ensurepip
"PathTo\Blender\4.2\python\bin\python.exe" -m pip install --upgrade pip
"PathTo\Blender\4.2\python\bin\python.exe" -m pip install numpy
```
### Run the Script
- Open Blender ```Scripting``` mode
- Open the ```mesh.py``` script
- Run the script