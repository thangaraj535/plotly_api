from django.shortcuts import render
import plotly.express as px
# Create your views here.
import json
from django.http import JsonResponse


# def ploting_plotly(request):
#     df = px.data.tips()
#     fig = px.bar(df, x='day', y="total_bill")
#     graph = fig.to_html(full_html=False, default_height=500, default_width=700, config= {'displaylogo': False})
#     context = {'graph': graph}
#     response = render(request, 'chart.html', context)
#     return response
#     # chart_data = fig.to_json()
#     # return render(request,'chart.html',{fig})


import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder

def ploting_plotly(request):
    df = px.data.tips()
    fig = px.bar(df, x='day', y="total_bill")
    chart_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    return JsonResponse(chart_json, safe=False)