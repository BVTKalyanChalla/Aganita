# 📄 PubMed Research Paper Fetcher

## 📝 Project Overview
This Python command-line tool fetches **research papers from PubMed** based on a user-specified query. It filters papers where **at least one author is affiliated with a pharmaceutical or biotech company** and saves the results as a **CSV file**.

---
## 🚀 Features
✔ **Fetches papers** from PubMed using **NCBI Entrez API**  
✔ **Filters non-academic authors** (pharmaceutical/biotech affiliations)  
✔ **Outputs a CSV file** with detailed paper information  
✔ **Command-line interface** with multiple options  
✔ **Colab-compatible script** for easy execution  

---
## 📂 Output CSV Format
The output file contains the following columns:

| Column | Description |
|--------|-------------|
| **PubmedID** | Unique identifier for the paper |
| **Title** | Title of the paper |
| **Publication Date** | Date the paper was published |
| **Non-academic Authors** | Names of authors affiliated with biotech/pharma companies |
| **Company Affiliations** | Names of pharmaceutical/biotech companies |
| **Corresponding Author Email** | Email of the corresponding author |

---
## 🛠️ Installation & Setup
### **1️⃣ Install Dependencies**
Ensure Python is installed (Python 3.7+ recommended). Then, install dependencies:
```sh
pip install requests xmltodict argparse
```

### **2️⃣ Run in Google Colab**
If using **Google Colab**, simply run the provided script, and it will automatically fetch and download results.

### **3️⃣ Running Locally (Command-Line Usage)**
```sh
python fetch_papers.py "cancer research" -f results.csv
```
- Replace **"cancer research"** with your search query.
- The `-f` option specifies the output file name (default: `results.csv`).

---
## 🖥️ Command-Line Options
| Option | Description |
|--------|-------------|
| `-h` or `--help` | Display usage instructions |
| `-d` or `--debug` | Print debug information during execution |
| `-f` or `--file` | Specify filename to save results (default: `results.csv`) |

---
## 🔍 How It Works
1️⃣ **Searches PubMed** using the query provided.  
2️⃣ **Retrieves paper IDs** and fetches details.  
3️⃣ **Filters authors affiliated with biotech/pharma**.  
4️⃣ **Extracts corresponding author email**.  
5️⃣ **Saves results to CSV** and downloads it (if in Colab).  

---
## 💡 Example Output (CSV)
```
PubmedID, Title, Publication Date, Non-academic Authors, Company Affiliations, Corresponding Author Email
12345678, "Breakthrough in Cancer Treatment", 2023, "John Doe", "XYZ Pharma Inc.", "johndoe@xyzpharma.com"
```

---
## 📌 Dependencies
- Python 3.7+
- `requests` (For API requests)
- `xmltodict` (For XML parsing)
- `argparse` (For command-line parsing)

---
## ⚙️ Development & Contribution
🔹 Clone this repository:  
```sh
git clone https://github.com/BVTKalyanChalla/pubmed-fetcher.git
cd pubmed-fetcher
```
🔹 Run the script:  
```sh
python fetch_papers.py "diabetes treatment" -f diabetes_papers.csv
```
🔹 Contribute by submitting pull requests! 🎯

---
## 📬 Contact
For any queries, reach out via GitHub issues or email: `chbhanuvtkalyan@gmail.com` 📩

