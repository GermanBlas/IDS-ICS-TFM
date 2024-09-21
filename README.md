# IDS-ICS-TFM
Este repositorio contiene toda la documentación y material usado en el TFM de Germán Aguilar "Análisis de la capacidad de detección de ataques en entornos ICS del IDS comercial FortiGate bajo la matriz MITRE ATT&CK ICS".       

La arquitectura del GitHub es la siguiente:

*Documentos TFM
	*Memoria. Memoria del TFM
	*Detecciones.xlsx. Análisis de la capacidad de detección de ambos IDS.
	*Mapeos.xlsx. Análisis de las correlaciones de tácticas y técnicas de MITRE con las alertas.

*Configuración IDS y Scripts. 		Contiene los archivos de configuración usados en los dos IDS y los Scripts.
	*IDS [Snort y Fortigate]. 
		*Configuración.
		*Scripts.
		*Reglas [Solo Snort]. 	Tiene 5 conjuntos de reglas, pertenecientes a Talos, ET Open y QuickDraw


*Datasets. 	Contiene todo el material de los datasets usados y los documentos relacionados.
	*Dataset [HIL WDT, ICS1, QuickDraw]
		*README Dataset. 	Contiene información sobre el dataset usado y donde obtenerlo
		*PCAPNGs. 		Contiene los archivos PCAPNG maliciosos
		*PCAPNGs legitimos. 	Contiene los archivos PCAPNG sin trafico malicioso.
		*Documentos generados. 		Dentro están los distintos archivos generados en el procesamiento, validación y análisis de los PCAPNGs.
			*Procesado y validación. 	Archivos generados para la validación de flujos completos.
			*FortiGate			Contiene los logs brutos y procesados de los PCAPNGs analizados por FortiGate	
				*CSV				CSV procesado con campos relevantes para el análisis.
				*CSV_full			CSV con todos los campos de los logs.
				*CSV_ips			CSV procesado con alertas de ataque L1 de FortiGate.
				*CSV_app_ctrl			CSV procesado con alertas de ataque L2 de FortiGate.
			*Snort
				*Conjunto de reglas [Talos: Community y Registered; ET Open: por defecto y Optimizadas; y QuickDraw]
					*análisis_snort. Contiene los logs brutos de Snort de los PCAPNGs analizados por Snort.
					*sids. Contiene los ID de las reglas de los logs procesados de los PCAPNGs.
				*RuleSet [RS2, RS3, RS4]. Combinación de conjuntos de reglas.
					*sids. Contiene los ID de las reglas de los logs procesados de los PCAPNGs.
