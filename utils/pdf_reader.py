from pypdf import PdfReader


def pdf_reader(file_name:str) :
    pdf = PdfReader(file_name)
    full_text = ""


    for i in pdf.pages:
        extracted_text = i.extract_text()
        if extracted_text is None:
            pass
        else:
            full_text = full_text + extracted_text

    return full_text
