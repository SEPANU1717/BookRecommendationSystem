# Book Recommendation System for Programmers

This project is a **Streamlit web application** that recommends programming books using a **content-based filtering** approach.

## Project Overview

The app lets users:

- Select a programming book and receive similar book recommendations
- View categorized book lists by programming language/topic
- Read project and team information
- Send messages using the contact form

The recommendation flow uses:

- `bastonedd.csv` as the main book metadata source
- `similarity.pkl` as the precomputed similarity matrix

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Pillow

## Project Structure

- `/🏠Home_Page.py` – main entry page and app shell
- `/pages/01_🔎Recommendation.py` – recommendation page
- `/pages/02_📚Book_List.py` – categorized book listing page
- `/pages/03_👥About.py` – about/project/team information
- `/pages/04_☎Contact.py` – contact form page
- `/csvfiles/` – category-based CSV files
- `/image/` – UI assets and backgrounds
- `bastonedd.csv` – primary recommendation dataset
- `similarity.pkl` – similarity model data

## How to Run

1. Create and activate a Python virtual environment (recommended).
2. Install dependencies:

   ```bash
   pip install streamlit pandas numpy pillow
   ```

3. Run the app:

   ```bash
   streamlit run "🏠Home_Page.py"
   ```

4. Open the local Streamlit URL shown in your terminal.

## Notes

- The repository includes additional CSV and PKL artifacts used by the app.
- The UI uses custom styling plus background images from the `image/` folder.
