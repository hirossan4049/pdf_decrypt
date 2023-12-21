import PyPDF2
import os

def decrypt_pdf(input_path, output_path, password):
    print(input_path, output_path, password)
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if reader.is_encrypted:
            reader.decrypt(password)

            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            print(f"Decrypted: {input_path}")
        else:
            print(f"No encryption: {input_path}")

# パスワードをここに設定
password = "password"

# フォルダ内のすべてのPDFファイルに対して実行
input_folder_path = "pdfs"
output_folder_path = "outputs"

for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.pdf'):
        input_path = os.path.join(input_folder_path, file_name)
        output_path = os.path.join(output_folder_path, "decrypted_" + file_name)
        decrypt_pdf(input_path, output_path, password)
