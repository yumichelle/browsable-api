import numpy as np
import pandas as pd

class API:
    def __init__(self, inputfile, outputfile) -> None:
        input = pd.read_csv(inputfile)  # dataframe
        self.outputfile = outputfile

    def square(x):
        return x * x
    
    def half(x):
        return float(x/2)
        
    def main(self):
        # loop thru df
        l = len(input)
        for i in range(l):
            row = input['Pulse'].iloc[i] / 2
            # half each val
            input['Pulse3'] = self.half(row)

        input.to_csv(self.outputfile ,index=False)