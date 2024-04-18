<p align="center">
  <img src="https://github.com/adalid2608/MockUps_Nutricion/blob/master/img/Logo_UTXJ.png?raw=true" alt="Logotipo de la Universidad Tecnológica de Xicotepec de Juárez"/>
</p>

***

![Organigrama](https://github.com/adalid2608/MockUps_Nutricion/blob/master/img/Organigrama.png)

***

# Perfiles de Github de los Integrantes del Equipo
- [@Aldair-NPM](https://www.github.com/Aldair-NPM)
- [@EmilioMendozaCortes](https://www.github.com/EmilioMendozaCortes)
- [@adalid2608](https://www.github.com/adalid2608)

# Enlace hacia la documentación completa: 
  [Documentación del modulo de Nutrición](https://github.com/adalid2608/MockUps_Nutricion/tree/master/Documentación)
# 1. Proposito
Desarrollar un modulo integral dentro del Sistema de gestión de un gimnasio,
orientado a la optimizacion y control eficiente, especialmente en el ambito de la
nutricion. El objetivo de este modulo es proporcionar una plataforma digital que
permita a los nutricionistas y al personal profesional del gimnasio realizar un
seguimiento preciso de las comidas y los planes de alimentacion de los usuarios. El
objetivo es crear una herramienta que facilite la comunicacion entre los usuarios y
el personal de nutricion, permitiendo el intercambio fluido de informacion sobre
dietas, objetivos de salud y restricciones dieteticas.

Ademas, se implementaran las siguientes funciones para ayudar a monitorear el
progreso de cada usuario: Ejemplos: registros de consumo de alimentos,
mediciones corporales pasadas, analisis de resultados, generacion de
recomendaciones personalizadas, etc. El principal objetivo del desarrollo de este
modulo es mejorar la experiencia del usuario del gimnasio y proporcionar un servicio
de seguimiento nutricional mas completo y adaptado a las necesidades individuales
de cada cliente. Del mismo modo, se espera que la herramienta contribuya a la
retencion de usuarios al tiempo que optimiza los procesos internos de los gimnasios
en el campo de la nutricion y promueve un enfoque holistico de la salud y el
bienestar de los usuarios.

# 2. Requerimientos Funcionales
- RF-01 	El sistema debe permitir el registro de información de los usuarios como nombre, edad, sexo, peso, estatura, alergias, entre otros. 
- RF-02 	El sistema debe permitir el registro y actualización del historial médico de los usuarios. 
- RF-03 	El sistema debe permitir la asignación de planes de alimentación personalizados para cada usuario, de acuerdo a su edad, sus objetivos y necesidades nutricionales. 
- RF-04 	El sistema debe permitir el registro y seguimiento del progreso de los usuarios en cuanto a peso, masa muscular, grasa corporal, entre otros indicadores. 
- RF-05 	El sistema debe permitir la modificación de los planes de alimentación de los usuarios en función de su progreso y nuevas necesidades identificadas. 
- RF-06 	El sistema debe permitir el registro de la ingesta de alimentos diaria de cada usuario. 
- RF-07	  El sistema debe permitir el registro y seguimiento de las rutinas de ejercicio realizadas por cada usuario. 
- RF-08 	El sistema debe tener registrados diferentes planes de alimentación predeterminados que el nutricionista pueda asignar. 
- RF-09 	El sistema debe permitir la creación y edición de planes de alimentación personalizados por el nutricionista. 
- RF-10 	El sistema debe permitir el registro y seguimiento de citas de los usuarios con el nutricionista. 
- RF-11 	El sistema debe permitir la creación de reportes y estadísticas de uso del módulo de nutrición. 
- RF-12 	El sistema debe tener un módulo de educación nutricional con artículos y videos. 
- RF-13 	El sistema debe tener un módulo de recomendación de complementos nutricionales y suplementos. 
- RF-14 	El sistema debe implementar un CRUD para las dietas asignadas. 
- RF-15 	El sistema debe permitir la carga de imágenes de platillos y progreso físico por parte de los usuarios. 
- RF-16 	El sistema debe tener un módulo de recomendación de recetas saludables personalizadas. 
- RF-17 	El sistema debe generar recomendaciones automáticas de ajustes al plan de alimentación en base a los patrones del usuario. 
- RF-18 	El sistema debe tener un portal web para los usuarios. 
- RF-19	  El sistema debe implementar un dashboard con graficas del área de nutrición. 
- RF-20	  El sistema debe tener una tabla dinámica de las dietas asignadas para mostrar el avancé.

# 3. Requerimientos No Funcionales
- RNF-01 	  El sistema debe tener un tiempo de respuesta menor a 5 segundos para consultas simples. 
- RNF-02 	  El sistema debe poder soportar hasta 100 usuarios concurrentes sin disminuir el rendimiento. 
- RNF-03 	  El sistema debe tener una disponibilidad de al menos 90% del tiempo. 
- RNF-04 	  El sistema debe cumplir con regulaciones de seguridad y privacidad como HIPAA. 
- RNF-05 	  Los datos sensibles de los usuarios deben encriptarse tanto en tránsito como en reposo. 
- RNF-06	  El sistema debe tener una interfaz intuitiva y de fácil uso para los usuarios. 
- RNF-07 	  El sistema debe tener al menos un 90% de cobertura de testing unitario. 
- RNF-08	  El sistema debe tener registros automatizados de los miembros y nutricionistas para llevar un control. 
- RNF-09	  Las interfaces deben contener información sobre algunas propuestas de dietas.
- RNF-10	  El sistema debe estar agilizado para la transferencia de datos.

# 4. Reglas de Negocio
- RN1. Regla de membresía: Todos los clientes deben adquirir una membresía para acceder a las instalaciones y servicios del gimnasio.
- RN2. Regla de pago: Los pagos deben realizarse puntualmente según el plan de membresía seleccionado por el cliente.
- RN3. Regla de cancelación: Los clientes deben seguir el procedimiento establecido para cancelar su membresía, en caso de desearlo, y pueden estar sujetos a tarifas de cancelación.
- RN4  Regla de horarios: El gimnasio debe tener horarios de operación claramente establecidos y comunicados a los clientes.
- RN5. Regla de seguridad: Los clientes deben seguir las normas de seguridad y salud establecidas, incluyendo el uso adecuado del equipo y la limpieza de las áreas después de su uso.
- RN6. Regla de supervisión: Menores de cierta edad deben estar acompañados por un adulto o estar bajo la supervisión del personal del gimnasio en todo momento.
- RN7. Regla de vestimenta: Se debe exigir a los clientes vestir adecuadamente para el ejercicio y seguir un código de vestimenta establecido.
- RN8. Regla de conducta: Se espera que los clientes mantengan un comportamiento respetuoso hacia otros clientes y el personal del gimnasio en todo momento.
- RN9. Regla de reserva: Algunos servicios, como clases grupales o entrenamientos personales, pueden requerir reserva previa.
- RN10. Regla de equipo: Los clientes deben utilizar el equipo de manera adecuada y seguir las instrucciones de uso para evitar lesiones.
- RN11. Regla de limpieza: Los clientes deben limpiar y desinfectar el equipo después de su uso, siguiendo las instrucciones proporcionadas.
- RN12. Regla de prohibición: Está prohibido el uso de sustancias ilegales, alcohol y tabaco dentro de las instalaciones del gimnasio.
- RN13. Regla de salud: Los clientes deben informar al personal del gimnasio sobre cualquier condición médica relevante antes de comenzar cualquier programa de ejercicio.
- RN14. Regla de responsabilidad: El gimnasio no se hace responsable de lesiones o daños personales que puedan ocurrir debido al mal uso del equipo o falta de seguimiento de las instrucciones del personal.
- RN15. Regla de cortesía: Se espera que los clientes respeten los turnos y tiempos de uso del equipo durante los momentos de mayor afluencia.
- RN16. Regla de estacionamiento: Se debe establecer un área de estacionamiento claro y reglas para su uso por parte de los clientes.
- RN17. Regla de nutrición: Se pueden ofrecer servicios de asesoramiento nutricional, pero se debe recordar a los clientes que consulten a un profesional médico antes de realizar cambios significativos en su dieta.
- RN18. Regla de invitados: Se puede permitir que los miembros traigan invitados según las políticas establecidas, como un límite de veces por mes o una tarifa adicional.
- RN19. Regla de renovación: Los clientes deben ser informados sobre la renovación automática de sus membresías y tienen derecho a cancelar esta renovación con anticipación.
- RN20. Regla de comunicación: El gimnasio debe proporcionar canales de comunicación claros para que los clientes puedan hacer preguntas, plantear inquietudes o brindar comentarios sobre su experiencia.
