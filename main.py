import yt_dlp
import os

def descargar_musica(url, carpeta="MUSICA"):
    try:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        print("Descargando...")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Descarga finalizada")
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    while True:
        url = input("Ingrese la URL del video: ")
        descargar_musica(url)
        continuar = input("¿Desea continuar? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa.")
            break