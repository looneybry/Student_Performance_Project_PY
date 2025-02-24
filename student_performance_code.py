"""
Student Performance Analysis Script

This script analyzes a dataset of student performance to understand the relationships between
study habits, attendance, sleep, and exam scores.
"""

import pandas as pd

# Load the dataset
FILE_PATH = (
    r"C:\Users\Loone\OneDrive\Desktop\Student_Performance_Project"
    r"\student_performance_large_dataset.csv"
)
df = pd.read_csv(FILE_PATH)

# Display basic information
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Data Cleaning
# Handling missing values
df.dropna(inplace=True)

# Convert percentage columns to numeric (if they are not already)
if df['Assignment_Completion_Rate (%)'].dtype == object:  # Check if the column is a string
    df['Assignment_Completion_Rate (%)'] = (
        df['Assignment_Completion_Rate (%)'].str.replace('%', '').astype(float)
else:
    df['Assignment_Completion_Rate (%)'] = df['Assignment_Completion_Rate (%)'].astype(float)

if df['Exam_Score (%)'].dtype == object:  # Check if the column is a string
    df['Exam_Score (%)'] = df['Exam_Score (%)'].str.replace('%', '').astype(float)
else:
    df['Exam_Score (%)'] = df['Exam_Score (%)'].astype(float)

if df['Attendance_Rate (%)'].dtype == object:  # Check if the column is a string
    df['Attendance_Rate (%)'] = df['Attendance_Rate (%)'].str.replace('%', '').astype(float)
else:
    df['Attendance_Rate (%)'] = df['Attendance_Rate (%)'].astype(float)

# Convert categorical values to lowercase for consistency
df['Gender'] = df['Gender'].str.lower()
df['Preferred_Learning_Style'] = df['Preferred_Learning_Style'].str.lower()
df['Self_Reported_Stress_Level'] = df['Self_Reported_Stress_Level'].str.lower()
df['Use_of_Educational_Tech'] = df['Use_of_Educational_Tech'].str.lower()
df['Participation_in_Discussions'] = df['Participation_in_Discussions'].str.lower()

# Analyze Relationships Between Attributes
# 1. Study Hours vs. Social Media Usage
study_vs_social_media = df[['Study_Hours_per_Week', 'Time_Spent_on_Social_Media (hours/week)']].corr()
print("\nCorrelation between Study Hours and Social Media Usage:")
print(study_vs_social_media)

# 2. Sleep Hours vs. Exam Score
sleep_vs_exam_score = df[['Sleep_Hours_per_Night', 'Exam_Score (%)']].corr()
print("\nCorrelation between Sleep Hours and Exam Score:")
print(sleep_vs_exam_score)

# 3. Attendance vs. Exam Score
attendance_vs_exam_score = df[['Attendance_Rate (%)', 'Exam_Score (%)']].corr()
print("\nCorrelation between Attendance Rate and Exam Score:")
print(attendance_vs_exam_score)

# 4. Learning Style vs. Exam Score (Grouped Analysis)
learning_style_vs_exam_score = df.groupby('Preferred_Learning_Style')['Exam_Score (%)'].mean()
print("\nAverage Exam Score by Learning Style:")
print(learning_style_vs_exam_score)

# 5. Study Hours vs. Exam Score
study_vs_exam_score = df[['Study_Hours_per_Week', 'Exam_Score (%)']].corr()
print("\nCorrelation between Study Hours and Exam Score:")
print(study_vs_exam_score)

# Export Cleaned Data for Tableau
CLEANED_FILE_PATH = (
    r"C:\Users\Loone\OneDrive\Desktop\Student_Performance_Project"
    r"\cleaned_student_performance.csv"
)
print(f"\nAttempting to save cleaned data to: {CLEANED_FILE_PATH}")
df.to_csv(CLEANED_FILE_PATH, index=False)
print("Data saved successfully!")