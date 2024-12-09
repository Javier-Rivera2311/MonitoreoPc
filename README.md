# Documentación del Algoritmo de Monitoreo de Recursos del Sistema

## Descripción
Este script en Python monitorea el uso de los recursos del sistema (CPU, memoria, disco y red) durante un período de 2 minutos, recopilando métricas cada 10 segundos. Los datos recopilados se almacenan en un archivo de Excel (`monitoreo.xlsx`). El script utiliza la librería `psutil` para obtener las métricas del sistema y `openpyxl` para generar y escribir en el archivo Excel.

## Requisitos

Para ejecutar este script, necesitas tener instaladas las siguientes librerías:

- `psutil`: Para obtener métricas del sistema.
- `openpyxl`: Para crear y manejar archivos de Excel.

Puedes instalarlas utilizando `pip`:

```bash
pip install psutil openpyxl
```

## Estructura del Código

### 1. `obtener_metricas()`
Esta función obtiene las métricas de uso de los recursos del sistema:
- **CPU**: Utiliza `psutil.cpu_percent()` para obtener el porcentaje de uso de la CPU.
- **Memoria**: Utiliza `psutil.virtual_memory().percent` para obtener el porcentaje de uso de la memoria RAM.
- **Disco**: Utiliza `psutil.disk_usage('/').percent` para obtener el porcentaje de uso del disco.
- **Red**: Utiliza `psutil.net_io_counters().bytes_sent` para obtener los bytes enviados por la interfaz de red.

#### Retorno
Devuelve una tupla con las métricas: `(cpu, memoria, disco, red)`.

### 2. `crear_excel()`
Esta función crea un archivo Excel y prepara la hoja para almacenar las métricas. La hoja tendrá las siguientes columnas:
- **Tiempo (segundos)**: El tiempo transcurrido desde el inicio de la ejecución del monitoreo.
- **CPU (%)**: El porcentaje de uso de la CPU.
- **Memoria (%)**: El porcentaje de uso de la memoria RAM.
- **Disco (%)**: El porcentaje de uso del disco.
- **Red (bytes enviados)**: La cantidad de datos enviados por la interfaz de red.

#### Retorno
Devuelve un objeto `Workbook` y su hoja activa `ws` para que se pueda escribir en ella.

### 3. `monitorear()`
Esta es la función principal que gestiona el proceso de monitoreo de los recursos:
- Crea el archivo Excel y la hoja.
- Monitorea el sistema durante 2 minutos (120 segundos), recolectando métricas cada 10 segundos.
- Para cada recolección, obtiene las métricas mediante `obtener_metricas()` y las guarda en el archivo Excel.
- Finalmente, guarda el archivo Excel con el nombre `monitoreo.xlsx`.

#### Proceso de Ejecución
1. Se inicia el monitoreo con `tiempo_inicio = time.time()`.
2. Cada 10 segundos, se obtienen las métricas del sistema.
3. Se registran las métricas junto con el tiempo transcurrido en el archivo Excel.
4. El proceso se repite hasta que hayan transcurrido 120 segundos (2 minutos).
5. El archivo Excel se guarda y se notifica al usuario.

### 4. Ejecución Principal
El script ejecuta la función `monitorear()` cuando se ejecuta directamente el archivo Python.

```python
if __name__ == "__main__":
    monitorear()
```

## Funcionamiento Detallado

1. **Inicio del Monitoreo**:
   - El script comienza a ejecutar la función `monitorear()`.
   - Se crea un archivo Excel vacío con la hoja titulada "Monitoreo" y las columnas apropiadas.
   
2. **Recopilación de Datos**:
   - Se obtiene el tiempo transcurrido desde el inicio utilizando `time.time()`.
   - Cada 10 segundos se recopilan las métricas del sistema (CPU, memoria, disco y red) y se añaden a la hoja de Excel.
   
3. **Espera entre Recolecciones**:
   - Después de cada recolección de métricas, el script espera 10 segundos antes de volver a recolectar los datos.

4. **Finalización**:
   - Después de 120 segundos (2 minutos), el monitoreo se detiene.
   - El archivo Excel se guarda con los datos recopilados y se notifica al usuario que los datos se guardaron en el archivo `monitoreo.xlsx`.

## Salida Esperada

Al final de la ejecución, el script generará un archivo Excel llamado `monitoreo.xlsx` con el siguiente formato:

| Tiempo (segundos) | CPU (%) | Memoria (%) | Disco (%) | Red (bytes enviados) |
|-------------------|---------|-------------|-----------|----------------------|
| 0                 | 15.4    | 56.7        | 40.2      | 102450               |
| 10                | 16.1    | 58.2        | 40.4      | 104700               |
| ...               | ...     | ...         | ...       | ...                  |
| 120               | 14.2    | 55.8        | 39.9      | 128250               |

## Consideraciones

- El script obtiene las métricas del sistema con un intervalo de 1 segundo para cada tipo de recurso (lo cual puede no ser exacto para algunos recursos, como el uso de red).
- El monitoreo se realiza solo por un período de 2 minutos (120 segundos), pero puedes modificar el valor de `tiempo_total` y el intervalo de recolección si es necesario.
- El archivo Excel se guarda en el mismo directorio donde se ejecuta el script, y sobrescribirá el archivo si ya existe.

## Conclusión

Este script proporciona una solución simple y eficiente para monitorear el uso de los recursos del sistema (CPU, memoria, disco y red) y almacenar esos datos en un archivo Excel para su posterior análisis o uso.
