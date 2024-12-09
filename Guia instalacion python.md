# Guía de Instalación de Python 3 en Windows

Esta guía detalla los pasos para instalar Python 3 en un sistema operativo Windows y asegurarte de que esté configurado correctamente para su uso.

---

## 1. **Descargar el Instalador de Python**
1. Abre un navegador web y ve al sitio oficial de Python:
   - [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Haz clic en el botón de descarga que aparece en la página principal. Por defecto, detectará la versión más reciente compatible con tu sistema operativo Windows.

---

## 2. **Ejecutar el Instalador**
1. Abre el archivo descargado (normalmente, estará en tu carpeta de `Descargas`).

2. En la ventana inicial del instalador:
   - **Marca la opción "Add Python 3.x to PATH"**: Esto es crucial para ejecutar Python desde cualquier lugar en la línea de comandos.
   - Haz clic en **"Customize installation"** si deseas instalar componentes adicionales o cambiar el directorio de instalación. Si no, selecciona **"Install Now"** para una instalación predeterminada.

---

## 3. **Configurar Opciones Personalizadas (Opcional)**
Si seleccionaste **"Customize installation"**:
1. Verifica que estén marcadas las opciones:
   - `pip` (administrador de paquetes de Python).
   - `tcl/tk` y `IDLE` (para la interfaz gráfica y el entorno de desarrollo).
   - `Python test suite` (opcional para pruebas avanzadas).
   
2. Elige el directorio de instalación o usa la ubicación predeterminada.

3. Haz clic en **"Install"** para comenzar la instalación.

---

## 4. **Completar la Instalación**
1. Una vez que la instalación se haya completado, haz clic en **"Close"**.

2. Puedes verificar que Python se haya instalado correctamente:
   - Abre el **Command Prompt** (tecla Windows + `R`, escribe `cmd` y presiona Enter).
   - Escribe el siguiente comando:
     ```cmd
     python --version
     ```
   - Deberías ver la versión instalada de Python, como `Python 3.x.x`.

3. Verifica que `pip` esté instalado escribiendo:
   ```cmd
   pip --version
   ```

---

## 5. **Configurar Variables de Entorno (Si No Seleccionaste PATH)**
Si olvidaste marcar la opción **"Add Python 3.x to PATH"**:
1. Busca "Variables de entorno" en el menú de inicio y selecciona **"Editar las variables de entorno del sistema"**.

2. En la ventana emergente, selecciona **"Variables de entorno"**.

3. En la sección "Variables del sistema":
   - Selecciona la variable **Path** y haz clic en **Editar**.
   - Haz clic en **Nuevo** y agrega la ruta del directorio de Python y del directorio `Scripts` (ejemplo):
     ```
     C:\Python39\
     C:\Python39\Scripts\
     ```

4. Haz clic en **Aceptar** en todas las ventanas y reinicia el terminal.

---

## 6. **Probar la Instalación**
1. Abre el **Command Prompt** o **PowerShell** y escribe:
   ```cmd
   python
   ```
   Esto debería abrir el intérprete interactivo de Python (REPL), mostrando algo como:
   ```
   Python 3.x.x (tags/v3.x.x:...)
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

2. Sal del intérprete escribiendo:
   ```python
   exit()
   ```

---

## 7. **Instalar Paquetes Adicionales**
Con `pip`, puedes instalar paquetes y bibliotecas adicionales. Por ejemplo, para instalar `numpy`, ejecuta:
```cmd
pip install numpy
```

---

## 8. **Opcional: Instalar un Entorno de Desarrollo**
Para facilitar el desarrollo en Python, puedes instalar un IDE (Entorno de Desarrollo Integrado) como:
- **VS Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm**: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
- **IDLE**: Incluido por defecto con Python.

---

¡Listo! Ahora tienes Python 3 instalado y configurado en tu máquina con Windows. 🎉
