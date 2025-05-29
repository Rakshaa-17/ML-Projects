## 🎬 Basic Movie Recommender System
This project builds a simple yet effective Movie Recommender System using unsupervised learning techniques. By analyzing user preferences and movie features, the system suggests similar movies to enhance user experience and engagement.

### 🎯 Objective
- Build a basic content-based movie recommendation system
- Recommend movies that are similar in genre and content
- Help users discover new movies aligned with their preferences

### 🧰 Technologies Used
Programming Language:

- Python

Libraries:

- pandas, numpy – Data manipulation
- scikit-learn – Vectorization and similarity computation
- nltk – Text preprocessing
- matplotlib, seaborn – Visualization (if applicable)

### 📊 Data Preprocessing
Loaded movie metadata containing titles, genres, keywords, etc.

- Handled missing values and cleaned data
- Combined relevant textual features into a single representation
- Used TF-IDF Vectorization to convert text into numerical format

### 🔍 Recommendation Logic
- Calculated cosine similarity between movie vectors
- For a given movie, retrieved top N most similar movies
- Displayed recommendations based on content similarity (e.g., genre, plot keywords)

### 💡 Example Output 

Given the input movie "The Dark Knight" → Recommended:
Batman Begins
The Prestige
Iron Man
Spider-Man 2
Avengers: Infinity War

### 📌 Features
- Content-based filtering using TF-IDF and cosine similarity
- Easy to extend with new data or switch to collaborative filtering
- Simple, explainable logic ideal for learning purposes

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
