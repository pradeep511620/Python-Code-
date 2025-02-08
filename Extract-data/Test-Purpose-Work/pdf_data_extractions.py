
import pdfplumber

pdf_path = "downloaded_pdf.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for table in tables:
            print(f"Page {page_num + 1} Table:\n")
            for row in table:
                print(row)
                # with open('table.txt', 'a+', encoding='utf-8') as table_save:
                #     table_save.write(f"{row}\n")



