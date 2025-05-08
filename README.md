# Collect Lobby Register Data in Germany
![Logo](./bundestag_register.png)

## Project Description

This project automates the collection and processing of lobby register data from [official German Bundestag Website](https://www.lobbyregister.bundestag.de/startseite?lang=de).

**Please note**: This project was developed prior to whole batch JSON downloads being available on the Lobby Register website. 

### Features

    ⚡ Automated PDF downloading from German Lobby Register

    📂 PDF merging into single file

    🗃️ Data extraction from PDF to structured CSV format

Requirements

    Python 3.x

    Required Python packages (incl. selenium and PyPDF2 -  full list in requirements.txt)

    Internet connection for downloading files

Installation

    Clone this repository

    Install required packages: pip install -r requirements.txt

Usage (to be updated)

Run the main script with:

``` python main.py ```

Output Structure
```
/output
├── raw_pdfs/           # Downloaded individual PDFs
├── merged.pdf          # Combined PDF
└── lobby_data.csv      # Final extracted data
```
