# 🏥 Healthcare Analytics for Doctor Visits Using Python

An exploratory data analytics project focused on understanding **doctor visits, patient health, illness, chronic conditions, healthcare coverage, and healthcare utilization patterns** using Python.

## 📌 Project Overview

Healthcare data can provide valuable insights into patient behavior and healthcare utilization. This project analyzes a healthcare dataset to explore patterns in doctor visits and their relationship with factors such as:

* Gender
* Age
* Illness
* Health status
* Reduced activity
* Chronic conditions
* Healthcare coverage
* Income

The project follows a complete analytics workflow from **data loading and cleaning to feature engineering, exploratory analysis, correlation analysis, and data-driven insights**.

---

## 🎯 Objectives

The main objectives of this project are to:

* Analyze doctor visit patterns.
* Understand patient demographics and health characteristics.
* Compare healthcare utilization across gender and age groups.
* Examine the relationship between illness and doctor visits.
* Analyze chronic conditions and healthcare coverage.
* Explore income and healthcare utilization.
* Identify relationships between important numerical variables.
* Generate data-driven insights from the healthcare dataset.

---

## 🗂️ Dataset

**Dataset:** Healthcare Analytics for Doctor Visits

The dataset contains healthcare-related variables used to analyze patient characteristics and doctor visit behavior.

Important variables include:

| Category            | Variables                          |
| ------------------- | ---------------------------------- |
| Patient Information | `gender`, `age`, `income`          |
| Doctor Visits       | `visits`                           |
| Health Indicators   | `illness`, `health`, `reduced`     |
| Chronic Conditions  | `nchronic`, `lchronic`             |
| Healthcare Coverage | `private`, `freepoor`, `freerepat` |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook / Python Environment**

These tools are used for data loading, cleaning, transformation, statistical analysis, visualization, and exploratory data analysis.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Healthcare Utilization Analysis
   ↓
Correlation Analysis
   ↓
Cross Analysis
   ↓
Data-Driven Insights
```

---

## 🧹 Data Cleaning

The project performs several data-cleaning operations, including:

* Removing unnecessary columns when present.
* Standardizing text/categorical values.
* Checking missing values.
* Checking duplicate records.
* Reviewing data types and dataset structure.

The cleaning process is implemented directly in Python using Pandas.

---

## ⚙️ Feature Engineering

New analytical features are created to support deeper analysis.

### Age in Years

The original age representation is transformed into an integer-based age field:

```text
Age_Years
```

### Age Groups

Patients are grouped into:

```text
0-18
19-30
31-45
46-60
61+
```

### Any Chronic Condition

A combined indicator is created using:

* `nchronic`
* `lchronic`

Resulting feature:

```text
Any_Chronic_Condition
```

### Any Healthcare Coverage

Coverage is combined from:

* `private`
* `freepoor`
* `freerepat`

Resulting feature:

```text
Any_Healthcare_Coverage
```

These engineered fields are used for further healthcare utilization analysis.

---

## 📊 Key Analysis Areas

### 1. Doctor Visit Analysis

The project analyzes:

* Total doctor visits
* Average visits
* Median visits
* Maximum visits
* Visit frequency patterns

### 2. Gender Analysis

Patient and visit patterns are compared across gender using:

* Patient count
* Total visits
* Average visits

### 3. Age Analysis

The analysis examines:

* Patient distribution by age group
* Average visits by age group
* Relationship between age and visits

### 4. Illness & Health Analysis

The project studies:

* Illness levels
* Health status
* Reduced activity
* Relationship between reduced activity and doctor visits

### 5. Chronic Condition Analysis

The project analyzes:

* Chronic condition indicators
* Combined chronic condition status
* Doctor visits among patients with and without chronic conditions

### 6. Healthcare Coverage Analysis

Healthcare access is examined using:

* Private coverage
* Free/poor coverage
* Free/repatriate coverage
* Combined healthcare coverage

### 7. Income & Healthcare Utilization

The project investigates:

* Income distribution
* Income-related patterns
* Relationship between income and doctor visits

### 8. Correlation Analysis

A correlation matrix is used to examine relationships among selected numerical variables, including:

```text
visits
age
income
illness
reduced
health
```

The analysis also identifies variables with stronger absolute linear associations with doctor visits.

> **Note:** Correlation indicates association and does not establish causation.

### 9. Cross Analysis

The project performs additional comparisons such as:

* Illness × Chronic Condition
* Age Group × Chronic Condition

---

## 📈 Visualizations

The project uses Python visualization libraries to create analytical charts, including:

* Count plots
* Bar charts
* Scatter plots
* Correlation heatmaps
* Comparative analytical visualizations

These visualizations help identify patterns and relationships within the healthcare data.

---

## 💡 Data-Driven Insights

The project automatically evaluates several analytical dimensions, including:

* Gender with the highest average visit level
* Age group with the highest average visit level
* Illness level associated with higher average visits
* Difference between chronic and non-chronic patient visit levels
* Strongest absolute linear association with doctor visits among selected numerical variables

The insight-generation logic is based on the analyzed dataset rather than manually entered conclusions.

---

## 👥 End Users

This project can be useful for:

* **Doctors & Healthcare Professionals**
* **Hospital & Clinic Managers**
* **Healthcare Analysts**
* **Healthcare Planning Teams**
* **Researchers & Students**

The analysis can support understanding of patient visit patterns and healthcare utilization.

---

## 📁 Project Structure

```text
HEALTHCARE-ANALYTICS-FOR-DOCTOR-VISITS/
│
├── Healthcare Analytics for Doctor Visits.csv
├── Python analysis script
├── cleaned_healthcare_doctor_visits.csv
└── README.md
```

The Python workflow also saves the cleaned dataset as:

```text
cleaned_healthcare_doctor_visits.csv
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/harshadamali14-rgb/HEALTHCARE-ANALYTICS-FOR-DOCTOR-VISITS.git
```

### 2. Open the project folder

```bash
cd HEALTHCARE-ANALYTICS-FOR-DOCTOR-VISITS
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the Python analysis

Open the Python project file in:

* Jupyter Notebook
* VS Code
* Google Colab
* Any Python-compatible IDE

Make sure the dataset file is available in the expected project location before running the analysis. The script loads the healthcare CSV using Pandas.

---

## 📌 Project Outcome

This project demonstrates a complete **Python-based exploratory data analytics workflow** for healthcare data:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Statistical & Correlation Analysis
      ↓
Visualization
      ↓
Insights
```

It demonstrates practical skills in:

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Data Visualization
* Statistical Analysis
* Feature Engineering
* Correlation Analysis
* Healthcare Data Analytics

---

## 🚀 Future Improvements

Possible future extensions include:

* Interactive healthcare dashboards
* Predictive analysis of doctor visits
* Machine learning models
* Automated reporting
* Interactive web-based analytics
* Deployment as a healthcare analytics application

---

## 👩‍💻 Author

**Harshada Mali**

Integrated MCA Student
Aspiring Data Analyst / BI Analyst

### Skills Demonstrated

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Data Cleaning` · `EDA` · `Data Visualization` · `Statistical Analysis`

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/harshadamali14-rgb/HEALTHCARE-ANALYTICS-FOR-DOCTOR-VISITS
