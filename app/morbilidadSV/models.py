from __future__ import unicode_literals

from django.db import models

class Morbilidad(models.Model):
	#Definiendo valores de la lista departamentos
	AHUACHAPAN='Ahuachapan'
	SONSONATE='Sonsonate'
	SANTA_ANA='Santa ana'

	CABANAS='Cabanas'
	CHALATENANGO='Chalatenango'
	CUSCATLAN='Cuscatlan'
	LA_LIBERTAD='La Libertad'
	LA_PAZ='La Paz'
	SAN_SALVADOR='San Salvador'
	SAN_VICENTE='San Vicente'
	
	MORAZAN='Morazan'
	SAN_MIGUEL='San Miguel'
	USULUTAN='Usulutan'
	LA_UNION='La Union'

	#lista anios
	A2014=2014
	A2015=2015

	#lista meses
	ENERO='Enero'
	FEBRERO='Febrero'
	MARZO='Marzo'
	ABRIL='Abril'
	MAYO='Mayo'
	JUNIO='Junio'
	JULIO='Julio'
	AGOSTO='Agosto'
	SEPTIEMBRE='Septiembre'
	OCTUBRE='Octubre'
	NOVIEMBRE='Noviembre'
	DICIEMBRE='Diciembre'


	nombre = models.CharField(max_length=100)
	nom_departamento_opciones=(
	
	(AHUACHAPAN, 'Ahuachapan'),
	(SONSONATE,'Sonsonate'),
	(SANTA_ANA,'Santa ana'),
	(CABANAS,'Cabanas'),
	(CHALATENANGO,'Chalatenango'),
	(CUSCATLAN,'Cuscatlan'),
	(LA_LIBERTAD,'La Libertad'),
	(LA_PAZ,'La Paz'),
	(SAN_SALVADOR,'San Salvador'),
	(SAN_VICENTE,'San Vicente'),
	(MORAZAN,'Morazan'),
	(SAN_MIGUEL,'San Miguel'),
	(USULUTAN,'Usulutan'),
	(LA_UNION,'La Union'),



		)
	nom_departamento = models.CharField(
		max_length=50,
		choices=nom_departamento_opciones,
		default=SAN_SALVADOR,

		)
	anio_opciones=(
		(A2014,'2014'),
		(A2015,'2015'),
		
	)

	anio = models.IntegerField(
		choices=anio_opciones,
		default=A2014,
		)
	mes_opciones=(

	(ENERO,'Enero'),
	(FEBRERO,'Febrero'),
	(MARZO,'Marzo'),
	(ABRIL,'Abril'),
	(MAYO,'Mayo'),
	(JUNIO,'Junio'),
	(JULIO,'Julio'),
	(AGOSTO,'Agosto'),
	(SEPTIEMBRE,'Septiembre'),
	(OCTUBRE,'Octubre'),
	(NOVIEMBRE,'Noviembre'),
	(DICIEMBRE,'Diciembre'),
		)
	mes = models.CharField(
		max_length=15,
		choices=mes_opciones,
		default=ENERO,

		)
	cantidad = models.IntegerField()

