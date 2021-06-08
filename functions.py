from packages import * 

f_calibration = lambda x, A, B: A * np.array(x) + np.array(B)
f_gaussian = lambda x, a, b, c: a * np.exp(- (  (np.array(x) - b) ** 2  ) / (2 * c)) 

