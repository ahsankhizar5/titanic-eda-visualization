# 🚢 Titanic Dataset - EDA & Visualization

A complete **Exploratory Data Analysis (EDA)** on the Titanic dataset using Python. This project cleans the dataset, explores key insights, visualizes patterns, and summarizes findings to understand survival factors.

---

## 📁 Dataset

- Source: [Kaggle - Titanic Dataset](https://www.kaggle.com/c/titanic/data)
- Filename: `TiTanic_Dataset.csv`

---

## 🔍 Objective

Perform EDA and generate visual insights to answer:
- Who were most likely to survive?
- Were there patterns in class, gender, age, or fare?
- What variables are correlated?

---

## 📌 Features Explored

- Passenger Class (Pclass)
- Sex
- Age
- Fare
- Survival
- Siblings/Spouse & Parents/Children (SibSp, Parch)
- Embarked

---

## 📊 Visualizations

Saved in the `Graphs/` folder:
- 📦 Bar charts for categorical data (Sex, Pclass)
- 📈 Histograms for distributions (Age, Fare)
- 🌡️ Correlation Heatmap

---

## 🧹 Cleaning & Processing

- Handled missing values:
  - `Age`: Filled with median
  - `Embarked`: Filled with mode
  - `Cabin`: Dropped (too sparse)
- Removed duplicates
- Detected outliers in `Fare` using IQR

---

## 💡 Key Insights

- Majority of passengers were **male** and in **3rd class**
- **Females had higher survival rates**
- **Younger passengers** were common
- Strong correlation between **SibSp** and **Parch** (family)
- **Fare** had significant outliers

Full findings are documented in [`TiTanic_EDA_Summery.docx`](./TiTanic_EDA_Summery.docx)

---

## ▶️ Run It Yourself

```bash
python eda_titanic.py

---

## ⚙️ Tools Used

- **Python**
- **Pandas**
- **Matplotlib** & **Seaborn**
- **Numpy**

---

## 👨‍💻 Author

**Ahsan Khizar**
[GitHub](https://github.com/ahsankhizar5) — [LinkedIn](https://linkedin.com/in/ahsankhizar5)

---

> 💡 *"Models may predict prices, but code quality predicts trust."* — Ahsan Khizar
