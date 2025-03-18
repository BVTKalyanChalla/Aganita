import requests
import xmltodict
import csv
import argparse
from google.colab import files

# Function to fetch papers from PubMed
def fetch_papers(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 25,
        "retmode": "xml"
    }
    
    response = requests.get(base_url, params=params)
    data = xmltodict.parse(response.text)
    
    paper_ids = data["eSearchResult"].get("IdList", {}).get("Id", [])
    return paper_ids

# Function to fetch details of papers
def fetch_paper_details(paper_ids):
    if not paper_ids:
        return []
    
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    
    response = requests.get(base_url, params=params)
    data = xmltodict.parse(response.text)
    
    papers = []
    try:
        articles = data["PubmedArticleSet"]["PubmedArticle"]
        if not isinstance(articles, list):
            articles = [articles]

        for article in articles:
            pubmed_id = article["MedlineCitation"]["PMID"]["#text"]
            title = article["MedlineCitation"]["Article"]["ArticleTitle"]
            pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"].get("Year", "N/A")

            authors_list = article["MedlineCitation"]["Article"].get("AuthorList", {}).get("Author", [])
            if not isinstance(authors_list, list):
                authors_list = [authors_list]

            non_academic_authors = []
            company_affiliations = []
            corresponding_email = "N/A"

            for author in authors_list:
                affiliation = author.get("AffiliationInfo", {})
                if isinstance(affiliation, list):
                    affiliation = affiliation[0]

                affiliation_text = affiliation.get("Affiliation", "") if affiliation else ""
                email = affiliation_text.split()[-1] if "@" in affiliation_text else "N/A"

                if affiliation_text and any(keyword in affiliation_text.lower() for keyword in ["pharma", "biotech", "inc", "ltd", "corporation"]):
                    non_academic_authors.append(author.get("LastName", "Unknown"))
                    company_affiliations.append(affiliation_text)

                if email != "N/A":
                    corresponding_email = email

            papers.append([pubmed_id, title, pub_date, "; ".join(non_academic_authors), "; ".join(company_affiliations), corresponding_email])

    except Exception as e:
        print("Error fetching paper details:", e)

    return papers

# Function to save results to a CSV file
def save_to_csv(papers, filename):
    headers = ["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations", "Corresponding Author Email"]
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(papers)

# Main function
def main(args=None):
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results", default="results.csv")

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    print("Fetching papers for query:", args.query)
    paper_ids = fetch_papers(args.query)
    papers = fetch_paper_details(paper_ids)

    if papers:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")

        # Download file in Colab
        files.download(args.file)
    else:
        print("No papers found.")

# Run the script in Colab
main(["AI", "-f", "results.csv"])
