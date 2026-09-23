# ============================================================
# Healthcare Analytics for Doctor Visits Using Python
# ============================================================
# Dataset: Healthcare Analytics for Doctor Visits
# Tools: Python, Pandas, NumPy, Matplotlib, Seaborn
#
# Project sections:
# 1. Import Libraries & Load Data
# 2. Data Understanding
# 3. Data Cleaning
# 4. Feature Engineering
# 5. Descriptive Statistics
# 6. Doctor Visit Analysis
# 7. Gender Analysis
# 8. Age Analysis
# 9. Illness & Health Analysis
# 10. Chronic Condition Analysis
# 11. Insurance Analysis
# 12. Income & Healthcare Utilization
# 13. Correlation Analysis
# 14. Key Insights
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. LOAD DATA
# -----------------------------

# Change this path if your CSV is stored somewhere else.
FILE_PATH = "Healthcare Analytics for Doctor Visits.csv"

df = pd.read_csv(FILE_PATH)

print("=" * 70)
print("HEALTHCARE ANALYTICS FOR DOCTOR VISITS")
print("=" * 70)

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 2. DATA UNDERSTANDING
# -----------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumerical Summary:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include="object"))

# Unique values for every column
print("\nUnique Values:")
for column in df.columns:
    print(f"\n{column}:")
    print(df[column].unique())

# -----------------------------
# 3. DATA CLEANING
# -----------------------------

# Remove the CSV index column if it exists.
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Standardize text columns.
text_columns = [
    "gender",
    "private",
    "freepoor",
    "freerepat",
    "nchronic",
    "lchronic"
]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].astype(str).str.strip().str.lower()

# Check missing values and duplicates after cleaning.
print("\nAfter Cleaning - Missing Values:")
print(df.isnull().sum())

print("\nAfter Cleaning - Duplicate Rows:")
print(df.duplicated().sum())

# -----------------------------
# 4. FEATURE ENGINEERING
# -----------------------------

# The dataset stores age in an encoded form such as 0.19, 0.22, etc.
# Convert it to an approximate age in years for easier interpretation.
df["Age_Years"] = (df["age"] * 100).round().astype(int)

# Create useful age groups.
bins = [0, 18, 30, 45, 60, 100]
labels = ["0-18", "19-30", "31-45", "46-60", "61+"]

df["Age_Group"] = pd.cut(
    df["Age_Years"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Binary chronic-condition flag.
df["Any_Chronic_Condition"] = np.where(
    (df["nchronic"] == "yes") | (df["lchronic"] == "yes"),
    "yes",
    "no"
)

# Binary insurance/access flag.
df["Any_Healthcare_Coverage"] = np.where(
    (df["private"] == "yes") |
    (df["freepoor"] == "yes") |
    (df["freerepat"] == "yes"),
    "yes",
    "no"
)

print("\nNew Columns:")
print(df[[
    "Age_Years",
    "Age_Group",
    "Any_Chronic_Condition",
    "Any_Healthcare_Coverage"
]].head())

# -----------------------------
# 5. DESCRIPTIVE STATISTICS
# -----------------------------

print("\n" + "=" * 70)
print("KEY KPIs")
print("=" * 70)

total_patients = len(df)
total_visits = df["visits"].sum()
average_visits = df["visits"].mean()
median_visits = df["visits"].median()
maximum_visits = df["visits"].max()
average_illness = df["illness"].mean()
average_reduced_days = df["reduced"].mean()
average_health = df["health"].mean()
average_income = df["income"].mean()

print(f"Total Patients              : {total_patients:,}")
print(f"Total Doctor Visits         : {total_visits:,}")
print(f"Average Doctor Visits       : {average_visits:.2f}")
print(f"Median Doctor Visits        : {median_visits:.2f}")
print(f"Maximum Doctor Visits       : {maximum_visits}")
print(f"Average Illness Level       : {average_illness:.2f}")
print(f"Average Reduced Activity    : {average_reduced_days:.2f}")
print(f"Average Health Score        : {average_health:.2f}")
print(f"Average Income Indicator    : {average_income:.2f}")

# -----------------------------
# 6. DOCTOR VISIT ANALYSIS
# -----------------------------

visit_summary = (
    df.groupby("visits")
      .size()
      .reset_index(name="Patient_Count")
      .sort_values("visits")
)

print("\nDoctor Visit Frequency:")
print(visit_summary)

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="visits")
plt.title("Distribution of Doctor Visits")
plt.xlabel("Number of Doctor Visits")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# -----------------------------
# 7. GENDER ANALYSIS
# -----------------------------

gender_analysis = (
    df.groupby("gender")["visits"]
      .agg(
          Patient_Count="count",
          Total_Visits="sum",
          Average_Visits="mean"
      )
      .reset_index()
)

print("\nGender Analysis:")
print(gender_analysis)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=gender_analysis,
    x="gender",
    y="Average_Visits"
)
plt.title("Average Doctor Visits by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 8. AGE ANALYSIS
# -----------------------------

age_analysis = (
    df.groupby("Age_Group", observed=False)["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean",
          Total_Visits="sum"
      )
      .reset_index()
)

print("\nAge Group Analysis:")
print(age_analysis)

plt.figure(figsize=(9, 5))
sns.barplot(
    data=age_analysis,
    x="Age_Group",
    y="Average_Visits"
)
plt.title("Average Doctor Visits by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# Age vs visits
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Age_Years",
    y="visits",
    alpha=0.5
)
plt.title("Age vs Doctor Visits")
plt.xlabel("Age (Years)")
plt.ylabel("Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 9. ILLNESS & HEALTH ANALYSIS
# -----------------------------

illness_analysis = (
    df.groupby("illness")["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean",
          Total_Visits="sum"
      )
      .reset_index()
)

print("\nIllness Analysis:")
print(illness_analysis)

plt.figure(figsize=(9, 5))
sns.barplot(
    data=illness_analysis,
    x="illness",
    y="Average_Visits"
)
plt.title("Average Doctor Visits by Illness Level")
plt.xlabel("Illness Level")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

health_analysis = (
    df.groupby("health")["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean"
      )
      .reset_index()
)

print("\nHealth Analysis:")
print(health_analysis)

plt.figure(figsize=(9, 5))
sns.barplot(
    data=health_analysis,
    x="health",
    y="Average_Visits"
)
plt.title("Average Doctor Visits by Health Status")
plt.xlabel("Health Status / Score")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# Reduced activity vs visits
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="reduced",
    y="visits",
    alpha=0.5
)
plt.title("Reduced Activity vs Doctor Visits")
plt.xlabel("Reduced Activity")
plt.ylabel("Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 10. CHRONIC CONDITION ANALYSIS
# -----------------------------

chronic_analysis = (
    df.groupby("Any_Chronic_Condition")["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean",
          Total_Visits="sum"
      )
      .reset_index()
)

print("\nAny Chronic Condition Analysis:")
print(chronic_analysis)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=chronic_analysis,
    x="Any_Chronic_Condition",
    y="Average_Visits"
)
plt.title("Average Doctor Visits: Chronic vs Non-Chronic")
plt.xlabel("Any Chronic Condition")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# Separate chronic indicators
for column in ["nchronic", "lchronic"]:
    analysis = (
        df.groupby(column)["visits"]
          .mean()
          .reset_index(name="Average_Visits")
    )

    print(f"\n{column} Analysis:")
    print(analysis)

    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=analysis,
        x=column,
        y="Average_Visits"
    )
    plt.title(f"Average Doctor Visits by {column}")
    plt.xlabel(column)
    plt.ylabel("Average Doctor Visits")
    plt.tight_layout()
    plt.show()

# -----------------------------
# 11. INSURANCE / HEALTHCARE ACCESS
# -----------------------------

coverage_columns = ["private", "freepoor", "freerepat"]

for column in coverage_columns:
    analysis = (
        df.groupby(column)["visits"]
          .agg(
              Patient_Count="count",
              Average_Visits="mean",
              Total_Visits="sum"
          )
          .reset_index()
    )

    print(f"\n{column} Analysis:")
    print(analysis)

    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=analysis,
        x=column,
        y="Average_Visits"
    )
    plt.title(f"Average Doctor Visits by {column}")
    plt.xlabel(column)
    plt.ylabel("Average Doctor Visits")
    plt.tight_layout()
    plt.show()

# Combined healthcare coverage
coverage_analysis = (
    df.groupby("Any_Healthcare_Coverage")["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean",
          Total_Visits="sum"
      )
      .reset_index()
)

print("\nOverall Healthcare Coverage Analysis:")
print(coverage_analysis)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=coverage_analysis,
    x="Any_Healthcare_Coverage",
    y="Average_Visits"
)
plt.title("Average Doctor Visits by Healthcare Coverage")
plt.xlabel("Any Healthcare Coverage")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 12. INCOME ANALYSIS
# -----------------------------

income_summary = (
    df.groupby("income")["visits"]
      .agg(
          Patient_Count="count",
          Average_Visits="mean"
      )
      .reset_index()
)

print("\nIncome Analysis:")
print(income_summary.head(20))

plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df,
    x="income",
    y="visits",
    alpha=0.5
)
plt.title("Income Indicator vs Doctor Visits")
plt.xlabel("Income Indicator")
plt.ylabel("Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 13. CORRELATION ANALYSIS
# -----------------------------

numeric_columns = [
    "visits",
    "age",
    "income",
    "illness",
    "reduced",
    "health"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(9, 7))
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)
plt.title("Correlation Matrix - Healthcare Variables")
plt.tight_layout()
plt.show()

# Correlation specifically with doctor visits
visit_correlation = (
    correlation["visits"]
    .sort_values(ascending=False)
)

print("\nCorrelation with Doctor Visits:")
print(visit_correlation)

# -----------------------------
# 14. CROSS ANALYSIS
# -----------------------------

# Illness and chronic condition
cross_analysis = (
    df.groupby(["illness", "Any_Chronic_Condition"])["visits"]
      .mean()
      .reset_index(name="Average_Visits")
)

print("\nIllness vs Chronic Condition:")
print(cross_analysis)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=cross_analysis,
    x="illness",
    y="Average_Visits",
    hue="Any_Chronic_Condition"
)
plt.title("Doctor Visits by Illness Level and Chronic Condition")
plt.xlabel("Illness Level")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# Age group and chronic condition
age_chronic = (
    df.groupby(["Age_Group", "Any_Chronic_Condition"], observed=False)["visits"]
      .mean()
      .reset_index(name="Average_Visits")
)

print("\nAge Group vs Chronic Condition:")
print(age_chronic)

plt.figure(figsize=(10, 5))
sns.barplot(
    data=age_chronic,
    x="Age_Group",
    y="Average_Visits",
    hue="Any_Chronic_Condition"
)
plt.title("Doctor Visits by Age Group and Chronic Condition")
plt.xlabel("Age Group")
plt.ylabel("Average Doctor Visits")
plt.tight_layout()
plt.show()

# -----------------------------
# 15. TOP PATIENT GROUPS
# -----------------------------

print("\nHighest Visit Records:")
print(
    df.nlargest(10, "visits")[
        [
            "visits",
            "gender",
            "Age_Years",
            "income",
            "illness",
            "reduced",
            "health",
            "private",
            "nchronic",
            "lchronic"
        ]
    ]
)

# -----------------------------
# 16. AUTOMATIC DATA-DRIVEN INSIGHTS
# -----------------------------

print("\n" + "=" * 70)
print("DATA-DRIVEN INSIGHTS")
print("=" * 70)

# Highest average visit gender
gender_top = gender_analysis.loc[
    gender_analysis["Average_Visits"].idxmax()
]

print(
    f"\n1. Gender with higher average visits in this dataset: "
    f"{gender_top['gender']} "
    f"({gender_top['Average_Visits']:.2f} average visits)."
)

# Highest average visit age group
age_top = age_analysis.loc[
    age_analysis["Average_Visits"].idxmax()
]

print(
    f"2. Age group with higher average visits: "
    f"{age_top['Age_Group']} "
    f"({age_top['Average_Visits']:.2f} average visits)."
)

# Highest illness level by average visits
illness_top = illness_analysis.loc[
    illness_analysis["Average_Visits"].idxmax()
]

print(
    f"3. Illness level with higher average visits: "
    f"{illness_top['illness']} "
    f"({illness_top['Average_Visits']:.2f} average visits)."
)

# Chronic comparison
if set(chronic_analysis["Any_Chronic_Condition"]) >= {"yes", "no"}:
    chronic_yes = chronic_analysis.loc[
        chronic_analysis["Any_Chronic_Condition"] == "yes",
        "Average_Visits"
    ].iloc[0]

    chronic_no = chronic_analysis.loc[
        chronic_analysis["Any_Chronic_Condition"] == "no",
        "Average_Visits"
    ].iloc[0]

    print(
        f"4. Average visits - chronic condition: {chronic_yes:.2f}; "
        f"no chronic condition: {chronic_no:.2f}."
    )

# Strongest numeric correlation with visits, excluding visits itself
corr_without_visits = visit_correlation.drop("visits")
strongest_factor = corr_without_visits.abs().idxmax()
strongest_value = corr_without_visits[strongest_factor]

print(
    f"5. Among the selected numeric variables, the strongest "
    f"linear correlation with visits is '{strongest_factor}' "
    f"(correlation = {strongest_value:.2f})."
)

print(
    "\nNote: Correlation shows association, not causation. "
    "The findings should be interpreted as patterns in this dataset."
)

# -----------------------------
# 17. SAVE CLEANED DATA
# -----------------------------

df.to_csv("cleaned_healthcare_doctor_visits.csv", index=False)

print("\nCleaned dataset saved as:")
print("cleaned_healthcare_doctor_visits.csv")

print("\nProject analysis completed successfully!")
