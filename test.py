#Just a piece of code to do random stuff needed
listToChange = ["RadarFailure", "Fog", "EnvironmentalObstacles", "Visibility", "HighSpeed", "HumanFactor", "Navigation", "EquipmentError", "DetectionFailure", 
             "RidgeIceAndIceberg", "PackIce", "HighWind", "Waves", "PackIceEffect", "NondetectedMultiLayerIce", "RidgeIceAndIcebergEffect", "WaveEffect", 
             "FaultOfOtherVessels", "IceBreakersFailure", "DangerousIceCondition", "TypeOfExpedition", 'EnvironmentalOperationalEffects', "PotentialObstacles", "Collision"]

for i in range(len(listToChange)):
    listToChange[i] = listToChange[i].lower()

print(listToChange)