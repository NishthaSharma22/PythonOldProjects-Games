import PyPDF2, pyttsx3

pdf_reader = PyPDF2.PdfReader(open('peterpan.pdf', 'rb'))
speaker = pyttsx3.init()
for pag_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pag_num].extract_text()
    clean_pag = text.strip().replace('\n', ' ')
    print(clean_pag)
speaker.save_to_file(clean_pag, 'story.mp3')
speaker.runAndWait()
speaker.stop()
