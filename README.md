# Urban Routes: Automatización de Solicitud de Taxi Comfort
INDICE:
- DESCRIPCION
- LISTA DE COMPROBACIÓN
- PASOS COMPROBADOS EN EL FLUJO DE USUARIO
- TECNOLOGIAS UTILIZADAS
- ARCHIVOS DEL PROYECTO
- COMANDOS DE EJECUCIÓN
- INSTRUCCIONES PARA LAS PRUEBAS
## Descripción

Este proyecto automatiza y verifica, mediante pruebas automatizadas, la funcionalidad de solicitud de taxi en la plataforma Urban Routes, específicamente para la tarifa Comfort. Las pruebas cubren todo el flujo: desde la configuración de la ruta hasta la confirmación y llegada del taxista, incluyendo personalizaciones y métodos de pago.

---

## Lista de comprobación
setup_class(cls): Configura las opciones del navegador.

test_set_route(self): Configura y verifica la dirección de la ruta.

test_click_call_taxi_button(self): Selecciona el botón para llamar al taxi.

test_select_comfort_rate(self): Selecciona y valida la tarifa Comfort.

set_select_number_button(self): Selecciona y rellena el número de teléfono.

add_number(self): Añade número de teléfono.

phone_number(self): Verifica el número de teléfono.

the_next_button(self): Avanza al siguiente paso.

code_number(self): Añade el código de verificación del teléfono.

payment_method(self): Configura y revisa los métodos de pago.

write_driver(self): Ingresa y confirma un mensaje personalizado para el conductor.

blanket_and_tissues(self): Selecciona y valida los requisitos adicionales (manta y pañuelos).

request_ice_cream(self): Selecciona la cantidad de helado.

search_taxi(self): Realiza la búsqueda de taxi y verifica que la orden se haya ejecutado.

test_wait_driver_details(self): Verifica la recepción de los detalles del conductor y que el viaje haya sido tomado.

## Pasos comprobados en el flujo de usuario
URL de servidor

- Configurar la dirección

- Seleccionar personalización

- Pedir taxi

- Seleccionar la tarifa Comfort

- Rellenar el número de teléfono

- Agregar una tarjeta de crédito

- Escribir un mensaje para el conductor

- Pedir una manta y pañuelos

- Pedir 2 helados

- Aparece el modal: buscar un taxi

- Esperar a que aparezca la información del conductor en el modal
- 
## Tecnologías utilizadas

- **Python 3**
- **Selenium**
- **Pytest**
- **Requests**

---

## Archivos del proyecto

- `main.py`
- `data.py`
- `Urban_RoutesPage.py`
- `SMS.py`
- `README.md`

---

## Comando de ejecución

1. Ver el estado de los archivos: git status
2. Cambiar de rama: git branch
3. Crear un commit con mensaje: git commit -m "Mensaje del commit"
4. Subir los cambios al repositorio remoto: git push
5. Fusionar ramas: git merge "nombre-de-la-rama"
6. Guardar cambios temporales (stash): git stash
7. Cambiar a la rama principal (master): git checkout master
8. Comando para ejecutar las pruebas automatizadas: pytest main.py , pytest tests/test_UrbanRoutesPage.py


---

## Instrucciones para las pruebas
1. Clonar el repositorio de GitHub en tu máquina local: git clone https://github.com/alext/qa-project-Urban-Routes-es.git
2. Abrir el proyecto en PyCharm
3. Instalar las dependencias necesarias: pip install selenium, pip install pytest, pip install requests
4. Ejecutar las pruebas automatizadas: pytest 





