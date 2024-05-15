import PyPDF2

def search_name_in_pdf(pdf_file_path, name):
    found = False
    
    try:
        # Abrir o arquivo PDF em modo de leitura binária
        with open(pdf_file_path, 'rb') as file:
            # Criar um objeto PDFReader
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Iterar sobre cada página do PDF
            for page_number in range(len(pdf_reader.pages)):
                # Extrair o texto da página atual
                page_text = pdf_reader.pages[page_number].extract_text()
                
                # Verificar se o nome está presente no texto da página
                if name in page_text:
                    found = True
                    print(f'O nome "{name}" foi encontrado na página {page_number + 1}')
                    
    except FileNotFoundError:
        print(f'O arquivo "{pdf_file_path}" não foi encontrado.')
    except Exception as e:
        print('Ocorreu um erro:', e)
    
    if not found:
        print(f'O nome "{name}" não foi encontrado no PDF.')

def main():
    pdf_file_path = r'D:\OSINT\Bilingue_habilitados.pdf'  # Substitua pelo caminho do seu arquivo PDF
    name = "Daniel Felipe Marins Macedo"
    search_name_in_pdf(pdf_file_path, name)

if __name__ == '__main__':
    main()
