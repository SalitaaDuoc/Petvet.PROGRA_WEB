# Petvet.PROGRA_WEB

Al clonar el repositorio es necesario seguir estos pasos:

1. Crear un entorno virtual. Uno de estos comandos en la consola sobre la carpeta del proyecto deberian funcionar:
  py -m venv venv
  python -m venv venv

2. Activar el entorno virtual. Si se creo a partir de el comando anterior este sera suficiente:
  .\venv\Scripts\activate

3. Instalar dependencias en el entorno virtual. Usar el siguiente comando:
  pip install -r .\requirements.txt

4. Una vez seguidos estos pasos, ejecutar el servidor con:
  .\manage.py runserver