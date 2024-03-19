# README
**Bootcamp MLOps Individual Project**

**Autor:** Fabio Solórzano Flores

**Fecha:** 18/03/2024

---

## Tareas

1. **Análisis y Comprensión de Datos: Exploratory Data Analysis (EDA)**
   - Archivo: `eda_AIDS_Clinical_Trials_GS175.ipynb`
   - Descripción: Este cuaderno contiene el análisis y la exploración del conjunto de datos proporcionado. Incluye estadísticas resumidas, visualizaciones e ideas derivadas de los datos.

2. **Determinar la Pregunta del Modelo de Aprendizaje Automático**
   - Descripción: La pregunta que deseo abordar con un modelo de aprendizaje automático es predecir la probabilidad de muerte de un paciente con determinadas características.

3. **Identificar la Necesidad de una Estrategia de MLOps**
   - Descripción: La razón por la que se necesita una estrategia de MLOps para este conjunto de datos o modelo es que en el campo de la medicina las condiciones y supuestos en los que se basan la mayoría de modelos probabilísticos cambian rápidamente con la aparición de nuevas tecnologías y cambios en el ambiente. Es necesario una estrategia de MLOps para asegurar que el modelo no pierda actualidad y sea útil, consistente y confiable para los usuarios. Este conjunto de datos está desactualizado pero puede funcionar como la base para poner un modelo en producción y a través de la estrategia, este modelo irá mejorando con el flujo de nueva información y reentrenamientos constantes.

4. **Diseñar la Arquitectura del Pipeline**
   - Descripción: El diseño del pipeline para este proyecto implica definir los pasos necesarios para preprocesar los datos, entrenar modelos, evaluar su rendimiento y desplegarlos en producción.

5. **Crear Modelo Base**
   - Archivo: `modelo_base.ipynb`

---

## Arquitectura del Pipeline de Preprocesamiento

El pipeline de preprocesamiento consta de los siguientes pasos, cada uno con una descripción detallada de su función:

1. **Pipeline Binario:** 
   - **Descripción:** Este pipeline pasa las columnas especificadas sin realizar ningún preprocesamiento adicional.

2. **Pipeline de Tiempo Personalizado:** 
   - **Descripción:** Este pipeline se encarga de preprocesar la columna de tiempo, imputando valores faltantes, aplicando una transformación personalizada y escalando los datos resultantes.

3. **Pipeline One-Hot:** 
   - **Descripción:** Este pipeline convierte la variable categórica 'trt' en variables dummy utilizando One-Hot Encoding.

4. **Pipeline Min-Max:** 
   - **Descripción:** Este pipeline aplica un escalado min-max a las columnas 'age' y 'wtkg'.

5. **Pipeline Log-Min-Max:** 
   - **Descripción:** Este pipeline realiza una transformación logarítmica en las columnas especificadas y luego aplica un escalado min-max a los datos resultantes.

6. **Pipeline Karnof:** 
   - **Descripción:** Este pipeline divide los valores en la columna 'karnof' por 100.

7. **Pipeline Preanti:** 
   - **Descripción:** Este pipeline divide los valores en la columna 'preanti' en tres categorías mediante binning y luego aplica One-Hot Encoding a los datos resultantes.

Con esta arquitectura de pipeline, se establece un flujo de trabajo robusto y modular que facilita la escalabilidad y la mantenibilidad del proyecto.
