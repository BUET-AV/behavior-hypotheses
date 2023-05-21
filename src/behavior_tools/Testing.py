import pandas as pd
from typing import *
import scipy.stats as stats
# import os
# import matplotlib.pyplot as plt
import numpy as np
from behavior_tools.TrajectoryADECalculator import TrajectoryADECalculator
from tti_dataset_tools.ColMapper import ColMapper
from behavior_tools.Sampler import Sampler



adeCalculator = TrajectoryADECalculator()
sampler = Sampler()
colMapper = ColMapper(
        idCol='uniqueTrackId', 
        xCol='sceneX', 
        yCol='sceneY',
        xVelCol='sceneXVelocity', 
        yVelCol='sceneYVelocity',
        xAccCol='sceneXAcceleration',
        yAccCol='sceneYAcceleration',
        speedCol='speed',
        accelerationCol='acceleration',
    )

class TrajectoryTestingCalculator:
    
    
    def getT_statistic_p_value(self, tracksDf : pd.DataFrame, idCol, xCol, yCol):
        
        print(type(idCol))
        
        sampleDf1 = sampler.getRandom(tracksDf, idCol = 'uniqueTrackId', n=10)
        aade1 = adeCalculator.getAADE(sampleDf1, idCol, xCol, yCol)
        ades1 = adeCalculator.getADEs(sampleDf1, idCol = 'uniqueTrackId', xCol = 'localX', yCol = 'localY')
        print(aade1)
        
        sampleDf2 = sampler.getRandom(tracksDf, idCol = 'uniqueTrackId', n=10)
        aade2 = adeCalculator.getAADE(sampleDf2, idCol = 'uniqueTrackId', xCol = 'localX', yCol = 'localY')
        ades2 = adeCalculator.getADEs(sampleDf2, idCol = 'uniqueTrackId', xCol = 'localX', yCol = 'localY')
        print(aade2)
        
        t_statistic, p_value = stats.ttest_ind(ades1, ades2)
        
        alpha_value = 0.005

        # Print the results
        print("T-Statistic:", t_statistic)
        print("P-Value:", p_value)
        
        if(p_value<alpha_value):
            print("The null hypothesis is rejected")
        else:
            print("The null hypothesis is accepted")
        
        
        
        return t_statistic,p_value

    
        


