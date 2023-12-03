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

    def addRelativeAngularDisplacement(df):
        relAngularDisplacements = []
        relAngularDisplacements.append(0)
        for i in range(1, df.shape[0]):
            x1 = df.iloc[i-1]["localX"]
            y1 = df.iloc[i-1]["localY"]
            x2 = df.iloc[i]["localX"]
            y2 = df.iloc[i]["localY"]
            relAngularDisplacements.append(AngularDisplacementCalculator.getAngularDisplacement(x1, y1, x2, y2))
        df = df.copy()
        df["relativeAngularDisplacement"] = relAngularDisplacements
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
        print(len(pedIds))
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
            "meanRelativeAngularDisplacement": meanRelativeAngularDisplacements
        })
