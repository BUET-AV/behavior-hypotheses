import pandas as pd
from typing import *
import os
import matplotlib.pyplot as plt
import numpy as np

class TrajectoryVisualizer:

    
    def show(self, df: pd.DataFrame, idCol, xCol, yCol, trackIds=None):
        plt.rc('font', size=10)
        # print the length of yCol and xCol
        # print(f"ycol length {len(df[yCol])}")
        # print(f"xcol length {len(df[xCol])}")
        fig = plt.figure()
        # fig.set_xlabel('Sample Value', fontsize=20)
        ax = fig.add_subplot()
        total_diff = 0
        
        
        
        if trackIds is None:
            trackIds = df[idCol].unique()
            # length of trackIds
            # print(f"trackIds length {len(trackIds)}")


        for trackId in trackIds:
            diff = 0
            trackDf = df[df[idCol] == trackId]
            plt.plot(trackDf[xCol], trackDf[yCol])
            if False:
                for i in range(len(trackDf[xCol])):
                    ax.plot([trackDf[xCol][i], 0], [trackDf[yCol][i], trackDf[yCol][i]])
            # ax.set_xlabel('Sample Value', fontsize=20)
            

            # plot direction
            lastRow = trackDf.tail(1)
            endPoint = (lastRow[xCol] , lastRow[yCol])
            # print(f"end point {endPoint[0].values[0]}")
            firstRow = trackDf.head(1)
            startPoint = (firstRow[xCol] , firstRow[yCol])
            # print(f"start point {startPoint[0].values[0]}")
            # print(startPoint[0].values[0], startPoint[1].values[0])
            for col in trackDf[xCol]:
                diff += abs(col - startPoint[0].values[0])   
            plt.plot(endPoint[0], endPoint[1], marker='x')
            # diff = abs(endPoint[0].values[0] - startPoint[0].values[0])
            # print(f"diff {diff}")
            total_diff += (diff / len(trackDf[xCol]))
            
            
        avg_displacement_error = total_diff / len(trackIds)
        # print(f"ADE : {avg_displacement_error}")
        
        # Sampling 
        
        
        
        # plt.plot(avg_displacement_error, 0, marker='x', color="red")
        # plt.axvline(x=avg_displacement_error, color='r', linestyle='--')
        # plt.axvline(x=0, color='r', linestyle='--')
        
        ax.set_xlabel('Lateral Shift (m)')
        ax.set_ylabel('Road Width (m)')
        ax.set_aspect('equal', adjustable='box')
        #for scene 10 midvis
        # plt.ylim(0,5)
        # plt.xlim(-4,3) 
        #for scene 30 midvis
        # plt.ylim(0,5)
        # plt.xlim(-1,6)
        #for scene 10 endvis
        # plt.ylim(0,7)
        # plt.xlim(-5,4)
        # for scene 30 endvis
        # plt.ylim(0,7)
        # plt.xlim(-1,8)
        plt.tight_layout()
        plt.show()
