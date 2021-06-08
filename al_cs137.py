from load_data import * 
from functions import * 


pico_1 = 260; pico_2 = 652; x_f_calibration = [pico_1, pico_2]; y_f_calibration = [511, 1274] # keV
a1, C1 = opt.curve_fit(f_calibration, x_f_calibration, y_f_calibration)

x_energy = f_calibration(np.arange(1, 1025, 1) , *a1)


al_cs137 = [d_cs_al2, d_cs_al4, d_cs_al6, d_cs_al8]
al_cs137_name = ['al2_', 'al4_', 'al6_', 'al8_']
a_al = []; b_al = []; c_al = []

print('\n\n         Cs137 con Al: ')
print('         Valores del ajuste gaussiano \n')

for i in range(len(al_cs137)):


	fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
	ax.set_title('Espectro de Cs137 - Al 2 mm', fontsize=20)
	ax.set_ylabel(r'$\Phi$ (Cuentas)', fontsize=20); ax.set_xlabel('Energía (keV)', fontsize=20)

	# datos 


	y_data = al_cs137[i] - d_bkg # d_cs0
	ax.plot(x_energy, y_data, 'go', markersize=4, label = 'Espectro Cs137')



	# forma funcional
	n1 = 332; n2 = 343; x_short = x_energy[n1:n2]

	y_max = 6000
	ax.vlines(x=x_short[0], ymin=-30.00, ymax=y_max, linewidth=2, color='grey', linestyle='dashed')
	ax.vlines(x=x_short[-1], ymin=-30.00, ymax=y_max, linewidth=2, color='grey', linestyle='dashed')

	param = [5000, 660, 10]


	# ajuste gaussiano
	y_short = y_data[0][n1:n2]

	a1, C1 = opt.curve_fit(f_gaussian, np.asarray(x_short), np.asarray(y_short), p0 = param)
	st = np.sqrt(np.diag(C1))

	ax.plot(x_short, f_gaussian(x_short, *a1), 'r', markersize=4, label = 'ajuste gaussiano  \n a = ' + str(np.round(a1[0], 3)) + ' +- ' + str(np.round(st[0], 3)) +
	 ' \n b = ' + str(np.round(a1[1], 3)) + ' +- ' + str(np.round(st[1], 3)) + ' \n c = ' + str(np.round(a1[2], 3)) + ' +- ' + str(np.round(st[2], 3)))

	print('\n' + '----' + al_cs137_name[i][:-1] + '----')
	print('Parameter    Value       Stderr')
	name = ['a', 'b', 'c'] 
	for val in range(len(name)):
	    print('{:2s} {:11.2f} {:11.2f}'.format(name[val], a1[val], st[val]))

	a_al.append([al_cs137_name[i] + 'a', a1[0], st[0]])		
	b_al.append([al_cs137_name[i] + 'b', a1[1], st[1]])	
	c_al.append([al_cs137_name[i] + 'c', a1[2], st[2]])

	ax.legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)

	ax.set_ylim([-50, y_max]); ax.set_xlim([640, 700])
	ax.set_xticks(np.arange(640, 700, 10)); ax.grid();

	plt.savefig('./images/' + al_cs137_name[i] + 'cs137_gaussian.png') 

print('\n')


