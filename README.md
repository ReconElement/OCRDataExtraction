# OCRDataExtraction
This project contains the source code for an OCR data extraction and db operations with the data so extracted
======================================================================================================================================================================
1. Install tesseract-ocr, add it to the system environment variables if in windows
2. Install pytesseract and use it, it is a wrapper on tesseract-ocr cmd
3. Install pdf2image, add it to the system environment path variables if in windows
4. Use pdf2image pip package to interact with pdf2image executable to enhance and perform various efficiency enhancing procedures on files in dataset_documents
5. Run db_init.py script to initialize the database and neccessary tables before going to the next step.
6. On running the script.py script file, data is extracted using tesseract ocr from pdf, arranged and filtered using various functions and then is written in DB and is dumped in the directory ./json_file_storage
