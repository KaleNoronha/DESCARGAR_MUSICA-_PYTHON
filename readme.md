# Proyecto de Python / Python Project

## Descripción / Description

Este proyecto es una aplicación de Python que [describe brevemente la funcionalidad del proyecto].  
This project is a Python application that [briefly describe the functionality of the project].

## Requisitos / Requirements

- Python 3.11 (recomendado / recommended)
- yt_dlp
- ffmpeg (versión esencial / essential version)

## Instalación / Installation

1. Clona este repositorio / Clone this repository:
    ```bash
    git clone https://github.com/usuario/proyecto.git
    ```
2. Navega al directorio del proyecto / Navigate to the project directory:
    ```bash
    cd proyecto
    ```
3. Instala las dependencias / Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Instala la librería yt_dlp / Install the yt_dlp library:
    ```bash
    pip install yt_dlp
    ```
5. Instala ffmpeg (versión esencial) / Install ffmpeg (essential version):
    - Descarga la versión esencial de ffmpeg desde el sitio oficial.
    - Utiliza una herramienta de descompresión como 7-Zip para extraer el contenido del archivo descargado.
    - Renombra la carpeta extraída a `ffmpeg` y muévela a una ubicación permanente en tu sistema:
        - **Windows**: por ejemplo, `C:\ffmpeg`.
        - **Mac/Linux**: por ejemplo, `/usr/local/ffmpeg`.
    - Agrega FFmpeg al PATH del sistema:
        - **Windows**:
            - Presiona `Win + S`, escribe "Variables de entorno" y selecciona "Editar las variables de entorno del sistema".
            - En la pestaña "Opciones avanzadas", haz clic en "Variables de entorno".
            - En "Variables del sistema", selecciona la variable `Path` y haz clic en "Editar".
            - Haz clic en "Nuevo" y añade la ruta al directorio `bin` de FFmpeg, por ejemplo, `C:\ffmpeg\bin`.
            - Confirma los cambios haciendo clic en "Aceptar" en todas las ventanas.
        - **Mac/Linux**:
            - Abre una terminal y edita el archivo de configuración de tu shell (por ejemplo, `~/.bashrc` o `~/.zshrc`).
            - Añade la siguiente línea al final del archivo:
                ```bash
                export PATH="/usr/local/ffmpeg/bin:$PATH"
                ```
            - Guarda el archivo y recarga la configuración del shell:
                ```bash
                source ~/.bashrc  # o source ~/.zshrc
                ```
    ```bash
    sudo apt-get install ffmpeg
    ```

## Uso / Usage

Ejecuta el siguiente comando para iniciar la aplicación / Run the following command to start the application:
```bash
python main.py
```

## Contribución / Contribution

1. Haz un fork del repositorio / Fork the repository.
2. Crea una nueva rama / Create a new branch:
    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```
3. Realiza tus cambios y haz un commit / Make your changes and commit:
    ```bash
    git commit -am 'Añadir nueva funcionalidad'
    ```
4. Envía tus cambios a tu fork / Push your changes to your fork:
    ```bash
    git push origin feature/nueva-funcionalidad
    ```
5. Abre un Pull Request / Open a Pull Request.

## Licencia / License

Este proyecto está bajo la Licencia MIT / This project is licensed under the MIT License.