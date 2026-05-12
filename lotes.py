import fitz
import os

def obter_info_lotes(diretorio_pdfs):
    info_lotes = {}

    # Itera sobre todos os arquivos no diretório
    for arquivo_pdf in os.listdir(diretorio_pdfs):
        if arquivo_pdf.endswith('.pdf'):
            arquivo_pdf_path = os.path.join(diretorio_pdfs, arquivo_pdf)

            pdf_doc = fitz.open(arquivo_pdf_path)

            # Itera sobre todas as páginas para identificar os lotes
            for pagina_num in range(pdf_doc.page_count):
                pagina = pdf_doc[pagina_num]
                texto = pagina.get_text()

                # Identifica o lote com base em um padrão (por exemplo, "Lote:")
                if 'Lote:' in texto:
                    # Obtém o número do lote (ajuste conforme necessário)
                    numero_lote = texto.split('Lote:')[1].split()[0]

                    # Adiciona o número do lote e a quantidade de páginas ao dicionário
                    if numero_lote not in info_lotes:
                        info_lotes[numero_lote] = 0

                    info_lotes[numero_lote] += 1

            pdf_doc.close()

    return info_lotes

if __name__ == "__main__":
    # Caminho para o diretório contendo os arquivos PDF
    diretorio_pdfs = "C:/Importar Drive/pdf"

    # Obtém informações sobre os lotes nos arquivos PDF
    info_lotes = obter_info_lotes(diretorio_pdfs)

    # Exibe as informações obtidas
    print("Informações sobre lotes:")
    for numero_lote, num_paginas in info_lotes.items():
        print(f"Lote {numero_lote}: {num_paginas} página(s)")
