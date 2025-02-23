# Student Performance Analysis

## Overview
This project analyzes a dataset of student performance to understand the relationships between various factors (e.g., study hours, sleep hours, attendance, learning style) and exam scores. The goal is to identify which attributes may contribute to better academic performance.

**GitHub Username**: [looneybry](https://github.com/looneybry)

**Repository**: [Student_Performance_Project_PY](https://github.com/looneybry/Student_Performance_Project_PY)

## Tools Used
- **Python**: For data cleaning and analysis.
- **Pandas**: For data manipulation.

## Data Source
The dataset used in this project is available on Kaggle:
- [Student Performance and Learning Style Dataset](https://www.kaggle.com/datasets/adilshamim8/student-performance-and-learning-style)

## Dataset
The dataset contains **10,000 rows** and **15 columns**, including:
- **Student_ID**: Unique identifier for each student.
- **Study_Hours_per_Week**: Number of hours spent studying per week.
- **Sleep_Hours_per_Night**: Average hours of sleep per night.
- **Attendance_Rate (%)**: Percentage of classes attended.
- **Exam_Score (%)**: Student's exam score.
- **Preferred_Learning_Style**: Learning style (e.g., visual, auditory, kinesthetic).
- **Time_Spent_on_Social_Media (hours/week)**: Hours spent on social media per week.
- And more...

## Analysis
### Key Steps:
1. **Data Cleaning**:
   - Handled missing values.
   - Converted percentage columns to numeric.
   - Standardized categorical values (e.g., lowercase for consistency).

2. **Exploratory Data Analysis (EDA)**:
   - Calculated correlations between:
     - Study Hours vs. Social Media Usage.
     - Sleep Hours vs. Exam Score.
     - Attendance Rate vs. Exam Score.
     - Study Hours vs. Exam Score.
   - Grouped analysis:
     - Average exam score by learning style.

### Key Findings:
- **Weak Correlations**: Most factors (e.g., study hours, sleep hours, attendance) showed very weak correlations with exam scores.
- **Learning Style Impact**: Learning style had a minimal impact on exam scores, with auditory learners scoring slightly higher on average.

### Interpreting Correlation Values
- **0.7 to 1.0 (-0.7 to -1.0)**: Strong correlation.
- **0.3 to 0.7 (-0.3 to -0.7)**: Moderate correlation.
- **0.0 to 0.3 (-0.0 to -0.3)**: Weak or no correlation.

## Script Output
### Dataset Info
![Dataset Info](Screenshots/dataset_info.png)

### First 5 Rows
![First 5 Rows](Screenshots/first_5_rows.png)

### Correlation Analysis
#### Study Hours vs. Social Media Usage
![Study Hours vs. Social Media Usage](Screenshots/study_vs_social_media.png)

#### Sleep Hours vs. Exam Score
![Sleep Hours vs. Exam Score](Screenshots/sleep_vs_exam_score.png)

#### Attendance Rate vs. Exam Score
![Attendance Rate vs. Exam Score](Screenshots/attendance_vs_exam_score.png)

#### Study Hours vs. Exam Score
![Study Hours vs. Exam Score](Screenshots/study_vs_exam_score.png)

### Average Exam Score by Learning Style
![Average Exam Score by Learning Style](Screenshots/learning_style_vs_exam_score.png)

### Data Saved Successfully
![Data Saved Successfully](Screenshots/data_saved_successfully.png)

## Correlation Analysis
#### Study Hours vs. Social Media Usage
- **Correlation**: 0.01038
- **Interpretation**: Very weak positive correlation. Study hours and social media usage are almost unrelated.

#### Sleep Hours vs. Exam Score
- **Correlation**: -0.016284
- **Interpretation**: Very weak negative correlation. Sleep hours and exam scores are almost unrelated.

#### Attendance Rate vs. Exam Score
- **Correlation**: 0.003717
- **Interpretation**: Very weak positive correlation. Attendance rate and exam scores are almost unrelated.

#### Study Hours vs. Exam Score
- **Correlation**: 0.004084
- **Interpretation**: Very weak positive correlation. Study hours and exam scores are almost unrelated.

#### Exam Score by Learning Style
- **Auditory**: 70.49
- **Kinesthetic**: 70.35
- **Reading/Writing**: 69.81
- **Visual**: 70.11
- **Interpretation**: The average exam scores for different learning styles are **basically the same**, indicating that learning style has **minimal impact** on exam performance.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/looneybry/Student_Performance_Project_PY.git