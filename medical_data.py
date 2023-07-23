# -*- coding: utf-8 -*-
"""medical data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15b9Sple0u1XI4kQNO7YS395Hj5_0O2zy
"""

import pandas as pd

medical_df = pd.read_csv('medical.csv')

medical_df

medical_df.info()

medical_df.describe()

!pip install plotly matplotlib seaborn --quiet

# Commented out IPython magic to ensure Python compatibility.
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 10)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

medical_df.age.describe()

medical_df.charges.describe()

fig=px.histogram(medical_df,x="age",marginal="box",nbins=47,title="Distribution of age")
fig.update_layout(bargap=0.5)
fig.show()

fig=px.histogram(medical_df,x="bmi",marginal="box",nbins=47,title="Distribution of age")
fig.update_layout(bargap=0.5)
fig.show()

fig = px.histogram(medical_df,
                   x='charges',
                   marginal='box',
                   color='smoker',
                   color_discrete_sequence=['green', 'black'],
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.histogram(medical_df,
                   x='charges',
                   marginal='box',
                   color='sex',
                   color_discrete_sequence=['green', 'black'],
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.histogram(medical_df,
                   x='charges',
                   marginal='box',
                   color='region',
                   color_discrete_sequence=['green', 'black'],
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()

medical_df.smoker.value_counts()

px.histogram(medical_df,x="smoker",color="sex",title="smoker")

px.histogram(medical_df,x="region",color="sex",title="region")

px.histogram(medical_df,x="children",color="sex",title="children")

px.histogram(medical_df,x="sex",color="smoker",title="sex")

"""# Age and charges"""

fig=px.scatter(medical_df,x="age",y="charges",color="smoker",opacity=0.8,hover_data=["sex"],title="Age vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=px.scatter(medical_df,x="bmi",y="charges",color="smoker",opacity=0.8,hover_data=["sex"],title="bmi vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=px.scatter(medical_df,x="smoker",y="charges",color="smoker",opacity=0.8,hover_data=["sex"],title="region vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=sns.barplot(data=medical_df,x="smoker",y="charges")

fig=px.violin(medical_df,x="smoker",y="charges",color="smoker",hover_data=["sex"],title="region vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=px.scatter(medical_df,x="region",y="charges",color="smoker",opacity=0.8,hover_data=["sex"],title="region vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=px.violin(medical_df,x="region",y="charges",color="smoker",hover_data=["sex"],title="region vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=sns.barplot(data=medical_df,x="region",y="charges",hue="sex")
#fig.update_traces(marker_size=5)
#fig.show()

fig=px.violin(medical_df,x="children",y="charges")
fig.update_traces(marker_size=5)
fig.show()

fig=px.scatter(medical_df,x="children",y="charges",color="smoker",hover_data=["sex"],title="region vs Charges")
fig.update_traces(marker_size=5)
fig.show()

fig=sns.barplot(data=medical_df,x="children",y="charges")

"""# correlation"""

medical_df.charges.corr(medical_df.age)

medical_df.charges.corr(medical_df.bmi)

medical_df.charges.corr(medical_df.children)

smoker_values={"no":0,"yes":1}
smoker_numeric=medical_df.smoker.map(smoker_values)
medical_df.charges.corr(smoker_numeric)

"""# linear regression using single feature"""

non_smoker_df=medical_df[medical_df.smoker=="no"]

plt.title("Age vs. charges")
sns.scatterplot(data=non_smoker_df, x='age', y='charges', alpha=0.7, s=15);

smoker_df=medical_df[medical_df.smoker=="yes"]

plt.title("Age vs. charges")
sns.scatterplot(data=smoker_df, x='age', y='charges', alpha=0.7, s=15);

def estimate_charges(age,w,b):
    return w*age+b

w=50
b=100

estimate_charges(30,w,b)

ages=non_smoker_df.age
ages

estimated_charges=estimate_charges(ages,w,b)
estimated_charges

non_smoker_df.charges

ages = non_smoker_df.age
estimated_charges = estimate_charges(ages, w, b)

plt.plot(ages, estimated_charges, 'r-o');
plt.xlabel('Age');
plt.ylabel('Estimated Charges');

target = non_smoker_df.charges

plt.plot(ages, estimated_charges, 'r', alpha=0.9);
plt.scatter(ages, target, s=8,alpha=0.8);
plt.xlabel('Age');
plt.ylabel('Charges')
plt.legend(['Estimate', 'Actual']);

def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges

    estimated_charges = estimate_charges(ages, w, b)

    plt.plot(ages, estimated_charges, 'r', alpha=0.9);
    plt.scatter(ages, target, s=8,alpha=0.8);
    plt.xlabel('Age');
    plt.ylabel('Charges')
    plt.legend(['Estimate', 'Actual']);
#w=int(input("enter w: "))
#b=int(input("enter b: "))
try_parameters(w, b)

targets=non_smoker_df.charges
targets

predictions=estimated_charges
predictions

!pip install numpy --quiet

import numpy as np

def rmse(targets, predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))

w = 50
b = 100

try_parameters(w,b)

targets = non_smoker_df['charges']
predicted = estimate_charges(non_smoker_df.age, w, b)

rmse(targets, predicted)

def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    predictions = estimate_charges(ages, w, b)

    plt.plot(ages, predictions, 'r', alpha=0.9);
    plt.scatter(ages, target, s=8,alpha=0.8);
    plt.xlabel('Age');
    plt.ylabel('Charges')
    plt.legend(['Prediction', 'Actual']);

    loss = rmse(target, predictions)
    print("RMSE Loss: ", loss)

try_parameters(50, 100)

try_parameters(200, 200)

"""# linear regression with scikit-learn"""

!pip install scikit-learn --quiet

from sklearn.linear_model import LinearRegression

model = LinearRegression()

help(model.fit)

inputs = non_smoker_df[['age']]
targets = non_smoker_df.charges
print('inputs.shape :', inputs.shape)
print('targes.shape :', targets.shape)

model.fit(inputs, targets)

model.predict(np.array([[23],
                        [37],
                        [61]]))

predictions = model.predict(inputs)

predictions

inputs

targets

rmse(targets, predictions)

# w
model.coef_

# b
model.intercept_

try_parameters(model.coef_, model.intercept_)

"""# linear regression with multiple features"""

inputs,targets=non_smoker_df[["age","bmi"]],non_smoker_df["charges"]
model=LinearRegression().fit(inputs,targets)
predictions=model.predict(inputs)
loss=rmse(targets,predictions)
print("Loss:",loss)

non_smoker_df.charges.corr(non_smoker_df.bmi)

fig = px.scatter(non_smoker_df, x='bmi', y='charges', title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show()

fig = px.scatter_3d(non_smoker_df, x='age', y='bmi', z='charges')
fig.update_traces(marker_size=3, marker_opacity=0.5)
fig.show()

model.coef_, model.intercept_

non_smoker_df.charges.corr(non_smoker_df.children)

fig = px.strip(non_smoker_df, x='children', y='charges', title= "Children vs. Charges")
fig.update_traces(marker_size=4, marker_opacity=0.7)
fig.show()

inputs,targets=non_smoker_df[["age","bmi","children"]],non_smoker_df["charges"]
model=LinearRegression().fit(inputs,targets)
predictions=model.predict(inputs)
loss=rmse(targets,predictions)
print("Loss:",loss)

inputs,targets=medical_df[["age","bmi","children",]],medical_df["charges"]
model=LinearRegression().fit(inputs,targets)
predictions=model.predict(inputs)
loss=rmse(targets,predictions)
print("Loss:",loss)

sns.barplot(data=medical_df, x='smoker', y='charges');

smoker_codes = {'no': 0, 'yes': 1}
medical_df['smoker_code'] = medical_df.smoker.map(smoker_codes)

medical_df.charges.corr(medical_df.smoker_code)

medical_df

inputs,targets=medical_df[["age","bmi","children","smoker_code"]],medical_df["charges"]
model=LinearRegression().fit(inputs,targets)
predictions=model.predict(inputs)
loss=rmse(targets,predictions)
print("Loss:",loss)

sns.barplot(data=medical_df, x='sex', y='charges')

sex_codes = {'female': 0, 'male': 1}

medical_df['sex_code'] = medical_df.sex.map(sex_codes)

medical_df.charges.corr(medical_df.sex_code)

inputs,targets=medical_df[["age","bmi","children","smoker_code",]],medical_df["charges"]
model=LinearRegression().fit(inputs,targets)
predictions=model.predict(inputs)
loss=rmse(targets,predictions)
print("Loss:",loss)

sns.barplot(data=medical_df, x='region', y='charges');

from sklearn import preprocessing
enc = preprocessing.OneHotEncoder()
enc.fit(medical_df[['region']])
enc.categories_

one_hot = enc.transform(medical_df[['region']]).toarray()
one_hot

medical_df[['northeast', 'northwest', 'southeast', 'southwest']] = one_hot

medical_df

input_cols = ['age', 'bmi', 'children', 'smoker_code', 'sex_code', 'northeast', 'northwest', 'southeast', 'southwest']
inputs, targets = medical_df[input_cols], medical_df['charges']
model = LinearRegression().fit(inputs, targets)
predictions = model.predict(inputs)
loss = rmse(targets, predictions)
print('Loss:', loss)

model.coef_

model.intercept_

weights_df = pd.DataFrame({
    'feature': np.append(input_cols, 1),
    'weight': np.append(model.coef_, model.intercept_)
})
weights_df

from sklearn.preprocessing import StandardScaler

numeric_cols = ['age', 'bmi', 'children']
scaler = StandardScaler()
scaler.fit(medical_df[numeric_cols])

scaler.mean_

scaler.var_

scaled_inputs = scaler.transform(medical_df[numeric_cols])
scaled_inputs

cat_cols = ['smoker_code', 'sex_code', 'northeast', 'northwest', 'southeast', 'southwest']
categorical_data = medical_df[cat_cols].values
model = LinearRegression().fit(inputs, targets)
predictions = model.predict(inputs)
loss = rmse(targets, predictions)
print('Loss:', loss)

weights_df = pd.DataFrame({
    'feature': np.append(numeric_cols + cat_cols, 1),
    'weight': np.append(model.coef_, model.intercept_)
})
weights_df.sort_values('weight', ascending=False)

medical_df

from sklearn.preprocessing import StandardScaler

numeric_cols = ['age', 'bmi', 'children']
scaler = StandardScaler()
scaler.fit(medical_df[numeric_cols])

scaler.mean_

scaler.var_

scaled_inputs = scaler.transform(medical_df[numeric_cols])
scaled_inputs

cat_cols = ['smoker_code', 'sex_code', 'northeast', 'northwest', 'southeast', 'southwest']
categorical_data = medical_df[cat_cols].values

inputs = np.concatenate((scaled_inputs, categorical_data), axis=1)
targets = medical_df.charges
model = LinearRegression().fit(inputs, targets)
predictions = model.predict(inputs)
loss = rmse(targets, predictions)
print('Loss:', loss)

weights_df = pd.DataFrame({
    'feature': np.append(numeric_cols + cat_cols, 1),
    'weight': np.append(model.coef_, model.intercept_)
})
weights_df.sort_values('weight', ascending=False)

from sklearn.model_selection import train_test_split

inputs_train, inputs_test, targets_train, targets_test = train_test_split(inputs, targets, test_size=0.1)

model = LinearRegression().fit(inputs_train, targets_train)
predictions_test = model.predict(inputs_test)
loss = rmse(targets_test, predictions_test)
print('Test Loss:', loss)

predictions_train = model.predict(inputs_train)
loss = rmse(targets_train, predictions_train)
print('Training Loss:', loss)




