import PyPDF2
import os

d = r'c:\AB-PMJAY-Hackathon\ps-2\PS2_Output_Guidelines\Guidelines'
out_path = r'c:\AB-PMJAY-Hackathon\ps-2\pdf_contents.md'

with open(out_path, 'w', encoding='utf-8') as out_file:
    for f in os.listdir(d):
        if f.endswith('.pdf'):
            out_file.write(f'\n# {f}\n\n')
            pdf_path = os.path.join(d, f)
            try:
                reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        out_file.write(text + '\n')
            except Exception as e:
                out_file.write(f"Error reading {f}: {e}\n")
