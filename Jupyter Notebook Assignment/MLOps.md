# Bank Marketing Dataset – Exploratory Data Analysis (EDA)

This notebook contains a simple exploratory data analysis of the **Bank Marketing dataset** from the UCI Machine Learning Repository. The goal here is to understand the structure of the data, look at basic statistics, and visualize a few important patterns before doing anything more advanced.

I’ve kept the analysis straightforward and practical, focusing on what each step tells us about the dataset.

---

## Importing Required Libraries

First, we import the libraries needed for data analysis and visualization. Pandas is used for handling the dataset, while Matplotlib and Seaborn are used for plotting graphs.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
```
---

## Loading the Dataset

The dataset is loaded using `pandas.read_csv`. This file uses a semicolon (`;`) as the separator, which is why it is explicitly specified. Once loaded, the data is stored in a DataFrame for further analysis.

```python
df = pd.read_csv("bank.csv", sep=";")
```
---

## Previewing the Data

To get a quick idea of what the dataset looks like, we display the first five rows. This helps in understanding the columns, data types, and general structure of the data.

```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>balance</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
      <th>month</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>poutcome</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>30</td>
      <td>unemployed</td>
      <td>married</td>
      <td>primary</td>
      <td>no</td>
      <td>1787</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>19</td>
      <td>oct</td>
      <td>79</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33</td>
      <td>services</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>4789</td>
      <td>yes</td>
      <td>yes</td>
      <td>cellular</td>
      <td>11</td>
      <td>may</td>
      <td>220</td>
      <td>1</td>
      <td>339</td>
      <td>4</td>
      <td>failure</td>
      <td>no</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35</td>
      <td>management</td>
      <td>single</td>
      <td>tertiary</td>
      <td>no</td>
      <td>1350</td>
      <td>yes</td>
      <td>no</td>
      <td>cellular</td>
      <td>16</td>
      <td>apr</td>
      <td>185</td>
      <td>1</td>
      <td>330</td>
      <td>1</td>
      <td>failure</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>management</td>
      <td>married</td>
      <td>tertiary</td>
      <td>no</td>
      <td>1476</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>3</td>
      <td>jun</td>
      <td>199</td>
      <td>4</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>59</td>
      <td>blue-collar</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>0</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>226</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>


---

## Dataset Structure and Data Types

The `.info()` method is used to understand the structure of the dataset. It shows the total number of rows and columns, the data type of each column, and whether there are any missing values.

```python
df.info()
```

    <class 'pandas.DataFrame'>
    RangeIndex: 4521 entries, 0 to 4520
    Data columns (total 17 columns):
     #   Column     Non-Null Count  Dtype
    ---  ------     --------------  -----
     0   age        4521 non-null   int64
     1   job        4521 non-null   str  
     2   marital    4521 non-null   str  
     3   education  4521 non-null   str  
     4   default    4521 non-null   str  
     5   balance    4521 non-null   int64
     6   housing    4521 non-null   str  
     7   loan       4521 non-null   str  
     8   contact    4521 non-null   str  
     9   day        4521 non-null   int64
     10  month      4521 non-null   str  
     11  duration   4521 non-null   int64
     12  campaign   4521 non-null   int64
     13  pdays      4521 non-null   int64
     14  previous   4521 non-null   int64
     15  poutcome   4521 non-null   str  
     16  y          4521 non-null   str  
    dtypes: int64(7), str(10)
    memory usage: 600.6 KB

---

## Descriptive Statistics (Numerical Columns)

Using `.describe()` gives summary statistics for numerical columns such as mean, standard deviation, minimum, and maximum values. This helps in understanding the distribution and spread of numerical features like age, balance, and duration.

```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>balance</th>
      <th>day</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4521.000000</td>
      <td>4521.000000</td>
      <td>4521.000000</td>
      <td>4521.000000</td>
      <td>4521.000000</td>
      <td>4521.000000</td>
      <td>4521.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>41.170095</td>
      <td>1422.657819</td>
      <td>15.915284</td>
      <td>263.961292</td>
      <td>2.793630</td>
      <td>39.766645</td>
      <td>0.542579</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.576211</td>
      <td>3009.638142</td>
      <td>8.247667</td>
      <td>259.856633</td>
      <td>3.109807</td>
      <td>100.121124</td>
      <td>1.693562</td>
    </tr>
    <tr>
      <th>min</th>
      <td>19.000000</td>
      <td>-3313.000000</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>33.000000</td>
      <td>69.000000</td>
      <td>9.000000</td>
      <td>104.000000</td>
      <td>1.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>39.000000</td>
      <td>444.000000</td>
      <td>16.000000</td>
      <td>185.000000</td>
      <td>2.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>49.000000</td>
      <td>1480.000000</td>
      <td>21.000000</td>
      <td>329.000000</td>
      <td>3.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>87.000000</td>
      <td>71188.000000</td>
      <td>31.000000</td>
      <td>3025.000000</td>
      <td>50.000000</td>
      <td>871.000000</td>
      <td>25.000000</td>
    </tr>
  </tbody>
</table>
</div>


---

## Descriptive Statistics (Categorical Columns)

For categorical columns, `.describe(include="object")` is used. This shows information such as the number of unique values, the most frequent category, and its frequency.

```python
df.describe(include="object")
```

    /tmp/ipykernel_25190/702825166.py:1: Pandas4Warning: For backward compatibility, 'str' dtypes are included by select_dtypes when 'object' dtype is specified. This behavior is deprecated and will be removed in a future version. Explicitly pass 'str' to `include` to select them, or to `exclude` to remove them and silence this warning.
    See https://pandas.pydata.org/docs/user_guide/migration-3-strings.html#string-migration-select-dtypes for details on how to write code that works with pandas 2 and 3.
      df.describe(include="object")





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>month</th>
      <th>poutcome</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
      <td>4521</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>12</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>12</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>management</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>cellular</td>
      <td>may</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>969</td>
      <td>2797</td>
      <td>2306</td>
      <td>4445</td>
      <td>2559</td>
      <td>3830</td>
      <td>2896</td>
      <td>1398</td>
      <td>3705</td>
      <td>4000</td>
    </tr>
  </tbody>
</table>
</div>


---

## Distribution of Target Variable (`y`)

The target variable `y` indicates whether a client subscribed to a term deposit. A bar chart is used to visualize how many clients said “yes” versus “no”. This also helps identify class imbalance in the dataset.

```python
df["y"].value_counts().plot.bar()
plt.title("Distribution of Yes/No")
plt.xlabel("y")
plt.ylabel("Count")
plt.show()
```


    
![png](output_6_0.png)
    

---

## Age Distribution

This histogram shows how client ages are distributed across the dataset. Most clients fall into the middle-age range, with fewer very young or very old clients.

```python
plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
```


    
![png](output_7_0.png)
    

---

## Correlation Heatmap (Numerical Features)

Correlation analysis is performed only on numerical columns, since correlation is not defined for categorical data. The heatmap helps visualize relationships between numerical variables such as age, balance, duration, and campaign.

```python
numeric_df = df.select_dtypes(include=["int64", "float64"])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numerical Features)")
plt.show()
```


    
![png](output_8_0.png)
    
---

## Conclusion

In this analysis, the Bank Marketing dataset was explored using basic EDA techniques. The dataset contains both numerical and categorical features with no missing values. The target variable is imbalanced, with more clients not subscribing to the term deposit. Visualizations and summary statistics provide useful insights into customer characteristics and their potential influence on subscription behavior. This analysis can be used as a foundation for further modeling or prediction tasks.
