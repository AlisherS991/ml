import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib
import os


def categorize_job(title):
    title = str(title).lower()
    if any(k in title for k in ['data', 'ai', 'machine learning', 'ml', 'analyst']):
        return 'Data Science & Analytics'
    elif any(k in title for k in ['devops', 'kubernetes', 'docker', 'jenkins']):
        return 'DevOps & Infrastructure'
    elif any(k in title for k in ['frontend', 'react', 'javascript', 'web']):
        return 'Frontend Development'
    elif any(k in title for k in ['backend', 'software', 'engineer', 'python', 'java']):
        return 'Software Engineering'
    return 'Other IT Role'


def train_model():
    """Загружает данные и обучает модель 'на лету'"""
    try:
        df1 = pd.read_csv('IT_Job_Roles_Skills.csv', encoding='latin1')
        df2 = pd.read_csv('real_dataset_v2 (1).csv')

        df1['Target_Role'] = df1['Job Title'].apply(categorize_job)
        df1_clean = df1[['Skills', 'Target_Role']].rename(columns={'Skills': 'Skills_List'})

        # Маппинг для второго датасета
        mapping = {'Data Scientist': 'Data Science & Analytics', 'Software Engineer': 'Software Engineering'}
        df2['Target_Role'] = df2['category'].map(mapping).fillna('Other IT Role')
        df2_clean = df2[['job_skill_set', 'Target_Role']].rename(columns={'job_skill_set': 'Skills_List'})

        df = pd.concat([df1_clean, df2_clean]).dropna()

        vec = TfidfVectorizer(stop_words='english', max_features=500)
        X = vec.fit_transform(df['Skills_List'])
        y = df['Target_Role']

        model = SVC(kernel='linear', class_weight='balanced')
        model.fit(X, y)

        joblib.dump(model, 'model.joblib')
        joblib.dump(vec, 'vectorizer.joblib')
        return True
    except Exception as e:
        print(f"Ошибка обучения: {e}")
        return False


def get_prediction(skills_text):
    # Если файлов нет — обучаем автоматически
    if not os.path.exists('model.joblib') or not os.path.exists('vectorizer.joblib'):
        success = train_model()
        if not success:
            return "Ошибка: не удалось обучить модель (проверьте наличие CSV файлов)"

    model = joblib.load('model.joblib')
    vec = joblib.load('vectorizer.joblib')

    pred = model.predict(vec.transform([skills_text]))
    return pred[0]