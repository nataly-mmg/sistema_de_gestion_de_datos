# Sistema de Gestión de Datos – Grupo Océanos

## 1. Contexto del proyecto

Grupo Océanos es una oficina de ingeniería naval ubicada en Puerto Montt, dedicada al desarrollo de documentación técnica para naves menores y mayores, tales como planos de arreglo general, estudios de estabilidad, manuales técnicos y regularizaciones ante la Autoridad Marítima.

En el trabajo diario de la oficina, se gestionan múltiples naves y solicitudes de trabajo de forma paralela, cada una con distintos estados de avance, responsables y observaciones técnicas. Actualmente, esta gestión se realiza principalmente mediante **planillas Excel**, en las cuales se registra el estado de los proyectos, los responsables asignados y observaciones relevantes.

Si bien estas planillas permiten llevar un control básico, presentan limitaciones importantes, tales como:
- dificultad para mantener un historial ordenado de cambios,
- riesgo de duplicidad de información,
- dependencia del manejo manual de los datos,
- y poca escalabilidad a medida que aumenta la cantidad de naves y proyectos.

En este contexto, surge la necesidad de desarrollar un **sistema de gestión de datos en Python**, que permita traspasar esta lógica de trabajo desde planillas Excel a una solución programada, estructurada y trazable, aplicando los conocimientos adquiridos en el Módulo 3.

Este proyecto corresponde a una **actividad ABP (Aprendizaje Basado en Proyectos)** y busca desarrollar una solución real, basada en un proceso existente, utilizando herramientas de programación para optimizar la gestión interna de la oficina.

---

## 2. Objetivo del sistema

Diseñar e implementar un sistema de gestión en Python que permita:

- Registrar y administrar fichas técnicas de naves.
- Gestionar proyectos asociados a cada nave.
- Controlar estados de avance de los proyectos.
- Asignar responsables de ejecución.
- Mantener un historial completo de eventos y observaciones.
- Aplicar estructuras de control, funciones, estructuras de datos y modularización.

---

## 3. Funcionalidades principales

El sistema presenta un menú principal con las siguientes opciones:

1. Registrar nave  
2. Ver / Editar nave  
3. Crear proyecto  
4. Ver / Editar proyectos  
5. Asignar responsable  
6. Cambiar estado de proyecto  
7. Visualizar estadísticas  
8. Ver historial por nave  
0. Salir  

Cada proyecto puede encontrarse en uno de los siguientes estados:

- EN_ESPERA  
- EN_PROCESO  
- DETENIDO  
- TERMINADO  

Las observaciones y notas asociadas a proyectos o historial son siempre opcionales y quedan registradas con fecha y autor.

---

## 4. Estructura del proyecto

El proyecto se organiza de la siguiente manera:


- **main.py**: archivo principal que inicia el sistema y gestiona el menú.
- **modulos/**: carpeta destinada a la organización modular del código.
- **README.md**: documentación general del proyecto.

A medida que avance el desarrollo, se incorporarán nuevos archivos dentro de la carpeta `modulos` para separar responsabilidades y mejorar la mantenibilidad del código.

---

## 5. Tecnologías y conceptos aplicados

Este proyecto aplica los siguientes contenidos del módulo:

- Tipos de datos básicos en Python.
- Estructuras de datos: listas, diccionarios, tuplas y conjuntos.
- Estructuras de control: condicionales y bucles.
- Uso de funciones con parámetros y valores de retorno.
- Modularización del código mediante archivos .py
- Buenas prácticas de legibilidad y organización.

---

## 6. Estado del proyecto

En proceso...

El sistema se encuentra actualmente en etapa de diseño y estructuración, definiendo flujos, estructuras de datos y organización de archivos, previo a la implementación completa del código.

El desarrollo y los avances del proyecto se respaldan mediante control de versiones en GitHub.