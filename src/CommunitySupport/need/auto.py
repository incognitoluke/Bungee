import pandas as pd

p = 0

group = []

while True:
    try:
        file = r"D:\Documents\Dev\CS Django\src\CommunitySupport\need\Bergen.csv"
        link_source = pd.read_csv(file)
        link = link_source.iloc[p,0]
        group.append(link)
        p += 1
    except:
        break
print(group)
