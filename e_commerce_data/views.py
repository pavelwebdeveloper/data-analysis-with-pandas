from django.shortcuts import render
import pandas as pd
import io

pd.set_option("display.precision", 0)

df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

# Create your views here.
def e_commerce_data(request):

    df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

    columnSort = request.GET.get("columnSort", "")
    ascending = request.GET.get("ascending", "")
    columnFilter = request.GET.getlist("columnFilter", "")

    if (columnSort or ascending or columnFilter):

        ascending = True if ascending == "True" else False

        if(columnSort):
            df = df.sort_values(by=columnSort, ascending=ascending)

        if(columnFilter):
            df = df[columnFilter]



    table = df.to_html(classes='table table-striped', index=False)

    return render(request, 'ecommerce_data.html', {
        'table': table
    })

def e_commerce_data_describe(request):

    df_description = df.describe()

    return render(request, 'ecommerce_data_description.html', {
        'df_description': df_description
    })

def e_commerce_data_info(request):

    buffer = io.StringIO()
    df.info(buf=buffer)
    info_output = buffer.getvalue()

    #table = df.to_html(classes='table table-striped', index=False)
    return render(request, 'ecommerce_data_info.html', {
        'data_info': info_output
    })