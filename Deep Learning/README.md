## Word Embedding using Keras Embedding Layer
This project demonstrates how to use the Keras Embedding Layer to convert categorical text data into dense vector representations (embeddings). Word embeddings are essential in Natural Language Processing (NLP), as they capture semantic meaning and contextual relationships between words in a numerical form, enabling deep learning models to process and learn from text data effectively.

### 🎯 Objective
- To develop a simple text classification pipeline using:
- Preprocessing and tokenization of text data
- Conversion of words into embedded vector representations
- A neural network model trained on the embedded input
- Evaluation of model performance in a binary classification task

### 🧰 Technologies Used
Language:
- Python

Libraries:
- pandas, numpy – Data handling
- tensorflow.keras – Building and training the model
- sklearn – Train-test split and evaluation

### 🧠 Embedding Technique Used
- Keras Embedding Layer
- Learns a dense vector representation for each word in the vocabulary
- Embedding dimension: 10
- Input is integer-encoded word sequences
- Used as the first layer of the neural network

### 📊 Workflow
Data Preparation
- Sample sentences labeled with binary outputs
- Tokenization and padding of text sequences
Model Architecture
- Embedding Layer: Converts words to vectors
- Flatten Layer: Converts 2D embedding output to 1D
- Dense Layers: Fully connected layers for classification

Training
- Loss Function: Binary Crossentropy
- Optimizer: Adam
- Epochs: 100
- Evaluation
- Accuracy metrics used to assess performance
- Visualization of accuracy and loss over epochs

### 🔑 Key Insights
- The Keras Embedding Layer is a powerful tool for converting text into a numerical form suitable for deep learning models.
- Embeddings help models capture relationships between words better than traditional one-hot encoding.
- A simple neural network can achieve good results on small text datasets using learned embeddings.

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
