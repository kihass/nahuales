##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        TareaExamen1.py
# Purpose:     Exámen práctico de Criptografía
#
# Author:      ISC. Carlos Enrique Quijano Tapia
#
# Created:     22/10/2013
# Copyright:   (c) Kike 2013
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import MyECC

def main():
	from datetime import datetime
	born = datetime.now()

	ecc = MyECC.ECC()

##	partial = datetime.now() # DEBUGG
	ecc.findRationalPoints((1,0,0,1), 5, (-1,-1))
	ecc.buildAddTable()
##	print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG

##	partial = datetime.now() # DEBUGG
	ecc.findRationalPoints((1,3,0,1), 5, (-1,-1))
	ecc.buildAddTable()
##	print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG

	# Tarea
	print('\n\nTarea Examen:')
##	partial = datetime.now() # DEBUGG
	# Usamos cálculos previos (si existen)
	ecc.E = (1,1,0,1)
	ecc.Zp = 10007
	if ecc.ldPreCalc():
		pass
##		print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG

	else:
		ecc.findRationalPoints((1,1,0,1), 10007, (-1,-1))
##		print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG

		# Guardamos datos para ahorrar tiempo en próximas ejecuciones
##		partial = datetime.now() # DEBUGG
		ecc.svPreCalc()
##		print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG


##	partial = datetime.now() # DEBUGG
	P = (7,5300)
	d = 12345
	if P in ecc.rp:
		print('\n%s es el punto racional %s de %s' % (P, ecc.rp.index(P) + 1,
				len(ecc.rp)))
		print('\nCalculamos el orden como: Ord%s = %s' % (P, ecc.orderFast(P)))
##		print('Tiempo parcial consumido: ', datetime.now() - partial) # DEBUGG
		print('\nSí d = %s y P = %s ->' % (d, P), ' Q =', ecc.fndQ(d, P))
##		print('Comprobación lenta: ', ecc.fndQSlow(d,P))
	else:
		print('\n%s no es un punto racional' % P)

	ecc.svData()

	print('\nTiempo consumido: ', datetime.now() - born)


if __name__ == '__main__':
    main()