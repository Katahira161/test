from pdf2image import convert_from_path

images = convert_from_path('C:\\python_test\\スマモビキーホルダーオリジナル.pdf',poppler_path = "C:\\python_test\\venv\\poppler-23.08.0\\Library\\bin") 
for i in range(len(images)):
          images[i].save('original.png', 'PNG')