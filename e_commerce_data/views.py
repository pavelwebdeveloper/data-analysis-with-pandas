from django.shortcuts import render
import pandas as pd

# Create your views here.
def e_commerce_data(request):
    df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

    table = df.to_html(classes='table table-striped', index=False)
    return render(request, 'ecommerce_data.html', {
        'table': table
    })
