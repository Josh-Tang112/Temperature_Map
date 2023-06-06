from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
import os
from socket import gethostbyname
import folium
from . import temp_data_fetcher as tdf
import base64

def get_server_url(request):
    ip = gethostbyname(request.META['SERVER_NAME'])
    port = request.META['SERVER_PORT']
    return f"{ip}:{port}"

def TempView(request, coord):
    # get the coordinate
    coord = coord.split(",")
    lat = float(coord[0])
    lng = float(coord[1])
    res = tdf.get_fig(tdf.get_station_name(lat,lng))

    m = folium.Map(location = (lat, lng), zoom_start = 7, tiles = "OpenStreetMap")
    html = '<a href="/temperature/${lat},${lng}">'+get_server_url(request)+'/temperature/${lat},${lng}</a>'
    folium.ClickForMarker(html).add_to(m)
    if res == 1:        # put the image into iframe
        encoded = base64.b64encode(open("./temperature/lol.jpg", 'rb').read())
        html = '<img src="data:image/jgg;base64,{}">'.format
        iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=950, height=520)

    else:
        html = "<b>The nearest station does not have any data on temperature</b>"
        iframe = folium.IFrame(html, width=300, height=100)

    popup = folium.Popup(iframe, max_width=1050)
    icon=folium.Icon(color = 'blue',icon='temperature-quarter',prefix='fa')
    folium.Marker(location=coord, popup = popup, icon=icon).add_to(m)
    m.save("./temperature/templates/temperature/temp_map.html")

    return render(request, "./temperature/temp_map.html")


def MapView(request):
    url = f"{get_server_url(request)}/temperature"
    html = '<a href="/temperature/${lat},${lng}">' + url + '/${lat},${lng}</a>'
    m = folium.Map(location = (37.0902, -95.7129), zoom_start = 5, tiles = "OpenStreetMap")
    folium.ClickForMarker(html).add_to(m)
    m.save("./temperature/templates/temperature/map.html")
    return render(request,"./temperature/map.html")