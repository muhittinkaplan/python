import pandas as pd

dataFrame=pd.read_csv("nba_all_elo.csv")
pd.set_option("display.max.columns", None)
print("Head\n",dataFrame.head(100))
print("Shape\n",dataFrame.shape)
print("Keys\n",dataFrame.keys())
print("Head\n",dataFrame.head(1))
print("Tail\n",dataFrame.tail(1))
print("Spec Data\n",dataFrame['game_id'][0])