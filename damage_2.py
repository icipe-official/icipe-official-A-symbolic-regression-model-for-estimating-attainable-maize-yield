import numpy as np
import pandas as pd


# Your function

def solution_45(Temperatur, row):
    return 46.3917-np.tan(0.834691*(0.999257-row-0.00024874))-(-0.00507619-row+np.sqrt(-0.0177625+row)+(np.sqrt(2.154/(row+Temperatur))/np.cos(0.591531+Temperatur)))

dataValu = pd.read_csv("Africa_6km_sq_2.csv").to_numpy()

temperatureValu = dataValu[:,0]
rowwValu = dataValu[:,1]

regionValu = dataValu[:,2:4]

damageValu = solution_45(temperatureValu, rowwValu)


data = pd.DataFrame(np.concatenate((regionValu, damageValu.reshape(damageValu.shape[0],1)), axis=1))
data.columns = ["longitude", "latitide", "damage"]

pd.DataFrame(data).to_csv("outputDamage.csv", index=None)
