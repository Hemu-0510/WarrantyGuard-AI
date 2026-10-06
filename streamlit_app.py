import streamlit as st
import tempfile
from ocr import extract_text
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(
    page_title="Warranty Guard AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("Warranty Guard AI")
st.write("Upload a warranty invoice or bill to analyze warranty details.")

uploaded_file = st.file_uploader(
    "Upload Warranty Document",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Document", width=500)

    if st.button("Analyze Warranty"):

        # Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as temp_file:

            temp_file.write(uploaded_file.getbuffer())
            image_path = temp_file.name

        # OCR
        text = extract_text(image_path)

        st.subheader("Extracted Text")
        st.text_area(
            "OCR Result",
            text,
            height=250
        )

        # Find date
        date_pattern = r"\b\d{2}[./-]\d{2}[./-]\d{4}\b"
        dates = re.findall(date_pattern, text)

        # Find warranty
        warranty_line = None

        for line in text.splitlines():

            line_lower = line.lower()

            if "warrant" in line_lower or "warranly" in line_lower:
                warranty_line = line.strip()
                break

        # Find product
        product = "Not Found"

        if "air cooler" in text.lower() or "alr cooler" in text.lower():
            product = "Air Cooler"

        # Display information
        st.subheader("Warranty Information")

        if dates:
            invoice_date_text = dates[0]
            st.write("**Invoice Date:**", invoice_date_text)

            try:
                invoice_date = datetime.strptime(
                    invoice_date_text,
                    "%d.%m.%Y"
                )

                expiry_date = invoice_date + relativedelta(years=1)

                today = datetime.today()

                st.write(
                    "**Warranty Start Date:**",
                    invoice_date.strftime("%d-%m-%Y")
                )

                st.write(
                    "**Warranty Expiry Date:**",
                    expiry_date.strftime("%d-%m-%Y")
                )

                st.write("**Warranty Period:** 1 Year")

                if today <= expiry_date:
                    st.success("Warranty Status: ACTIVE")
                else:
                    st.error("Warranty Status: EXPIRED")

            except:
                st.warning("Could not calculate warranty date.")

        else:
            st.warning("Invoice date not found.")

        st.write("**Product:**", product)

        if warranty_line:
            st.write("**Warranty Details:**", warranty_line)
        else:
            st.write("**Warranty Details:** Not Found")