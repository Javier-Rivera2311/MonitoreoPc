import psutil
import time
from openpyxl import Workbook

# Función para obtener métricas del sistema
def obtener_metricas():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    red = psutil.net_io_counters().bytes_sent
    return cpu, memoria, disco, red

# Crear un archivo Excel para almacenar los datos
def crear_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Monitoreo"
    ws.append(["Tiempo (segundos)", "CPU (%)", "Memoria (%)", "Disco (%)", "Red (bytes enviados)"])
    return wb, ws

# Función principal para ejecutar el monitoreo cada 10 segundos por 2 minutos
def monitorear():
    # Crear el archivo Excel y la hoja
    wb, ws = crear_excel()
    
    # Tiempo de monitoreo: 2 minutos = 120 segundos
    tiempo_total = 120
    intervalo = 10  # cada 10 segundos
    tiempo_inicio = time.time()
    
    # Recolectar datos cada 10 segundos durante 2 minutos
    while time.time() - tiempo_inicio < tiempo_total:
        # Obtener las métricas
        cpu, memoria, disco, red = obtener_metricas()
        
        # Guardar los datos en la hoja de Excel
        tiempo_transcurrido = round(time.time() - tiempo_inicio)
        ws.append([tiempo_transcurrido, cpu, memoria, disco, red])
        
        # Esperar 10 segundos antes de la siguiente recolección
        time.sleep(intervalo)
    
    # Guardar el archivo Excel
    wb.save("monitoreo.xlsx")
    print("Datos guardados en 'monitoreo.xlsx'.")

# Ejecutar el monitoreo
if __name__ == "__main__":
    monitorear()
