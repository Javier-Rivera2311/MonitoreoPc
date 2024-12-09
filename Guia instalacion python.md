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

## 8. **Ejecutar un Script de Python**

Una vez que hayas instalado Python y verificado que está funcionando correctamente, puedes ejecutar tus scripts de Python de la siguiente manera:

### Pasos para Ejecutar un Script:
1. **Crear un script de Python**:
   - Abre un editor de texto (puede ser el **Bloc de notas**, **VS Code**, **PyCharm**, o cualquier editor de tu preferencia).
   - Escribe el código de Python y guárdalo con la extensión `.py`. Por ejemplo:
     ```python
     # archivo: ejemplo.py
     print("¡Hola, mundo!")
     ```

2. **Ejecutar el script desde la línea de comandos**:
   - Abre **Command Prompt** (tecla Windows + `R`, escribe `cmd` y presiona Enter).
   - Navega hasta el directorio donde guardaste el archivo `.py` usando el comando `cd`. Por ejemplo, si el archivo está en `C:\MisScripts`:
     ```cmd
     cd C:\MisScripts
     ```
   - Ejecuta el script escribiendo:
     ```cmd
     python ejemplo.py
     ```
     Esto debería mostrar:
     ```
     ¡Hola, mundo!
     ```

3. **Ejecutar un script desde cualquier ubicación**:
   - Si has agregado Python al `PATH` correctamente (como se mencionó en los pasos anteriores), puedes ejecutar el script desde cualquier carpeta en la que te encuentres, solo proporcionando la ruta completa al archivo:
     ```cmd
     python C:\MisScripts\ejemplo.py
     ```

### Problemas comunes:
- **Error "python no es reconocido"**: Si recibes este error, significa que Python no está en tu `PATH`. Asegúrate de haber marcado la opción **"Add Python 3.x to PATH"** durante la instalación o agrega manualmente las rutas correspondientes en las variables de entorno.
- **Error "No such file or directory"**: Si el script no se encuentra, asegúrate de haber navegado correctamente al directorio donde está guardado el archivo `.py`.

---

## 9. **Opcional: Instalar un Entorno de Desarrollo**
Para facilitar el desarrollo en Python, puedes instalar un IDE (Entorno de Desarrollo Integrado) como:
- **VS Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm**: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
- **IDLE**: Incluido por defecto con Python.

---

¡Listo! Ahora tienes Python 3 instalado y configurado en tu máquina con Windows, y sabes cómo ejecutar un script de Python. 🎉

--- 
