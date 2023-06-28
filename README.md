# Clasificación de texto con GPT

[![En Construcción](https://img.shields.io/badge/Estado-En%20Construcción-yellow)](#)


Este proyecto es desarrollado en el Laboratorio de Ingeniería Biomédica de la Universidad Peruana Cayetano Heredia. El objetivo principal de este proyecto es clasificar comentarios en español relacionados con la vacunación utilizando la inteligencia artificial.

## Clasificador de texto en salud

Usamos _`gpt-3.5-turbo`_ de OpenAI para clasificar comentarios en cuatro categorías:

- 0: El comentario tiene una postura contraria a la vacuna contra el VPH (antivacuna)
- 1: El comentario tien una postura a favor de la vacuna contra el VPH (provacuna)
- 2: El comentario refleja una duda o dudas relacionada con la vacuna contra el VPH
- 3: El comentario habla de cualquier otra cosa

_**Nota:** Este clasificar funciona bien identificando temas relacionada con la vacunación. Sin embargo, se debe usar con precausión. Ya que requiere ser evaluado con más rigor del que los autores han realizado para su primera versión._


## Instalación

Para ejecutar tu versión de este proyecto, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
    ```shell
    git clone https://github.com/ulewis/VaxClass.git [carpeta_de_destino]
    ```
2. Configurar el entorno virtual (opcional)

    Se recomienda crear un entorno virtual para este proyecto, para mantener las dependencias aisladas del sistema global. Sigue los siguientes pasos para crear y activar un entorno virtual utilizando venv:

    - En la terminal, navega hasta el directorio del repositorio clonado:
    ```shell
    cd <directorio_del_repositorio>
    ```
  - Para entornos Unix/Linux/macOS:

    - Crea un nuevo entorno virtual:
        ```shell
        python3 -m venv gpt
        ```
    - Activa el entorno virtual:

        ```shell
        source gpt/bin/activate
        ```
 - Para Windows:

     - Crea un nuevo entorno virtual:
        ```shell
        python -m venv gpt
        ```
     - Activa el entorno virtual:

        ```shell
        gpt\Scripts\activate
        ```


3. Instala las dependencias necesarias mediante el siguiente comando:

    ```shell
    pip install -r requirements.txt
    ```
4. Asegúrate de tener un archivo de excel llamado `"data.xlsx"` en la carpeta [datos](datos/)

5. Los comentarios deberán en una columna llamada "Comment" 


## Uso

1. Agrega tu API Key de Open AI en [`"api_key.txt"`](api_key.txt) . Si aún no tienes una puedes adquirla en : https://platform.openai.com/account/api-keys

2. En la terminal, navega hasta el directorio del repositorio clonado
3. Ejecuta el archivo `"main.py"` para realizar la clasificación de comentarios utilizando GPT-3.5-turbo, se creará un nuevo archivo llamado `checkpoint.txt`

    ```shell
    python main.py
    ```


4. Se generará una nueva columna en el archivo `"data.xlsx"` llamada "Clasificación_gpt" con las clasificaciones obtenidas y se guardará en `"clasificación.xlsx"`.

5. Puedes personalizar el prompt y demás parametros en el archivo [classifier_gpt](classifier_gpt.ipynb)



## Contribución

¡Las contribuciones son bienvenidas! Si deseas colaborar en este proyecto, por favor, sigue los siguientes pasos:

1. Realiza un fork de este repositorio.
2. Crea una rama con un nombre descriptivo para tu contribución.
3. Realiza tus cambios y mejoras.
4. Envía un pull request describiendo tus cambios y explicando su importancia.

También puedes ponerte en contacto con el equipo del proyecto para obtener más información.

## Equipo
- Lewis De La Cruz - Email: umbert.de.la.cruz@upch.pe
___

- Luis Chirre - Email: luis.chirre@upch.pe



## Licencia
Este proyecto se distribuye bajo la licencia de código abierto [MIT License](LICENSE).