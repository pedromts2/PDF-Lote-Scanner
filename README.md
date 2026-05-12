# 📄 PDF Lote Scanner

Projeto em Python para leitura automática de arquivos PDF e identificação de lotes com contagem de páginas.

## 🚀 Funcionalidades

* Leitura automática de múltiplos PDFs
* Extração de texto das páginas
* Identificação automática de lotes
* Contagem de páginas por lote
* Exibição organizada no terminal

## 🛠 Tecnologias

* Python
* PyMuPDF (`fitz`)

## ▶ Instalação

```bash
pip install pymupdf
```

## ▶ Como executar

```bash
python main.py
```

## 📂 Estrutura

O programa lê automaticamente todos os PDFs da pasta configurada:

```python
diretorio_pdfs = "C:/Importar Drive/pdf"
```

## 📌 Exemplo de saída

```bash
Informações sobre lotes:
Lote 12345: 10 página(s)
Lote 67890: 5 página(s)
```

## 📖 Objetivo

Automatizar a leitura e organização de documentos PDF por lote.
