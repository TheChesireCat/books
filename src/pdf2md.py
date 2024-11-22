# pip install pymupdf4llm
import os
import pymupdf4llm
import pathlib

pdf_files = os.listdir("pdfs")
pdf_files = [pdf for pdf in pdf_files if pdf.endswith(".pdf")]
for pdf in pdf_files:
    md_text = pymupdf4llm.to_markdown("pdfs/"+pdf)
    pathlib.Path("mds",pdf.split(".")[0] + ".md").write_bytes(md_text.encode())
    os.remove("pdfs/" + pdf)
    print(f"Processed and deleted: {pdf}")
