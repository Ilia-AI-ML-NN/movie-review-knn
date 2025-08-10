🎬 AI Movie Review Analyzer
An AI-powered tool that analyzes movie reviews using KNN and TF-IDF to:

Identify whether the review is written by a viewer or a critic

Predict the movie rating on a 10-point scale

📌 Features
K-Nearest Neighbors (KNN) classification

TF-IDF text vectorization

Two independent models:

Source classifier (viewer or critic)

Rating classifier (1–10)

Model persistence with joblib (no need to retrain every run)

Interactive CLI input for review analysis

Color-coded console output

🛠 Installation
Clone the repository:

bash
Копировать
Редактировать
git clone https://github.com/YourUsername/movie-review-analyzer.git
cd movie-review-analyzer
Install dependencies:

bash
Копировать
Редактировать
pip install -r requirements.txt
▶ Usage
Run the program:

bash
Копировать
Редактировать
python main.py
Example:

bash
Копировать
Редактировать
Введите новый отзыв для анализа (или 'exit' для выхода): Отличный сюжет, шикарная игра актёров
Отзыв от: зритель
Оценка фильма по 10-бальной шкале: 9
📂 Project Structure
graphql
Копировать
Редактировать
movie-review-analyzer/
│── main.py                # Main application
│── requirements.txt       # Dependencies
│── knn_source_model.joblib  # Saved source classifier
│── source_vectorizer.joblib # TF-IDF vectorizer for source
│── knn_rating_model.joblib  # Saved rating classifier
│── rating_vectorizer.joblib # TF-IDF vectorizer for rating
└── README.md
📊 Example Training Data
Review	Source	Rating
Отлично снято, шикарный сюжет	зритель	10
Скучный и нудный фильм	критик	3
Мой любимый фильм, супер актёры	зритель	9
Ужасно, плохой сюжет	критик	2

📜 License
MIT License – feel free to use and modify this project.
