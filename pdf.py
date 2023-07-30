    from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def extraer_titulo_pdf(ruta_pdf):
    try:
        with open(ruta_pdf, 'rb') as archivo_pdf:
            parser = PDFParser(archivo_pdf)
            documento = PDFDocument(parser)
            if 'Title' in documento.info:
                titulo = documento.info['Title']
                return titulo
            else:
                return None
    except Exception as e:
        print("Error al extraer el título del PDF:", e)
        return None

ruta_pdf = 'ruta/al/libro.pdf'
titulo = extraer_titulo_pdf(ruta_pdf)
if titulo:
    nuevo_nombre = titulo + ".pdf"
    print("Título del libro:", titulo)
    print("Nuevo nombre de archivo:", nuevo_nombre)
    # Renombrar el archivo con el nuevo nombre
    # os.rename(ruta_pdf, nuevo_nombre)
else:
    print("No se encontró el título del libro en el PDF.")


# Configuración de los argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Directory Path')
parser.add_argument('-p', '--path', type=str, help='Directory Path')
args = parser.parse_args()

# Obtener la ruta del directorio proporcionada como argumento
path = args.path