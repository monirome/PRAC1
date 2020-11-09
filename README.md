# Información sobre tenistas femeninas número uno en el ranking WTA


Este codigo extrae la informacion hayada en un [anexo](https://es.wikipedia.org/wiki/Anexo:Tenistas_n%C3%BAmero_1_de_la_WTA) de la web Wikipedia sobre tenistas numero una femeninas de la WTA a lo largo del tiempo, ademas de otras informacion destacada sobre las teninstas numero uno. 

Para este codigo es necesario instalar las siguientes bibliotecas: 

```pip install pandas```
```pip install requests```
```pip install beautifulsoup4 ```

La definicion de las metricas son: 

- Nombre de la jugadora (string). 
- Su fecha de inicio y fin de aparecion número uno en el ranking esta metrica hay que tener cuidado ya que no son fechas en un formato date si no strings del tipo “3 de Noviembre de 1975”. 
- Conteo de semanas tanto consecutivas como semanas totales (integer).
- Pais al que pertenecen las jugadoras (string).
- Nº de tenistas que acumulan el número 1 en el ranking (integer)
- Año en la que fueron número uno (string)
- Nombre del Grand Slam (string).
