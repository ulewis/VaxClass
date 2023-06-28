import time
import os
import openai
import pandas as pd

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

model = "gpt-3.5-turbo" 

data = pd.read_excel("datos/data.xlsx")
       
        
prompt = """    Tendrás un rol de clasificador de comentarios de una publicación relacionada con la vacuna contra el VPH.
                Sólo debes responder con un valor númerico.
                No tienes permitido responder otra cosa que no sea números. La clasifiación es :
                
                0: El comentario tiene una postura contraria a la vacuna contra el VPH (antivacuna)
                1: El comentario tien una postura a favor de la vacuna contra el VPH (provacuna)
                2: El comentario refleja una duda o dudas relacionada con la vacuna contra el VPH
                3: El comentario habla de cualquier otra cosa
                
                Trata de interpretar las intenciones de las personas, ya que se trata de comentarios de Facebook.
                Si no puedes clasificar, tu respuesta debe ser "3".
                Ahora, clasifica el siguiente comentario, teniendo en cuenta que tu respuesta es sólo un número : 
                
                """    

batch_size = 50  
output_file = "datos/clasificación.xlsx" 
checkpoint_file = "checkpoint.txt" 
timeout_retry_delay = 5  
completed = False

if not os.path.exists(checkpoint_file):
    with open(checkpoint_file, 'w') as file:
        file.write(str(0))

with open(checkpoint_file, 'r') as f:
    current_index = int(f.read())
    print("Verificando checkpoint...")
    print("Continuando desde la posición:", current_index)

if 'Clasificación_gpt' not in data.columns:
    data['Clasificación_gpt'] = ''

for index, row in data.iterrows():
    if index < current_index:
        continue

    comment = row['Comment']

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": comment}
            ],
            temperature=0.1
        )

        response = completion.choices[0].message.content.strip()

        if response.isdigit():
            response = int(response)
        else:
            response = None 

        data.at[index, 'Clasificación_gpt'] = response

        if (index + 1) % batch_size == 0 or (index + 1) == len(data):
            data[:index + 1].to_excel(output_file, index=False)
            print("Guardando avance ...")
            
            with open(checkpoint_file, 'w') as file:
                file.write(str(index + 1))

    except openai.error.OpenAIError as e:
        print("Error del servidor de OpenAI:", e)
        print("Reintentando en", timeout_retry_delay, "segundos...")
        time.sleep(timeout_retry_delay)
        print("Continuando desde la posición:", index+1)
        continue

else:
    completed = True
    print("Procesamiento completado. Reiniciando el contador en checkpoint...")
    with open(checkpoint_file, 'w') as file:
        file.write(str(0))

if completed:
    print("Resultados guardados en", output_file)
    print("\n" * 2)
    print("*********************")
    print("Clasificación:\n")
    print("0: El comentario tiene una postura contraria a la vacuna contra el VPH (antivacuna)")
    print("1: El comentario tiene una postura a favor de la vacuna contra el VPH (provacuna)")
    print("2: El comentario refleja una duda o dudas relacionadas con la vacuna contra el VPH")
    print("3: El comentario habla de cualquier otra cosa")
    print("\n" * 2)
    print("*********************")
    print("\n" * 2)
