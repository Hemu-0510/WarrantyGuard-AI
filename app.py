from ocr import extract_text
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Image file
image_path = "test.jpeg"

# OCR
text = extract_text(image_path)

print("\n========== WARRANTY GUARD AI ==========")

print("\nExtracted Text:")
print(text)

# -------------------------------
# Find Invoice Date
# -------------------------------

date_pattern = r"\b\d{2}[./-]\d{2}[./-]\d{4}\b"
dates = re.findall(date_pattern, text)

print("\n========== WARRANTY INFORMATION ==========")

if dates:
    invoice_date_text = dates[0]
    print("Invoice Date:", invoice_date_text)
else:
    invoice_date_text = None
    print("Invoice Date: Not Found")

# -------------------------------
# Find Warranty
# -------------------------------

warranty_found = False

for line in text.splitlines():

    line_lower = line.lower()

    if "warrant" in line_lower or "warranly" in line_lower:

        print("Warranty Details:", line.strip())
        warranty_found = True

if not warranty_found:
    print("Warranty Details: Not Found")

# -------------------------------
# Product
# -------------------------------

if "air cooler" in text.lower():
    print("Product: Air Cooler")
else:
    print("Product: Not Found")

# -------------------------------
# Warranty Calculation
# -------------------------------

if invoice_date_text:

    try:

        invoice_date = datetime.strptime(
            invoice_date_text,
            "%d.%m.%Y"
        )

        # Extended warranty = 1 year
        warranty_years = 1

        expiry_date = invoice_date + relativedelta(
            years=warranty_years
        )

        today = datetime.today()

        print("\nWarranty Period: 1 Year")

        print(
            "Warranty Start Date:",
            invoice_date.strftime("%d-%m-%Y")
        )

        print(
            "Warranty Expiry Date:",
            expiry_date.strftime("%d-%m-%Y")
        )

        if today <= expiry_date:
            print("Warranty Status: ACTIVE")
        else:
            print("Warranty Status: EXPIRED")

    except Exception as error:

        print("Warranty calculation error:", error)

print("\n==========================================")