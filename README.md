# Warranty Guard AI

## Overview

Warranty Guard AI is a Python-based application that extracts warranty information from invoices and warranty documents using Optical Character Recognition (OCR).

The application allows users to upload an invoice image and automatically identifies important details such as the product, invoice date, warranty period, warranty expiry date, and warranty status.

## Features

* Upload warranty invoice images
* Extract text using EasyOCR
* Detect invoice date
* Identify product information
* Calculate warranty expiry date
* Check whether the warranty is Active or Expired
* Simple web interface using Streamlit

## Technologies Used

* Python
* EasyOCR
* Streamlit
* Regular Expressions
* Python DateTime
* Python Dateutil

## How It Works

1. User uploads a warranty invoice image.
2. EasyOCR extracts text from the image.
3. Python processes the extracted text.
4. The system identifies warranty-related information.
5. The warranty expiry date is calculated.
6. The application displays the warranty status.

## Project Structure

```text
Warranty-Guard-AI/
│
├── app.py
├── streamlit_app.py
├── ocr.py
├── test.jpeg
├── requirements.txt
└── README.md
```

## Output
<img width="1600" height="793" alt="image" src="https://github.com/user-attachments/assets/21a6d2d7-3385-42bf-a4d4-46848590b7b0" />
<img width="1597" height="858" alt="image" src="https://github.com/user-attachments/assets/0bbb87b8-1a2f-4927-8d6f-7858bda035be" />

## Usefulness

Warranty Guard AI helps users quickly check warranty information without manually reading the complete invoice. It can be useful for customers, stores, and service centers for simple warranty tracking.



## Author

**Hemalatha M**
B.Sc Computer Science with AI
