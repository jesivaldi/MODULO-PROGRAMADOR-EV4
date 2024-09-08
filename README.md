# MODULO-PROGRAMADOR-EV4

Docentes: Programacion I :ROJAS, CÓRSICO IVANA / Base de datos: GERLERO, MARTÍN

Alumno: VALDIVIA JESICA- 34980147

Evidencia Nº4

### Tema: MÁQUINA SOPLADORA DE BOTELLAS

**Objetivo**: Diseñar y desarrollar una clase en Python que represente un objeto con funcionalidad
lógica, aplicando TDD, conceptos de POO y diseñando la base de datos correspondiente.

### DESCRIPCIÓN OBJETO: MÁQUINA SOPLADORA DE BOTELLAS
La máquina de soplado de botellas es un equipo especializado utilizado en la industria del envasado para fabricar botellas de plástico, generalmente de PET . A continuación Se detalla
de cómo es el proceso general de una máquina de este tipo:

1-Carga de Preformas

2-Calentamiento de Preformas

3-Transferencia al Molde

4-Soplado

5-Enfriamiento y Desmoldeado

6-Inspección y Recolección

## COMPORTAMIENTOS CLAVES DEL OBEJTO:

### -CONTROL DE LA TEMPERTATURA PARA PROFORMAS.

La temperatura ideal es de 90 a 120º aprox, se debe mantener esta temperatura para el buen modelado.

 *Obejtivo logico*: Establecer una temperatura ideal y monitorearla constantemente con la tempertura actual del calentador.Si la temperatura es alta, la máquina debe bajarla automáticamente y viceversa.
 
### -CONTROL DE LA PRESION DURANTE EL SOPLADO.

La presión del aire utilizada para soplar las preformas dentro de los moldes debe ajustarse según el material 
y el tamaño de la botella la presión ideal suele estar entre 25 a 40 bares. Una presión inadecuada podría deformar la botella o no llenarla completamente.

 *Obejtivo lógico*: Establecer una presion ideal y monitorearla constantemente con la presion actual en base al material y tamaño. En caso que la presion este fuera de la presion ideal la máquina debe 
 ajustarla automáticamente.
 
### -CALCULO DEL TIEMPO DE SOPLADO BASADO EN EL TAMAÑO DE LA PROFORMA.
En base al tamaño de la proforma el tiempo de soplado es diferente mientras mas grande es mayor el tiempo.

*Obejtivo lógico*: la maquina debe calcular el tiempo necesario segun el tamaño de la proforma.
 



