# Customer Feedback Analysis of Amazon Books

## Project Overview

This project involves the analysis of customer feedback for books on Amazon. The primary goal is to conduct sentiment analysis on the reviews and utilize Azure for enhanced data storage and analysis. The project is divided into four weeks, each focusing on specific tasks.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Week 1: Data Collection and SQL Database Setup](#week-1-data-collection-and-sql-database-setup)
- [Week 2: Data Preprocessing and Analysis](#week-2-data-preprocessing-and-analysis)
- [Week 3: Sentiment Analysis and Azure Integration](#week-3-sentiment-analysis-and-azure-integration)
- [Week 4: Model Deployment and Presentation](#week-4-model-deployment-and-presentation)
- [How to Run the Project](#how-to-run-the-project)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- Python
  - Libraries: `Pandas`, `NumPy`, `Scikit-learn`, `NLTK`, `VADER`, `SpaCy`
- Azure Data Services
- SQL Server
- MLflow (for model tracking)

## Project Structure

```
.
├── data
│   ├── reviews.csv
│   ├── books.csv
├── notebooks
│   ├── data_analysis.ipynb
│   ├── sentiment_analysis.ipynb
├── src
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   ├── model.py
├── requirements.txt
└── README.md
```

## Week 1: Data Collection and SQL Database Setup

- **Tasks:**
  - Collected customer feedback data from Amazon.
  - Designed and set up a SQL database to store reviews and book details.

## Week 2: Data Preprocessing and Analysis

- **Tasks:**
  - Preprocessed the data by cleaning, transforming, and aggregating it for analysis.
  - Analyzed the collected data to extract insights on customer feedback.

## Week 3: Sentiment Analysis and Azure Integration

- **Tasks:**
  - Built sentiment analysis models using Python to classify feedback into positive, neutral, or negative categories.
  - Integrated Azure Data Services for enhanced storage and analysis of feedback data.
  - Assessed sentiment analysis models and refined as needed.

## Week 4: Model Deployment and Presentation

- **Tasks:**
  - Deployed the sentiment analysis model for real-time feedback classification.
  - Summarized project work and prepared for final presentation.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amazon-feedback-analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd amazon-feedback-analysis
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebooks for analysis:
   ```bash
   jupyter notebook notebooks/data_analysis.ipynb
   jupyter notebook notebooks/sentiment_analysis.ipynb
   ```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License.
