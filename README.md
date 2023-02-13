# Generador de im�genes con OpenAI API
Este script de Python utiliza la API de OpenAI para generar im�genes. Se proporciona un modelo de IA, una descripci�n de la imagen deseada y se genera una URL que apunta a la imagen generada.

Requisitos
Python 3
Biblioteca openai (se puede instalar con pip install openai)
Biblioteca requests (se puede instalar con pip install requests)
Configuraci�n
Antes de ejecutar el script, debes establecer la clave API de OpenAI. Esto se puede hacer directamente en el c�digo o mediante un archivo de configuraci�n.

Establecer la clave API directamente en el c�digo
Abre el archivo main.py y modifica la l�nea que dice:
openai.api_key = "MY_API_KEY"
Reemplaza "MY_API_KEY" con tu propia clave API.

Establecer la clave API en un archivo de configuraci�n
Crea un archivo llamado config.json en el mismo directorio que main.py. El contenido de config.json debe tener el siguiente formato:
{
    "openai": {
        "api_key": "MI_CLAVE_API"
    }
}
Reemplaza "MI_CLAVE_API" con tu propia clave API.

Uso
Para ejecutar el script, abre una terminal y navega hasta el directorio donde se encuentra main.py. Luego, ejecuta el siguiente comando:
python main.py
La imagen generada se mostrar� en la salida de la terminal.

Modificar la descripci�n de la imagen
Para generar una imagen diferente, modifica la variable model_prompt en el c�digo para describir la imagen deseada. Por ejemplo:
model_prompt = "Un perro con un sombrero de copa en un parque"
Modificar el tama�o de la imagen
Puedes modificar el tama�o de la imagen cambiando el valor de la variable size en el c�digo. Aseg�rate de especificar el tama�o en el formato ANCHOxALTO. Por ejemplo:
data += """
    "num_images":1,
    "size":"512x512",  # Cambiar el tama�o a 512x512
    "response_format":"url"
}
