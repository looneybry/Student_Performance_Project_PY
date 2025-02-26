import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# File paths
DATA_FILE_PATH = r"C:\Users\Loone\OneDrive\Desktop\Student_Performance_Project\data\cleaned_student_performance.csv"
VISUALS_FOLDER = r"C:\Users\Loone\OneDrive\Desktop\Student_Performance_Project\visualizations"

# Ensure the visualizations folder exists
os.makedirs(VISUALS_FOLDER, exist_ok=True)

# Load the dataset
df = pd.read_csv(DATA_FILE_PATH)

### ATTENDANCE RATE VS. EXAM SCORE (Darker Blue Bar Chart)
df['Attendance_Category'] = pd.cut(df['Attendance_Rate (%)'], bins=[50, 60, 70, 80, 90, 100], labels=['50+%', '60+%', '70+%', '80+%', '90+%'])
attendance_avg = df.groupby('Attendance_Category')['Exam_Score (%)'].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=attendance_avg.index, y=attendance_avg.values, palette='Blues_d')
plt.title('Average Exam Score by Attendance Rate')
plt.xlabel('Attendance Rate')
plt.ylabel('Average Exam Score (%)')
plt.grid(True)
plt.savefig(os.path.join(VISUALS_FOLDER, "attendance_vs_exam_score.png"))
plt.close()

### STUDY HOURS VS. EXAM SCORE (Darker Green Bar Chart)
df['Study_Hours_Category'] = pd.cut(df['Study_Hours_per_Week'], bins=[0, 10, 20, 30, 40, 50], labels=['0-10', '11-20', '21-30', '31-40', '41-50'])
study_avg = df.groupby('Study_Hours_Category')['Exam_Score (%)'].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=study_avg.index, y=study_avg.values, palette='Greens_d')
plt.title('Average Exam Score by Study Hours')
plt.xlabel('Study Hours per Week')
plt.ylabel('Average Exam Score (%)')
plt.grid(True)
plt.savefig(os.path.join(VISUALS_FOLDER, "study_hours_vs_exam_score.png"))
plt.close()

### SOCIAL MEDIA USAGE VS. EXAM SCORE (Darker Orange Bar Chart)
df['Social_Media_Category'] = pd.cut(df['Time_Spent_on_Social_Media (hours/week)'], bins=[0, 5, 10, 15, 20, 25, 30], labels=['0-5', '6-10', '11-15', '16-20', '21-25', '26-30'])
social_avg = df.groupby('Social_Media_Category')['Exam_Score (%)'].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=social_avg.index, y=social_avg.values, palette='Oranges_d')
plt.title('Average Exam Score by Social Media Usage')
plt.xlabel('Time Spent on Social Media (hours/week)')
plt.ylabel('Average Exam Score (%)')
plt.grid(True)
plt.savefig(os.path.join(VISUALS_FOLDER, "social_media_vs_exam_score.png"))
plt.close()

### SLEEP HOURS VS. EXAM SCORE (Darker Purple Bar Chart)
sleep_avg = df.groupby('Sleep_Hours_per_Night')['Exam_Score (%)'].mean()

plt.figure(figsize=(8, 6))
sns.barplot(x=sleep_avg.index, y=sleep_avg.values, palette='Purples_d')
plt.title('Average Exam Score by Sleep Hours')
plt.xlabel('Sleep Hours per Night')
plt.ylabel('Average Exam Score (%)')
plt.grid(True)
plt.savefig(os.path.join(VISUALS_FOLDER, "sleep_hours_vs_exam_score.png"))
plt.close()

### LEARNING STYLE VS. EXAM SCORE (Deep Magma Color Palette)
plt.figure(figsize=(8, 6))
sns.barplot(x='Preferred_Learning_Style', y='Exam_Score (%)', data=df, ci=None, palette='magma')
plt.title('Average Exam Score by Learning Style')
plt.xlabel('Learning Style')
plt.ylabel('Average Exam Score (%)')
plt.grid(True)
plt.savefig(os.path.join(VISUALS_FOLDER, "avg_exam_score_by_learning_style.png"))
plt.close()

print(f"All visualizations saved in: {VISUALS_FOLDER}")

