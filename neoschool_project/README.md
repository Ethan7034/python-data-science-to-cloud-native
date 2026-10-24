# Neoschool General Lecture Project: Food Safety News Analysis

This folder contains the code and dataset for the Neoschool NLP project. The project is architected as a modular data pipeline, designed to bridge web data acquisition with Natural Language Processing (NLP) analysis for real-world food safety and supply chain news.

## 📂 Directory Structure
- `news_data/`: Storage for raw text datasets.
- `scraper.py`: Data acquisition module.
- `nlp_pipeline.py`: NLP processing module.

## 🏗️ Project Framework

The project is structured into two primary functional modules:

### Module 1: Data Acquisition (`scraper.py`)
This module is responsible for fetching external data and building the local dataset. 
- **Engine**: Utilizes `requests` and `BeautifulSoup` to parse the China National Radio (CNR) website.
- **Mechanisms**: Implements custom `User-Agent` spoofing, dynamic encoding detection (`apparent_encoding`), and comprehensive exception handling (`RequestException`).
- **Output**: Extracts structured article titles and raw text, exporting them as `.txt` files into the `news_data` directory for downstream processing.

### Module 2: NLP Pipeline (`nlp_pipeline.py`)
This module serves as the core processing unit for the acquired text corpus.
- **Processing Flow**: Loads the raw text from `news_data`, performs noise reduction and tokenization.
- **Analysis**: Designed to execute word frequency analysis and sentiment evaluation to extract insights from the food safety reports.

## 🛠️ Dependencies
- Python 3
- `requests`, `beautifulsoup4`
- *(NLP Pipeline)*: `pandas`, `jieba`, `scikit-learn`

## 💻 Execution
To initiate the data acquisition module:
```bash
python scraper.py