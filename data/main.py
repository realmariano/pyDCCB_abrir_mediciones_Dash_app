# Run this app with `python app.py` and
# visit http://127.0.0.1:8888/ in your web browser.


## to be improved
""" ======================================================================

I removed the code below and kept a long protocol with lots of sheets, because it does not copy the charts, so its easiert to just fill and then remove the ones not used create as much sheets as needed
2 - 
~~~
for nn in range(len(qlist)):
  source = xl['(0)']
  target = xl.copy_worksheet(source)
~~~

3- En el archivo de protocolo hay que modificar la inclusión del nombre de archivo de mea, set y config

4- Incluir un método para que tome automáticamente si la medición se hace en aire o en el baño y corrija el valor de la resistencia (probablemente dos protocolos son necesarios para esto)

5- Modificar celda P10 del protocolo a: 
~~~
=IFS(NUMBERVALUE(C23)<30,30,NUMBERVALUE(C23)<100,300,NUMBERVALUE(C23)<300,3000) 
~~~

De forma tal que reconozca la relación del RE automáticamente.

6- El programa no está generando correctamente la salida
"""


# packages
# =====================================================
import base64
import datetime
import io
import os
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table


# Dash, front end program
# =======================================================

UPLOAD_DIRECTORY = '/project/app_uploaded_files'
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

    
# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)
app = dash.Dash(__name__, server=server,
    external_stylesheets=[dbc.themes.SPACELAB]
    # available themes: CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI
    )

@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop o ', 
            html.A('\n click aquí',
            style= {'color': 'DodgerBlue','font-size': '20px'}
            )
        ], style= {'font-size': '20px'}),
        style={
            'width': '30%',
            'height': '90px',
            'lineHeight': '60px',
            'borderWidth': '3px',
            'borderStyle': 'solid',
            'borderColor': 'LightSeaGreen', 
            #'backgroundColor': '#eee',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '40px'
        },
        # Allow multiple files to be uploaded
        multiple= True
    ),
    html.Div(
        id='output-data-files',
        style={
            #'textAlign': 'center',
            'margin': '60px',
            'font-size': '20px'
        }
    ),
])


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))

def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)

@app.callback(
    Output(component_id= 'output-data-files', component_property= 'children'),
    [
        Input(component_id="upload-data", component_property= "filename"), 
        Input(component_id="upload-data", component_property= "contents")
    ],
    #State(component_id= 'upload-data', component_property= 'filename'),
    #State(component_id= 'upload-data', component_property= 'last_modified')
)

def update_output(uploaded_filenames, uploaded_file_contents):
    """ Save uploaded files and regenerate the file list """
    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for filename, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(filename, data)
            # correr acá mi programa sobre el loop:
            # processed_file = mi_programa(data,protocol_file_language= ENG, n_meas_stat= 20)
            # save_file(uploaded_filenames, processed_file)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
