from tablib import Dataset

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fourth_umpire.predictions.pred import *
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *

#add for report
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
#

import pandas_highcharts.core

# Create your views here.
def prematch(request):
    if request.method == 'POST':
        title_form = PreMatch(request.POST, request.FILES)
        if title_form.is_valid():
            carrera = title_form.cleaned_data['carrera']
            ciclo = title_form.cleaned_data['ciclo']
            sede = title_form.cleaned_data['sede']
            document = request.FILES['document']
            fs = FileSystemStorage()
            filename = fs.save(document.name, document)
            uploaded_file_url = fs.url(filename)
            document = "documents/"+str(title_form.cleaned_data['document'])
            [probab, cod_est, sexo] = pre_match_predict(document)
            winner = get_carrera(carrera)
            cod_est = pd.DataFrame(cod_est)
            #cod_est_html = cod_est.to_html()
            chart = pandas_highcharts.core.serialize(sexo, render_to='my-chart',
                                                    output_type='json',
                                                    kind = "bar",
                                                    x ="sex",
                                                    title="Distribucion general por sexo"
                                                    )
            return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form,"winner":winner,"probab":probab,"chart":chart})

    else:
        title_form = PreMatch()

    return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form})

#add for report
class ReportePersonasPDF(View):
    def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            archivo_imagen = settings.STATIC_ROOT+'/images/logo_eon.png'
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
            pdf.drawImage(archivo_imagen, 40, 740, 120, 90,preserveAspectRatio=True)
            #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
            pdf.setFont("Helvetica", 16)
            #Dibujamos una cadena en la ubicación X,Y especificada
            #pdf.drawString(230, 790, u"EON CORP")
            #pdf.setFont("Helvetica", 14)
            pdf.drawString(200, 770, u"DESERCIÓN POR PERIODO")
            pdf.line(200,765,415,765)

            pdf.setTitle("Reporte deserción")

    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=Reporte-decersion.pdf'
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            y = 600
            self.tabla(pdf, y)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

    def tabla(self,pdf,y):
            #Creamos una tupla de encabezados para neustra tabla
            encabezados = ('No.', 'Nombre', 'Apellido', 'Nota 1', 'Nota 2')
            #Creamos una lista de tuplas que van a contener a las personas

            per1 = [1, 'Carolina', 'Jaramillo', '3','7.5']
            per2 = [2, 'Lorena', 'Casas', '2','7.5']
            per3 = [3, 'Carlos', 'Pavon', '3.8','5.8']
            detalles = [per1, per2, per3]

            # detalles = [(persona.dni, persona.nombre, persona.apellido_paterno, persona.apellido_materno) for persona in Persona.objects.all()]
            #Establecemos el tamaño de cada una de las columnas de la tabla
            detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 2 * cm, 2 * cm])
            #Aplicamos estilos a las celdas de la tabla
            detalle_orden.setStyle(TableStyle(
            [
                    #La primera fila(encabezados) va a estar centrada
                    ('ALIGN',(0,0),(3,0),'CENTER'),
                    #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    #El tamaño de las letras de cada una de las celdas será de 10
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ]
            ))
            #Establecemos el tamaño de la hoja que ocupará la tabla
            detalle_orden.wrapOn(pdf, 800, 600)
            #Definimos la coordenada donde se dibujará la tabla
            detalle_orden.drawOn(pdf, 60,y)


#
