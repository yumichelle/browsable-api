import numpy as np
import pandas as pd
import os

class API:
    def __init__(self, inputfile, outputfile) -> None:
        self.input = pd.read_csv(inputfile)  # dataframe
        self.outputfile = outputfile
        print('api.py input \n', input, '\t output', self.outputfile)


    def square(x):
        return x * x
    
    def half(x):
        print('half function: x is', x)
        return (x/2).apply(lambda x: float(x))
        
    def main(self):
        print('api.py main\n', type(self.input)) # type(self.input) = <class 'pandas.core.frame.DataFrame'>
        # loop thru DataFrame:
        # l = len(input)
        # for i in range(l):
            # row = input['Pulse'].iloc[i] / 2
            # # half each val
            # input['Pulse3'] = self.half(row)

        self.input['Pulse3'] = API.half(self.input['Pulse'])
        
        if not os.path.exists(self.outputfile):
            os.makedirs(self.outputfile)

        self.input.to_csv(self.outputfile+'data2.csv' , index=False)
        print('done with api.py')