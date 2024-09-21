# IDS-ICS-TFM
Este repositorio contiene toda la documentación y material usado en el TFM de Germán Aguilar "Análisis de la capacidad de detección de ataques en entornos ICS del IDS comercial FortiGate bajo la matriz MITRE ATT&CK ICS".

La arquitectura del GitHub es la siguiente:

*Documentos TFM

&emsp;&emsp;*Memoria. Memoria del TFM

&emsp;&emsp;&emsp;&emsp;*Detecciones.xlsx. Análisis de la capacidad de detección de ambos IDS.

&emsp;&emsp;&emsp;&emsp;*Mapeos.xlsx. Análisis de las correlaciones de tácticas y técnicas de MITRE con las alertas.



*Configuración IDS y Scripts. 		Contiene los archivos de configuración usados en los dos IDS y los Scripts.

 &emsp;&emsp;*IDS [Snort y Fortigate]. 
 
&emsp;&emsp;&emsp;&emsp;*Configuración.

&emsp;&emsp;&emsp;&emsp;*Scripts.

&emsp;&emsp;&emsp;&emsp;*Reglas [Solo Snort]. 	Tiene 5 conjuntos de reglas, pertenecientes a Talos, ET Open y QuickDraw



*Datasets. 	Contiene todo el material de los datasets usados y los documentos relacionados.

&emsp;&emsp;*Dataset [HIL WDT, ICS1, QuickDraw]

&emsp;&emsp;&emsp;&emsp;*README Dataset. 	Contiene información sobre el dataset usado y donde obtenerlo

&emsp;&emsp;&emsp;&emsp;*PCAPNGs. 		Contiene los archivos PCAPNG maliciosos

&emsp;&emsp;&emsp;&emsp;*PCAPNGs legítimos. 	Contiene los archivos PCAPNG sin tráfico malicioso.

&emsp;&emsp;&emsp;&emsp;*Documentos generados. 		Dentro están los distintos archivos generados en el procesamiento, validación y análisis de los PCAPNGs.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*Procesado y validación. 	Archivos generados para la validación de flujos completos.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*FortiGate			Contiene los logs brutos y procesados de los PCAPNGs analizados por FortiGate

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*CSV				CSV procesado con campos relevantes para el análisis.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*CSV_full			CSV con todos los campos de los logs.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*CSV_ips			CSV procesado con alertas de ataque L1 de FortiGate.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*CSV_app_ctrl			CSV procesado con alertas de ataque L2 de FortiGate.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*Snort

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*Conjunto de reglas [Talos: Community y Registered; ET Open: por defecto y Optimizadas; y QuickDraw]

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*análisis_snort. Contiene los logs brutos de Snort de los PCAPNGs analizados por Snort.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*sids. Contiene los ID de las reglas de los logs procesados de los PCAPNGs.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*RuleSet [RS2, RS3, RS4]. Combinación de conjuntos de reglas.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*sids. Contiene los ID de las reglas de los logs procesados de los PCAPNGs.
