import PyPDF2
import os

def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        if reader.isEncrypted:
            reader.decrypt(password)

            writer = PyPDF2.PdfFileWriter()
            for i in range(reader.getNumPages()):
                writer.addPage(reader.getPage(i))

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            print(f"Decrypted: {input_path}")
        else:
            print(f"No encryption: {input_path}")

password = "password"

# フォルダ内のすべてのPDFファイルに対して実行
folder_path = "pdfs"
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):
        input_path = os.path.join(folder_path, file_name)
        output_path = os.path.join(folder_path, "decrypted_" + file_name)
        decrypt_pdf(input_path, output_path, password)
