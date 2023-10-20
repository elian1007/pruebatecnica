from flask import Flask, render_template, request, make_response
import mysql.connector
from fpdf import FPDF

app = Flask(__name__)

# Configura la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    # 'password': '',
    'database': 'datosdb'
}
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Registros de la base de datos', 0, 1, 'C')

@app.route('/')
def mostrar_registros():
    # Conecta a la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    # Consulta la base de datos
    cursor.execute("SELECT * FROM informacion")

    # Obtiene los registros
    registros = cursor.fetchall()

    # Cierra la conexión
    cursor.close()
    connection.close()

    return render_template('registros.html', registros=registros)

@app.route('/descargar_pdf')
def descargar_pdf():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM informacion")

    registros = cursor.fetchall()
    cursor.close()
    connection.close()

    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    for registro in registros:
        pdf.multi_cell(0, 10, f"Nombre de Archivo: {registro['nombrearchivo']}")
        pdf.multi_cell(0, 10, f"Cantidad de Líneas: {registro['cantlineas']}")
        pdf.multi_cell(0, 10, f"Cantidad de Palabras: {registro['cantpalabras']}")
        pdf.multi_cell(0, 10, f"Cantidad de Caracteres: {registro['cantcaracteres']}")
        pdf.multi_cell(0, 10, f"Fecha de Registro: {registro['fecharegistro']}")
        pdf.ln(10)

    response = make_response(pdf.output(dest='S').encode('latin1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=registros.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)
