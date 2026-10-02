from pathlib import Path
import pymupdf
import re


def load_text_file(file_path):
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return [{
        "text": text,
        "metadata": {
            "source": path.name,
            "file_type": ".txt",
            "characters": len(text)
        }
    }]


def load_pdf(file_path):
    path = Path(file_path)

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document):
        pages.append({
            "text": page.get_text(),
            "metadata": {
                "source": path.name,
                "page": page_number + 1,
                "characters" : len(page.get_text())
            }
        })

    document.close()

    return pages


def load_document(file_path):
    path = Path(file_path)

    if path.suffix == ".txt":
        return load_text_file(file_path)

    elif path.suffix == ".pdf":
        return load_pdf(file_path)

    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")


documents = load_document("sample.txt")


for document in documents:
    print(document)