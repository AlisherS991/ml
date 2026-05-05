IT Job Role Predictor — Streamlit Web App (Multi‑page)

A functional multi‑page Streamlit app based on your notebook (fianl.ipynb). It loads your CSV data, trains classic ML models, shows performance charts, and provides a dedicated Predict page.

Quick start
- Requirements: Python 3.9+ and pip
- In a terminal at this folder:
  pip install -r requirements.txt
  streamlit run streamlit_app.py
Then open the URL shown (usually http://localhost:8501).

Data options
You can use the provided CSVs in the project root or upload your own via the UI.
- Local files (default):
  - IT_Job_Roles_Skills.csv
  - real_dataset_v2 (1).csv
- Upload instead: In the sidebar, uncheck "Use local CSV files" and upload both CSVs.

Navigation (left sidebar)
- Home: overview and instructions.
- Data & Training (main page): load/upload data, train models, and view metrics/plots.
- Predict: after training, enter skills to get a predicted role (uses the cached model).

Step‑by‑step (with optional virtual env)
1) Create and activate a virtual env (optional but recommended):
   - Windows (PowerShell):
     python -m venv .venv
     .venv\Scripts\Activate.ps1
   - macOS/Linux (bash/zsh):
     python3 -m venv .venv
     source .venv/bin/activate
2) Install dependencies:
   pip install -r requirements.txt
3) Place CSVs next to this README (or plan to upload in the UI):
   - IT_Job_Roles_Skills.csv
   - real_dataset_v2 (1).csv
4) Launch the app:
   streamlit run streamlit_app.py
5) In the app:
   - If using local files, proceed to Training.
   - If uploading, uncheck the sidebar toggle and upload both CSVs.
   - Click through Training; the model and vectorizer are cached for this session.
   - Go to Predict to try your skills text.

What the app does
- Cleans and merges the two datasets.
- Uses TF‑IDF vectorizer (max_features=500).
- Trains three models: k‑NN, Perceptron (balanced), SVM Linear (balanced).
- Displays model accuracies and a confusion matrix for the best model.
- Lets you enter skills text and predicts the most likely IT role.

Troubleshooting
- Missing CSVs message: Either place both CSVs in the project root or upload both in the sidebar.
- Missing columns error: Ensure your CSVs have the following columns:
  - Kaggle‑like: Job Title, Skills
  - Custom: job_skill_set, category
- Not enough data/classes: The app removes classes with 10 or fewer samples; provide larger datasets if you see this error.
- Port already in use: Run on another port:
  streamlit run streamlit_app.py --server.port 8502
- Module not found: Make sure you installed requirements in the active environment and are launching from the project folder.

Notes
- Training happens at runtime after you provide/confirm datasets. The trained model is cached in session for the Predict page; a browser refresh or app restart clears the cache.
- The app mirrors the notebook’s preprocessing and modeling as closely as possible.

Project layout
- streamlit_app.py — Data & Training page (main entrypoint)
- pages/1_Home.py — Home page
- pages/2_Predict.py — Predict page
- ml_core.py — shared data/ML helpers
- requirements.txt — Python dependencies
- IT_Job_Roles_Skills.csv, real_dataset_v2 (1).csv — example datasets
