from src.lenden.dataexport import *

dataWithError = DataExport(Version=0.1, HasError=True,
                          DisplayType=DisplayType.grid, Results=[], 
                          Logs=DataLog("Voluptate sint sint eu aliqua consequat culpa nisi fugiat nostrud aute adipisicing.", 
                                       ["/path/log1","/path/log2","/path/log3"]))
print(dataWithError.getJSON())