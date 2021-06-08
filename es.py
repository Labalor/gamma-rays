from al_cs137 import *
from pb_cs137 import *

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Sección eficaz - Al', fontsize=20)
ax.set_ylabel(r'ln($\Phi$) (cuentas)', fontsize=20); ax.set_xlabel('x (cm)', fontsize=20)

x = [0.2, 0.4, 0.6, 0.8] 
a_al_value = []; a_al_value_err = []
c_al_value = []; c_al_value_err = []
for i in range(4): 
	a_al_value.append(a_al[i][1]) 
	a_al_value_err.append(a_al[i][2]) 
	c_al_value.append(c_al[i][1]) 
	c_al_value_err.append(c_al[i][2]) 

a_al_value = np.asarray(a_al_value)
a_al_value_err = np.asarray(a_al_value_err)
c_al_value = np.asarray(c_al_value)
c_al_value_err = np.asarray(c_al_value_err)

A_al = np.sqrt(2*np.pi) * a_al_value * c_al_value
A_al_err = ( np.sqrt(2*np.pi) / A_al ) * np.sqrt( (a_al_value * c_al_value_err) ** 2 + (c_al_value * a_al_value_err) ** 2 )

y = np.log(A_al)
y_err = A_al_err

# ax.plot(x, y, 'ko', markersize=8, label = 'area')
ax.errorbar(x, y, yerr = y_err, fmt = 'ko', markersize=8, label = 'area')


a1, C1 = opt.curve_fit(f_calibration, x, y, sigma = y_err, absolute_sigma=True)
st = np.sqrt(np.diag(C1))


ax.plot(x, f_calibration(x, *a1), 'r', label = 'ajuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + r' $\pm$ ' + str(np.round(st[0], 3)) +
	' \n n = ' + str(np.round(a1[1], 3)) + r' $\pm$ ' + str(np.round(st[1], 3)))

ax.legend(frameon=True, loc='lower left', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(0.1, 0.9, 0.1)); ax.grid();
'''

ax.set_yticks(np.arange(400, 1500, 100))

ax.set_xticklabels(np.arange(230, 700, 50), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels(np.arange(400, 1500, 100), rotation = 'horizontal', fontsize=15)
'''
plt.savefig('./images/al_es.png')









fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Sección eficaz - Pb', fontsize=20)
ax.set_ylabel(r'ln($\Phi$) (cuentas)', fontsize=20); ax.set_xlabel('x (cm)', fontsize=20)

x = [0.2, 0.4, 0.6, 0.8] 
a_pb_value = []; a_pb_value_err = []
c_pb_value = []; c_pb_value_err = []
for i in range(4): 
	a_pb_value.append(a_pb[i][1]) 
	a_pb_value_err.append(a_pb[i][2]) 
	c_pb_value.append(c_pb[i][1]) 
	c_pb_value_err.append(c_pb[i][2]) 

a_pb_value = np.asarray(a_pb_value)
a_pb_value_err = np.asarray(a_pb_value_err)
c_pb_value = np.asarray(c_pb_value)
c_pb_value_err = np.asarray(c_pb_value_err)

A_pb = np.sqrt(2*np.pi) * a_pb_value * c_pb_value
A_pb_err = ( np.sqrt(2*np.pi) / A_pb ) * np.sqrt( (a_pb_value * c_pb_value_err) ** 2 + (c_pb_value * a_pb_value_err) ** 2 )

y = np.log(A_pb)
y_err = A_pb_err

# ax.plot(x, y, 'ko', markersize=8, label = 'area')
ax.errorbar(x, y, yerr = y_err, fmt = 'ko', markersize=8, label = 'area')

a1, C1 = opt.curve_fit(f_calibration, x, y, sigma = y_err, absolute_sigma=True)
st = np.sqrt(np.diag(C1))


ax.plot(x, f_calibration(x, *a1), 'r', label = 'ajuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + r' $\pm$ ' + str(np.round(st[0], 3)) +
	' \n n = ' + str(np.round(a1[1], 3)) + r' $\pm$ ' + str(np.round(st[1], 3)))

ax.legend(frameon=True, loc='lower left', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(0.1, 0.9, 0.1)); ax.grid();
'''

ax.set_yticks(np.arange(400, 1500, 100))

ax.set_xticklabels(np.arange(230, 700, 50), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels(np.arange(400, 1500, 100), rotation = 'horizontal', fontsize=15)
'''
plt.savefig('./images/pb_es.png')





from al_cs137 import *
from pb_cs137 import *

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Sección eficaz - Al', fontsize=20)
ax.set_ylabel(r'ln($\Phi$) (cuentas)', fontsize=20); ax.set_xlabel('x (cm)', fontsize=20)

x = [0.2, 0.4, 0.6, 0.8] 
a_al_value = []; a_al_value_err = []
c_al_value = []; c_al_value_err = []
for i in range(4): 
	a_al_value.append(a_al[i][1]) 
	a_al_value_err.append(a_al[i][2]) 
	c_al_value.append(c_al[i][1]) 
	c_al_value_err.append(c_al[i][2]) 

a_al_value = np.asarray(a_al_value)
a_al_value_err = np.asarray(a_al_value_err)
c_al_value = np.asarray(c_al_value)
c_al_value_err = np.asarray(c_al_value_err)

A_al = np.sqrt(2*np.pi) * a_al_value * c_al_value
A_al_err = ( np.sqrt(2*np.pi) / A_al ) * np.sqrt( (a_al_value * c_al_value_err) ** 2 + (c_al_value * a_al_value_err) ** 2 )

y = np.log(A_al)
y_err = A_al_err

# ax.plot(x, y, 'ko', markersize=8, label = 'area')
ax.errorbar(x, y, yerr = y_err, fmt = 'ko', markersize=8, label = 'area')


a1, C1 = opt.curve_fit(f_calibration, x, y)
st = np.sqrt(np.diag(C1))


ax.plot(x, f_calibration(x, *a1), 'r', label = 'ajuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + r' $\pm$ ' + str(np.round(st[0], 3)) +
	' \n n = ' + str(np.round(a1[1], 3)) + r' $\pm$ ' + str(np.round(st[1], 3)))

ax.legend(frameon=True, loc='lower left', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(0.1, 0.9, 0.1)); ax.grid();
'''

ax.set_yticks(np.arange(400, 1500, 100))

ax.set_xticklabels(np.arange(230, 700, 50), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels(np.arange(400, 1500, 100), rotation = 'horizontal', fontsize=15)
'''
plt.savefig('./images/al_es_without.png')









fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
ax.set_title('Sección eficaz - Pb', fontsize=20)
ax.set_ylabel(r'ln($\Phi$) (cuentas)', fontsize=20); ax.set_xlabel('x (cm)', fontsize=20)

x = [0.2, 0.4, 0.6, 0.8] 
a_pb_value = []; a_pb_value_err = []
c_pb_value = []; c_pb_value_err = []
for i in range(4): 
	a_pb_value.append(a_pb[i][1]) 
	a_pb_value_err.append(a_pb[i][2]) 
	c_pb_value.append(c_pb[i][1]) 
	c_pb_value_err.append(c_pb[i][2]) 

a_pb_value = np.asarray(a_pb_value)
a_pb_value_err = np.asarray(a_pb_value_err)
c_pb_value = np.asarray(c_pb_value)
c_pb_value_err = np.asarray(c_pb_value_err)

A_pb = np.sqrt(2*np.pi) * a_pb_value * c_pb_value
A_pb_err = ( np.sqrt(2*np.pi) / A_pb ) * np.sqrt( (a_pb_value * c_pb_value_err) ** 2 + (c_pb_value * a_pb_value_err) ** 2 )

y = np.log(A_pb)
y_err = A_pb_err

# ax.plot(x, y, 'ko', markersize=8, label = 'area')
ax.errorbar(x, y, yerr = y_err, fmt = 'ko', markersize=8, label = 'area')

a1, C1 = opt.curve_fit(f_calibration, x, y)
st = np.sqrt(np.diag(C1))


ax.plot(x, f_calibration(x, *a1), 'r', label = 'ajuste lineal (y = mx + n) \n m = ' + str(np.round(a1[0], 3)) + r' $\pm$ ' + str(np.round(st[0], 3)) +
	' \n n = ' + str(np.round(a1[1], 3)) + r' $\pm$ ' + str(np.round(st[1], 3)))

ax.legend(frameon=True, loc='lower left', ncol=2, fontsize=15, shadow=True, borderpad=1)
ax.set_xticks(np.arange(0.1, 0.9, 0.1)); ax.grid();
'''

ax.set_yticks(np.arange(400, 1500, 100))

ax.set_xticklabels(np.arange(230, 700, 50), rotation = 'horizontal', fontsize=15)
ax.set_yticklabels(np.arange(400, 1500, 100), rotation = 'horizontal', fontsize=15)
'''
plt.savefig('./images/pb_es_without.png')