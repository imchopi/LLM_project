# Proyecto de Generación de Texto

[Generacion_de_Texto.pdf](https://github.com/user-attachments/files/17970134/Generacion_de_Texto.pdf)

## Descripción

Este proyecto tiene como objetivo generar texto utilizando dos modelos de lenguaje: **GPT-2** y **Qwen2-0.5B**. Se implementa en Python y permite comparar los resultados de ambos modelos en la generación de texto a partir de un conjunto de entradas específicas proporcionadas por el usuario. El proyecto está diseñado para facilitar la evaluación y comparación de los modelos de generación de texto, ayudando a entender cómo cada uno maneja la creatividad, coherencia y relevancia del texto generado.

## Modelos Utilizados

1. **GPT-2 (Generative Pre-trained Transformer 2)**:
   - Un modelo de lenguaje desarrollado por OpenAI. Es uno de los modelos más conocidos y utilizados para tareas de generación de texto.
   - **Versión**: GPT-2, implementado en el proyecto para generar respuestas coherentes basadas en prompts proporcionados.

2. **Qwen2-0.5B**:
   - Un modelo de lenguaje más reciente que se utiliza para generar texto en tareas similares. A pesar de tener un tamaño menor en comparación con GPT-2, es capaz de generar textos creativos y coherentes.
   - **Versión**: Qwen2-0.5B, implementado en este proyecto para comparar su desempeño con el de GPT-2.

## Requisitos

- **Python 3.7+**
- **Librerías necesarias**:
  - `requests`
  - `json`

Puedes instalar las dependencias necesarias usando `pip`:

```bash
pip install requests
```

## Uso

1º Clonamos el repositorio con:

```bash
git clone https://github.com/imchopi/LLM_project
```

2º Iniciamos el LLM que usaremos (previamente ejecutar sin especificar el modelo y descargar el modelo deseado en la sección model accediendo a localhost y el puerto que te indique en la terminal)

Para GPT2
```bash
./start_windows.sh --api --model openai-community_gpt2 --cpu --trust-remotecode
```
Para QWEN
```bash
./start_windows.sh --api --model Qwen_Qwen2-0.5B --cpu --trust-remotecode
```

Si tu ordenador es macos o linux, usar el start de cada uno, no el de windows.

3º Finalmente hacemos 
```bash
python chat.py
```
o
```bash
python3 chat.py
```
