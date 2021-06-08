from packages import * 

directory = './datos/'

d_bkg = pd.read_csv(directory + 'background.txt', header = None)


d_cs0 = pd.read_csv(directory + 'Cs137.txt', header = None)


d_cs_al2 = pd.read_csv(directory + 'Cs137-2mmAl.txt', header = None)
d_cs_al4 = pd.read_csv(directory + 'Cs137-4mmAl.txt', header = None)
d_cs_al6 = pd.read_csv(directory + 'Cs137-6mmAl.txt', header = None)
d_cs_al8 = pd.read_csv(directory + 'Cs137-8mmAl.txt', header = None)

d_cs_pb2 = pd.read_csv(directory + 'Cs137-2mmPb.txt', header = None)
d_cs_pb4 = pd.read_csv(directory + 'Cs137-4mmPb.txt', header = None)
d_cs_pb6 = pd.read_csv(directory + 'Cs137-6mmPb.txt', header = None)
d_cs_pb8 = pd.read_csv(directory + 'Cs137-8mmPb.txt', header = None)

d_na = pd.read_csv(directory + 'Na22.txt', header = None)
d_ra = pd.read_csv(directory + 'Ra226.txt', header = None)

