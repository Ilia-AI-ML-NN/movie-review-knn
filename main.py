import joblib
import logging
import re
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from colorama import Fore, Style, init

init(autoreset=True)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data():
    """Загружает и возвращает данные для обучения моделей."""
    reviews = [
        "Отлично снято, шикарный сюжет",
        "Скучный и нудный фильм",
        "Мой любимый фильм, супер актёры",
        "Ужасно, плохой сюжет",
        "Классный фильм, шикарно сыграно",
        "Нудный и тупой фильм",
        "Супер фильм, отлично снято",
        "Скучный и плохой фильм",
        "Фильм обычный, ничего особенного",
        "Средний фильм, есть моменты"
    ]

    source_labels = [
        "зритель",
        "критик",
        "зритель",
        "критик",
        "зритель",
        "критик",
        "зритель",
        "критик",
        "зритель",
        "критик"
    ]

    rating_labels = [
        "10",  
        "3",   
        "9",
        "2",
        "8",
        "4",
        "9",
        "3",
        "5",
        "6"
    ]

    return reviews, source_labels, rating_labels

def train_model(reviews, labels, k=3):
    """Обучает KNN модель с TF-IDF векторизацией."""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(reviews)
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, labels)
    return model, vectorizer

def predict_label(model, vectorizer, review):
    """Делает предсказание для нового текста."""
    cleaned_text = re.sub(r"[^\w\s]", "", review).strip()
    if not cleaned_text:
        logging.error("Отзыв пустой или содержит только знаки препинания")
        return None

    X = vectorizer.transform([cleaned_text])
    prediction = model.predict(X)
    return prediction[0]

def save_model(model, vectorizer, model_path, vectorizer_path):
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

def load_model(model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def main():
    source_model_path = "knn_source_model.joblib"
    source_vectorizer_path = "source_vectorizer.joblib"
    rating_model_path = "knn_rating_model.joblib"
    rating_vectorizer_path = "rating_vectorizer.joblib"

    if os.path.exists(source_model_path) and os.path.exists(source_vectorizer_path):
        logging.info("📦 Загружаем модель источника...")
        source_model, source_vectorizer = load_model(source_model_path, source_vectorizer_path)
    else:
        logging.info("⚙ Обучаем модель источника...")
        reviews, source_labels, rating_labels = load_data()
        source_model, source_vectorizer = train_model(reviews, source_labels)
        save_model(source_model, source_vectorizer, source_model_path, source_vectorizer_path)

    if os.path.exists(rating_model_path) and os.path.exists(rating_vectorizer_path):
        logging.info("📦 Загружаем модель рейтинга...")
        rating_model, rating_vectorizer = load_model(rating_model_path, rating_vectorizer_path)
    else:
        logging.info("⚙ Обучаем модель рейтинга...")
        if 'reviews' not in locals():
            reviews, source_labels, rating_labels = load_data()
        rating_model, rating_vectorizer = train_model(reviews, rating_labels)
        save_model(rating_model, rating_vectorizer, rating_model_path, rating_vectorizer_path)

    while True:
        new_review = input("Введите новый отзыв для анализа (или 'exit' для выхода): ")
        if new_review.lower() == "exit":
            logging.info("Выход из программы")
            break

        source_pred = predict_label(source_model, source_vectorizer, new_review)
        rating_pred = predict_label(rating_model, rating_vectorizer, new_review)

        if source_pred is None or rating_pred is None:
            print(Fore.YELLOW + "Невозможно сделать прогноз по введённому отзыву" + Style.RESET_ALL)
            continue

        print(f"Отзыв от: {source_pred}")
        print(F"Оценка фильма по 10-бальной шкале: {Fore.CYAN}{rating_pred}{Style.RESET_ALL}")

    logging.info("Работа программы завершена")

if __name__ == "__main__":
    main()
