from load_data import * 
from functions import * 






fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Espectro de Ra226', fontsize=20)
ax.set_ylabel(r'$\Phi$ (Cuentas)', fontsize=20); ax.set_xlabel('Energía (keV)', fontsize=20)

# datos 

pico_1 = 260; pico_2 = 652; x_f_calibration = [pico_1, pico_2]; y_f_calibration = [511, 1274] # keV
a1, C1 = opt.curve_fit(f_calibration, x_f_calibration, y_f_calibration)

x_energy = f_calibration(np.arange(1, 1025, 1) , *a1)
y_data = d_ra - d_bkg
ax.plot(x_energy, y_data, 'g', markersize=4, label = 'Espectro Ra226')

x = [x_energy[39], x_energy[95], x_energy[124], x_energy[151], x_energy[180], x_energy[311], x_energy[392]]
y = [y_data[0][39], y_data[0][95], y_data[0][124], y_data[0][151], y_data[0][180], y_data[0][311], y_data[0][392]] 
ax.plot(x, y, 'ro', markersize=8, label = 'Espectro Ra226')
ax.vlines(x=x[0], ymin=-30.00, ymax=y[0], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[1], ymin=-30.00, ymax=y[1], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[2], ymin=-30.00, ymax=y[2], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[3], ymin=-30.00, ymax=y[3], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[4], ymin=-30.00, ymax=y[4], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[5], ymin=-30.00, ymax=y[5], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[6], ymin=-30.00, ymax=y[6], linewidth=2, color='red', linestyle='dashed')


ax.legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)

# ax.set_ylim([-50, 1000]); ax.set_xlim([-100, 800])
ax.set_xticks(np.arange(-100, 2100, 100)); ax.grid();

plt.savefig('./images/ra226_all_energies.png'); 