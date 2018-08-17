import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



shot_df = pd.read_csv("./csvData/NBA_Shot_dist - Sheet2.csv")
guard_df = pd.read_csv("./csvData/NBA_Shot_dist - guard_list.csv")
forward_df = pd.read_csv("./csvData/NBA_Shot_dist - forwards_list.csv")
center_df = pd.read_csv("./csvData/NBA_Shot_dist - center_list.csv")
heightWeight_df = pd.read_csv("./csvData/playerHeight.csv")
salary_df = pd.read_csv("./csvData/playerSalaries.csv")
dribble_df = pd.read_csv("./csvData/NBA_Shot_dist - dribble stats.csv")

for col in salary_df.select_dtypes([np.object]):

    salary_df[col] = salary_df[col].str.lstrip('$')
salary_df = salary_df.replace(regex={',':''})
salary_df = salary_df.iloc[:,[1,2]]
salary_df.columns = ['name', 'salary']

heightWeight_df = heightWeight_df.iloc[:,[0,7,9]]

shot_df.columns = ['name', 'team', 'szn', 'type', 'games',
              '0to8_make', '8to16_make', '16to24_make', '24plus_make', 'bcMake',
              '0to8_att', '8to16_att', '16to24_att', '24plus_att', 'bcatt',
              'avg_dist', 'avg_madeDist', 'avg_missDist']

gen_df = pd.read_csv("./csvData/NBA_Shot_dist - gen_stats.csv")
gen_df = gen_df.iloc[:, [0,19,20,22,23]]
gen_df.columns = ['name','reb','ast','stl','blk',]

position_df = pd.concat([guard_df, forward_df, center_df])
position_df = position_df.groupby(['name'], as_index = False).sum()

dribble_df = dribble_df.iloc[:,[0,11,14,15]]
dribble_df.columns = ['name', 'avgDrib', 'post', 'paint']

df = pd.merge(heightWeight_df, shot_df, how='inner')
df = pd.merge(df,gen_df, how='inner')
df = pd.merge(df,dribble_df, how='inner')
df = pd.merge(df,salary_df, how='inner')
df = pd.merge(df, position_df, how='inner')

del df['0to8_att']
del df['8to16_att']
del df['16to24_att']
del df['24plus_att']
del df['bcatt']
del df['bcMake']
del df['avg_missDist']
del df['avg_dist']
del df['team']
del df['szn']
del df['type']

x = df.iloc[:, 1:16]
x['heightMeters'] = x['heightMeters']**3
x['weightKilograms'] = x['weightKilograms']**3
x['avg_madeDist'] = x['avg_madeDist']**3
x['reb'] = x['reb']**2
x['avgDrib'] = x['avgDrib']**2
x['games'] = (x['games'])/82

y = df.iloc[:, 17:20]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

""" RANDOM FOREST PREDICTION """

# X, y = make_classification(n_samples=100, n_features=5, n_informative=5, n_redundant=0, random_state=0, shuffle=False)

clf = RandomForestClassifier(n_estimators=120, max_depth=15, random_state=0)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred), " -- Accuracy with Random Forests\n")
print("-------------- Importances per column with RF")
print((clf.feature_importances_), "\n")

y1 = y.iloc[:,0]
x_train, x_test, y1_train, y1_test = train_test_split(x, y1, test_size=.3)
#y2 = y.iloc[:,1]
#X_train, X_test, y2_train, y2_test = train_test_split(X, y2, test_size=.3)
#y3 = y.iloc[:,2]
#X_train, X_test, y3_train, y3_test = train_test_split(X, y3, test_size=.3)

# Use silhouette score to find optimal number of clusters to segment the data
num_clusters = np.arange(2,10)
results = {}
for size in num_clusters:
    model = KMeans(n_clusters = size).fit(x)
    predictions = model.predict(x)
    results[size] = silhouette_score(x, predictions)

best_size = max(results, key=results.get)
# best_size

kmeans = KMeans(n_clusters= 2)
kmeans = kmeans.fit(x)

labels = kmeans.predict(x)
centroids = kmeans.cluster_centers_

x['group'] = labels

df["salary"] = round(df.salary.astype(pd.np.number))
salaries = df.iloc[:,16].values
x = df[["name", "guard", "forward", "center"]]
x['salary'] = salaries / 1e6
x["group"] = labels

df_groups = x.groupby('group', as_index=False)['guard', 'forward', 'center'].sum()
df_group_salary = x.groupby('group', as_index=False)['salary'].mean()
df_groups = pd.merge(df_groups, df_group_salary, how='inner')
print(df_groups)