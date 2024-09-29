import numpy as np
import pandas as pd

# Right side of the vertical axis is negative
class AngularDisplacementCalculator:
    
    
    def getAngle(x, y): # in degrees
        # if x and y are both near 0, then the angle is 0
        if abs(x) < 0.0001 and abs(y) < 0.0001:
            return 0
        return (np.arctan2(y, x) * 180 / np.pi) - 90

    def getAngularDisplacement(x1, y1, x2, y2):
        angle1 = AngularDisplacementCalculator.getAngle(x1, y1)
        angle2 = AngularDisplacementCalculator.getAngle(x2, y2)
        return angle2 - angle1

    def addAngularDisplacement(df):
        angularDisplacements = []
        angularDisplacements.append(0)
        for i in range(1, df.shape[0]):
            x = df.iloc[i]["localX"]
            y = df.iloc[i]["localY"]
            angularDisplacements.append(AngularDisplacementCalculator.getAngle(x, y))
        df = df.copy()
        df["angularDisplacement"] = angularDisplacements
        return df
    #######################################################
    def getAbsoluteAngularDisplacementTable(df):
        angularDisplacementTable=[]
        cumulativeAngularDisplacement=0
        temporaryCumulativeAngularDisplacement=0
        rowSize=df.shape[0]
        frame=df.iloc[0]["frame"]
        

        for i in range(0, df.shape[0]):
            if(i%5 == 0):
                frame=df.iloc[i]["frame"]
                
            temporaryCumulativeAngularDisplacement+=df.iloc[i]["absoluteAngularDisplacement"]
            cumulativeAngularDisplacement+=df.iloc[i]["absoluteAngularDisplacement"]
            if((i+1)%5 == 0 or i==rowSize-1):
                angularDisplacementTable.append((frame,temporaryCumulativeAngularDisplacement))
                temporaryCumulativeAngularDisplacement=0
        return angularDisplacementTable

    #######################################################
    def getRelativeAngularDisplacementTable(df):
        angularDisplacementTable=[]
        cumulativeAngularDisplacement=0
        temporaryCumulativeAngularDisplacement=0
        rowSize=df.shape[0]
        frame=df.iloc[0]["frame"]
        

        for i in range(0, df.shape[0]):
            if(i%5 == 0):
                frame=df.iloc[i]["frame"]
                
            temporaryCumulativeAngularDisplacement+=df.iloc[i]["relativeAngularDisplacement"]
            cumulativeAngularDisplacement+=df.iloc[i]["relativeAngularDisplacement"]
            if((i+1)%5 == 0 or i==rowSize-1):
                angularDisplacementTable.append((frame,temporaryCumulativeAngularDisplacement))
                temporaryCumulativeAngularDisplacement=0
        return angularDisplacementTable




    # Using this
    def addRelativeAngularDisplacement(df):
        relAngularDisplacements = []
        relAngularDisplacements.append(0)
        relAngularDisplacements.append(0)
        
        for i in range(2, df.shape[0]):
            if df.iloc[i]["uniqueTrackId"] != df.iloc[i-1]["uniqueTrackId"]:
                relAngularDisplacements.append(0)
                continue
            if df.iloc[i]["uniqueTrackId"] == df.iloc[i-1]["uniqueTrackId"] and df.iloc[i]["uniqueTrackId"] != df.iloc[i-2]["uniqueTrackId"]:
                relAngularDisplacements.append(0)
                continue
            x1 = df.iloc[i-1]["localX"]
            y1 = df.iloc[i-1]["localY"]
            x2 = df.iloc[i]["localX"]
            y2 = df.iloc[i]["localY"]
            relAngularDisplacements.append(AngularDisplacementCalculator.getAngularDisplacement(x1, y1, x2, y2))
        df = df.copy()
        df["relativeAngularDisplacement"] = relAngularDisplacements
        # add absolute angular displacement
        df["absoluteAngularDisplacement"] = abs(df["relativeAngularDisplacement"])
        return df

    def getMaxAngularDisplacement(df):
        # return the maximum absolute angular displacement
        return max(abs(i) for i in df["angularDisplacement"])

    def getMinAngularDisplacement(df):
        return min(abs(i) for i in df["angularDisplacement"])

    def getMeanAbsoluteAngularDisplacement(df):
        return np.mean(list(abs(i) for i in df["angularDisplacement"]))

    def getMeanAngularDisplacement(df):
        return np.mean(list(i for i in df["angularDisplacement"]))

    def getMaxRelativeAngularDisplacement(df):
        return max(abs(i) for i in df["relativeAngularDisplacement"])

    def getMinRelativeAngularDisplacement(df):
        return min(abs(i) for i in df["relativeAngularDisplacement"])

    def getMeanAbsoluteRelativeAngularDisplacement(df):
        return np.mean(list(abs(i) for i in df["relativeAngularDisplacement"]))

    def getMeanRelativeAngularDisplacement(df):
        return np.mean(list(i for i in df["relativeAngularDisplacement"]))

    def getPedIdList(df):
        return list(df["uniqueTrackId"].unique())
    
    def getMaxSpeed(df):
        return max(df["speed"])
    
    def getMeanSpeed(df):
        return np.mean(list(i for i in df["speed"]))
    

    # create a dataframe with the following columns:
    # pedId, maxAngularDisplacement, minAngularDisplacement, meanAbsoluteAngularDisplacement, meanAngularDisplacement,
    # maxRelativeAngularDisplacement, minRelativeAngularDisplacement, meanAbsoluteRelativeAngularDisplacement, meanRelativeAngularDisplacement
    def getPedAngularDisplacementDf(df):
        pedIds = AngularDisplacementCalculator.getPedIdList(df)
        counts = []
        maxAngularDisplacements = []
        # minAngularDisplacements = []
        meanAbsoluteAngularDisplacements = []
        meanAngularDisplacements = []
        maxRelativeAngularDisplacements = []
        # minRelativeAngularDisplacements = []
        meanAbsoluteRelativeAngularDisplacements = []
        meanRelativeAngularDisplacements = []
        maxSpeeds = []
        meanSpeeds = []
        for pedId in pedIds:
            pedDf = df[df["uniqueTrackId"] == pedId].copy()
            counts.append(pedDf.shape[0])
            pedDf = AngularDisplacementCalculator.addAngularDisplacement(pedDf)
            pedDf = AngularDisplacementCalculator.addRelativeAngularDisplacement(pedDf)
            maxAngularDisplacements.append(AngularDisplacementCalculator.getMaxAngularDisplacement(pedDf))
            # minAngularDisplacements.append(AngularDisplacementCalculator.getMinAngularDisplacement(pedDf))
            meanAbsoluteAngularDisplacements.append(AngularDisplacementCalculator.getMeanAbsoluteAngularDisplacement(pedDf))
            meanAngularDisplacements.append(AngularDisplacementCalculator.getMeanAngularDisplacement(pedDf))
            maxRelativeAngularDisplacements.append(AngularDisplacementCalculator.getMaxRelativeAngularDisplacement(pedDf))
            # minRelativeAngularDisplacements.append(AngularDisplacementCalculator.getMinRelativeAngularDisplacement(pedDf))
            meanAbsoluteRelativeAngularDisplacements.append(AngularDisplacementCalculator.getMeanAbsoluteRelativeAngularDisplacement(pedDf))
            meanRelativeAngularDisplacements.append(AngularDisplacementCalculator.getMeanRelativeAngularDisplacement(pedDf))
            maxSpeeds.append(AngularDisplacementCalculator.getMaxSpeed(pedDf))
            meanSpeeds.append(AngularDisplacementCalculator.getMeanSpeed(pedDf))
        # print(len(pedIds))
        return pd.DataFrame({
            "uniqueTrackId": pedIds,
            "count": counts,
            "maxAngularDisplacement": maxAngularDisplacements,
            # "minAngularDisplacement": minAngularDisplacements,
            "meanAbsoluteAngularDisplacement": meanAbsoluteAngularDisplacements,
            "meanAngularDisplacement": meanAngularDisplacements,
            "maxRelativeAngularDisplacement": maxRelativeAngularDisplacements,
            # "minRelativeAngularDisplacement": minRelativeAngularDisplacements,
            "meanAbsoluteRelativeAngularDisplacement": meanAbsoluteRelativeAngularDisplacements,
            "meanRelativeAngularDisplacement": meanRelativeAngularDisplacements,
            "maxSpeed": maxSpeeds,
            "meanSpeed": meanSpeeds
        })
