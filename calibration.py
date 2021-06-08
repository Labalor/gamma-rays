from load_data import * 
from functions import * 


fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(14, 10))
ax[0].set_title('Espectro de Na22 - Con background', fontsize=20)
ax[0].set_ylabel('log(cuentas)', fontsize=20)

y = np.log(d_na)
ax[0].plot(y, 'go', markersize=2, label = 'Na22 con bkg'); ax[0].grid()
ax[0].vlines(x=0, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')
ax[0].vlines(x=1024, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')

ax[0].set_xticks(np.arange(0, 1051, 150))
ax[0].set_xticklabels(np.arange(0, 1051, 150), rotation = 'horizontal', fontsize=15)
ax[0].set_yticklabels([-2, 0, 2, 4, 6, 8], rotation = 'horizontal', fontsize=15)

ax[1].set_title('Espectro de Na22 - Sin background', fontsize=20)
ax[1].set_ylabel('log(cuentas)', fontsize=20); ax[1].set_xlabel('canales', fontsize=20)

y = np.log(d_na - d_bkg)
ax[1].plot(y, 'go', markersize=2, label = 'Na22 sin bkg'); ax[1].grid()
ax[1].set_xticks(np.arange(0, 1051, 150))
ax[1].set_xticklabels(np.arange(0, 1051, 150), rotation = 'horizontal', fontsize=15)
ax[1].set_yticklabels([-2, 0, 2, 4, 6, 8], rotation = 'horizontal', fontsize=15)

ax[1].vlines(x=0, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')
ax[1].vlines(x=1024, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')

ax[0].legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)
ax[1].legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)
plt.savefig('./images/two_d_na_d_bkg.png'); 
# plt.show()


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Identificacion de picos - Espectro de Na22', fontsize=20)
ax.set_ylabel('log(Cuentas)', fontsize=20); ax.set_xlabel('Canales', fontsize=20)

y = np.log(d_na - d_bkg)

ax.plot(y, 'go', markersize=4, label = 'Espectro Na22')

# x = [170, 538]
# y = [y[0][170], y[0][538]]

pico_1 = 260; pico_2 = 652
x = [pico_1, pico_2]
y = [y[0][pico_1], y[0][pico_2]]


ax.plot(x, y, 'ro', markersize=8, label = 'Picos Na22')
ax.vlines(x=0, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')
ax.vlines(x=1024, ymin=0.00, ymax=8.70, linewidth=2, color='grey', linestyle='dashed')
ax.vlines(x=pico_1, ymin=0.00, ymax=8.69, linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=pico_2, ymin=0.00, ymax=7.32, linewidth=2, color='red', linestyle='dashed')

ax.legend(frameon=True, loc='upper right', ncol=1, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(0, 1051, 150)); ax.grid(); 
ax.set_xticklabels(np.arange(0, 1051, 150), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels([-2, 0, 2, 4, 6, 8], rotation = 'horizontal', fontsize=15)

plt.savefig('./images/picos_d_na_d_bkg.png'); 



fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Calibración con Na22', fontsize=20)
ax.set_ylabel('Energía (keV)', fontsize=20); ax.set_xlabel('Canales', fontsize=20)

x = [pico_1, pico_2]
y = [511, 1274] # keV

ax.plot(x, y, 'ko', markersize=8, label = 'Picos Na22')

a1, C1 = opt.curve_fit(f_calibration, x, y)
st = np.sqrt(np.diag(C1))


ax.plot(x, f_calibration(x, *a1), 'r', label = 'ajuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + ' \n n = ' + str(np.round(a1[1], 3)))

ax.legend(frameon=True, loc='upper left', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(230, 700, 50)); ax.grid();
ax.set_yticks(np.arange(400, 1500, 100))

ax.set_xticklabels(np.arange(230, 700, 50), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels(np.arange(400, 1500, 100), rotation = 'horizontal', fontsize=15)

plt.savefig('./images/recta_calibrado.png'); 
# lt.show()






fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Espectro de background', fontsize=20)
ax.set_ylabel(r'$\Phi$ (Cuentas)', fontsize=20); ax.set_xlabel('Energía (keV)', fontsize=20)

x = np.arange(1, 1025, 1) 
x_energy = f_calibration(x, *a1)

y_data = d_bkg
ax.plot(x_energy, y_data, 'g', markersize=4, label = 'Espectro background')
x = [x_energy[122], x_energy[180], x_energy[311], x_energy[572], x_energy[747]]
y = [y_data[0][122], y_data[0][180], y_data[0][311], y_data[0][572], y_data[0][747]] 
ax.plot(x, y, 'ro', markersize=8, label = 'Espectro Ra226')
ax.vlines(x=x[0], ymin=-30.00, ymax=y[0], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[1], ymin=-30.00, ymax=y[1], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[2], ymin=-30.00, ymax=y[2], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[3], ymin=-30.00, ymax=y[3], linewidth=2, color='red', linestyle='dashed')
ax.vlines(x=x[4], ymin=-30.00, ymax=y[4], linewidth=2, color='red', linestyle='dashed')



ax.legend(frameon=True, loc='uppper right', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_ylim([-50, 800]); ax.set_xlim([-100, 2100])
ax.set_xticks(np.arange(-100, 2150, 100)); ax.grid();


plt.savefig('./images/bkg_energy.png'); 




