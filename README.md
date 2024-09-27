# Consulta Automatizada de Antecedentes Legales
Quienes somos: Jerónimo Fotinós y Benjamín Marcolongo, alumnos del doctorado en física de la Facultad de Matemática, Astronomía, Física y Computación de la Universidad Nacional de Córdoba (FaMAF, UNC).

Contexto: este trabajo se desarrolla en el marco del curso de posgrado “Text Mining”, dictado por Laura Alsonso Alemany, Profesora Asociada del Grupo de Procesamiento de Lenguaje Natural, del departamento de Ciencias de la Computación, FaMAF, UNC.
## Resumen
En el presente proyecto se plantea la implementación de un modelo de lenguaje adaptado para responder consultas de jurisprudencia sobre textos legales argentinos. En particular, para el presente prototipo, nos enfocamos en los fallos de la corte suprema. Nuestro objetivo es que, a través de una interfaz de tipo chat, profesionales del derecho vean facilitadas sus tareas de búsqueda de antecedentes. Este objetivo está motivado por la esperanza de ayudar a reducir los tiempos demandados por estas tareas.
## Objetivos Preliminares
Dentro de nuestros objetivos específicos, se encuentra la implementación de un RAG (*Retrieval Augmented Generation*) para responder consultas sobre las sentencias más trascendentes que emite el Tribunal de la Corte Suprema, como recopiladas en la colección “Fallos”. Otra restricción al alcance que nos planteamos, al menos en estos objetivos preliminares, es que el sistema deberá responder preguntas sobre fallos posteriores al año 1992. El sistema debería listar los tomos recuperados como contexto, e idealmente los fallos, aunque esto último es difícil con los datos actuales.
## Hipótesis de Trabajo
Fundamentalmente, suponemos que los prompts de los usuarios van a constituir texto cuyo embedding va a ser similar al de las secciones relevantes de los fallos. Adicionalmente, suponemos que el ajuste fino (*fine-tuning*) del modelo de lenguaje utilizado resultará en un uso del lenguaje más apropiado, que incluya la correcta utilización de vocabulario específico.

A fin de intentar evaluar cuán ciertas resulten estas suposiciones, planeamos utilizar las siguientes heurísticas. Por un lado, para evaluar la recuperación (*retrival*), pensamos usar preguntas que apuntan a recuperar fallos específicos (aunque sea como sanity checks). Estas idealmente serían generadas por etiquetadores, pero también podrían ser sintéticas. Por otro lado, el modelo completo, incluyendo el ajuste fino, se evaluará utilizando preguntas generales sobre derecho argentino tomadas de exámenes multiple opción.
## Técnicas a Aplicar
Se implementará un RAG que constará de al menos las siguientes partes:
1. un embedding para oraciones;
2. un LLM para idioma castellano, con un ajuste fino sobre texto legal argentino;
3. una base de datos vectorial con el corpus de fallos.

La razón por la que elegimos utilizar un RAG es que estos reducen las alucinaciones, dándoles a los modelos un corpus en el que basar sus respuestas. Además, esta información puede ser actualizada sin necesidad de reentrenar. Sin embargo, quizás lo más interesante es que permiten citar las fuentes que el LLM usó como contexto para dar su respuesta. Esto es importante porque puede dar cierto grado de explicabilidad, permitiéndole al usuario evaluar las razones de la respuesta, y sopesar cuánto “creerle” al LLM.

El procedimiento a aplicar será el siguiente:
1. Los textos relevantes se fraccionaran en trozos para que nos alcance la ventana de contexto del LLM. Este fraccionamiento será tal que haya cierta superposición entre los trozos, a fin de evitar la pérdida de información relevante.
2. Se harán embeddings de estos trozos y se los almacenará en una base de datos vectorial.
3. Al recibir un prompt del usuario, primero se obtendrá el embedding de este. El mismo se usará para buscar en la base de datos vectorial los trozos más similares a la pregunta. Los strings correspondientes y el prompt original se usarán para llenar una plantilla, obteniendo así el prompt final.
4. Le damos a un LLM que ha sido fintuneado con texto legal argentino el prompt final y generamos una respuesta.
5. A la respuesta generada con el LLM, le agregamos abajo los fragmentos utilizados como contexto y su procedencia.

Respecto al fine-tuning del modelo, planteamos en principio hacerlo utilizando Causal Language Modeling (CLM), pues es la tarea más apropiada para generación de texto. Si esto no fuera suficiente, una alternativa sería realizar el fine-tuning en dos etapas: una primera etapa de domain adaptation basada en MLM (Masked Language Modeling), seguida de la etapa de CLM. Esta sugerencia supone que el MLM ayudaría al modelo a inferir el “significado” de palabras específicas de la jerga legal.
## Referencias
- Fuente de los datos: Página de la Secretaría de Jurisprudencia de la Corte Suprema de la Nación - [Tomos Colección “Fallos” 1863 - 2024 (1 a 347)](https://sjservicios.csjn.gov.ar/sj/tomosFallos.do?method=iniciar)
- Documentación de Langchain:
	- [Build a RAG App](https://python.langchain.com/v0.2/docs/tutorials/rag/)
	- [How to load PDFs](https://python.langchain.com/v0.2/docs/how_to/document_loader_pdf/)
- Hugging Face tutorials > Task Guides > Natural Language Processing:
	- [Masked language modeling](https://huggingface.co/docs/transformers/tasks/masked_language_modeling)
	- [Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)
- [Repositorio del taller “Modelos de lenguaje a tu medida”](https://github.com/nanom/llm_adaptation_workshop/tree/main)
## Planificación
Contamos con unas 8 semanas en total, del 01/10/2024 al 25/11/2024.
### Semanas 1 y 2: Preprocesamiento y Data Collection
1. Extraer texto de los tomos, estructurar el dataset en el formato convencional para datasets de texto plano. Subdividir en fallos en lugar de tomos, guardando el fallo y el tomo como metadatos.
2. Reunir un corpus de texto legal argentino para realizar el fine-tuning.
3. Armar el dataset de preguntas y respuestas de exámenes múltiple opción.
### Semanas 3 y 4: RAG Pipeline
1. Analizar las longitudes de los fallos para elegir el tamaño de los chunks, teniendo en cuenta el número de elementos que seremos capaces de recuperar como contexto a raíz de este.
2. Completar el pipeline del RAG: elegir el embedding, armar la base de datos vectorial, elegir el template para el prompt y la respuesta.
### Semanas 5 y 6: Fine-tuning
El objetivo de este período es elegir el modelo y realizar su fine-tuning.
### Semanas 7 y 8: Evaluación y Conclusión
1. Experimentos de recuperación de fallos específicos (preguntas sintéticas).
2. Evaluación con preguntas múltiple opción.