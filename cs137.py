from load_data import * 
from functions import * 




fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Espectro de Cs137', fontsize=20)
ax.set_ylabel(r'$\Phi$ (Cuentas)', fontsize=20); ax.set_xlabel('Energía (keV)', fontsize=20)

# datos 

pico_1 = 260; pico_2 = 652; x_f_calibration = [pico_1, pico_2]; y_f_calibration = [511, 1274] # keV
a1, C1 = opt.curve_fit(f_calibration, x_f_calibration, y_f_calibration)
print('\najuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + ' \n n = ' + str(np.round(a1[1], 3)) + '\n')

x_energy = f_calibration(np.arange(1, 1025, 1) , *a1)
y_data = d_cs0 - d_bkg 
ax.plot(x_energy, y_data, 'go', markersize=4, label = 'Espectro Cs137')



# forma funcional
n1 = 332; n2 = 343; x_short = x_energy[n1:n2]

y_max = 6000
ax.vlines(x=x_short[0], ymin=-30.00, ymax=y_max, linewidth=2, color='grey', linestyle='dashed')
ax.vlines(x=x_short[-1], ymin=-30.00, ymax=y_max, linewidth=2, color='grey', linestyle='dashed')

param = [5000, 660, 10]
ax.plot(x_short, f_gaussian(x_short, *param), 'b', markersize=4, label = 'forma funcional \n a = ' + str(np.round(param[0], 3)) +
 ' \n b = ' + str(np.round(param[1], 3)) + ' \n c = ' + str(np.round(param[2], 3)))




# ajuste gaussiano
y_short = y_data[0][n1:n2]

a1, C1 = opt.curve_fit(f_gaussian, np.asarray(x_short), np.asarray(y_short), p0 = param)
st = np.sqrt(np.diag(C1))

ax.plot(x_short, f_gaussian(x_short, *a1), 'r', markersize=4, label = 'ajuste gaussiano  \n a = ' + str(np.round(a1[0], 3)) + ' +- ' + str(np.round(st[0], 3)) +
 ' \n b = ' + str(np.round(a1[1], 3)) + ' +- ' + str(np.round(st[1], 3)) + ' \n c = ' + str(np.round(a1[2], 3)) + ' +- ' + str(np.round(st[2], 3)))




ax.legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)

ax.set_ylim([-50, y_max]); ax.set_xlim([640, 700])
ax.set_xticks(np.arange(640, 700, 10)); ax.grid();

plt.savefig('./images/cs137_gaussian.png'); 






fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Espectro de Cs137', fontsize=20)
ax.set_ylabel(r'$\Phi$ (Cuentas)', fontsize=20); ax.set_xlabel('Energía (keV)', fontsize=20)

# datos 

pico_1 = 260; pico_2 = 652; x_f_calibration = [pico_1, pico_2]; y_f_calibration = [511, 1274] # keV
a1, C1 = opt.curve_fit(f_calibration, x_f_calibration, y_f_calibration)

x_energy = f_calibration(np.arange(1, 1025, 1) , *a1)
y_data = d_cs0 
ax.plot(x_energy, y_data, 'g', markersize=4, label = 'Espectro Cs137')


x = [x_energy[15], x_energy[57], x_energy[95], x_energy[240]]
y = [y_data[0][15], y_data[0][57], y_data[0][95], y_data[0][240]] 
ax.plot(x, y, 'ro', markersize=8, label = 'Espectro Cs137')
ax.vlines(x=x[0], ymin=-30.00, ymax=y[0], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[1], ymin=-30.00, ymax=y[1], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[2], ymin=-30.00, ymax=y[2], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[3], ymin=-30.00, ymax=y[3], linewidth=2, color='red', linestyle='dashed')


ax.legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)

ax.set_ylim([-50, 1000]); ax.set_xlim([-100, 800])
ax.set_xticks(np.arange(-100, 800, 100)); ax.grid();

plt.savefig('./images/cs137_all_energies.png'); 