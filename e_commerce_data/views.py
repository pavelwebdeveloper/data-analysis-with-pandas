from django.shortcuts import render
import pandas as pd
import plotly.express as px
import io

pd.set_option("display.precision", 0)

df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

# Create your views here.
def e_commerce_data(request):

    df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

    columnSort = request.GET.get("columnSort", "")
    ascending = request.GET.get("ascending", "")
    #columnFilter = request.GET.getlist("columnFilter", "")

    orderID = request.GET.get("Order ID", "")
    orderDate = request.GET.get("Order Date", "")
    customerName = request.GET.get("Customer Name", "")
    region = request.GET.get("Region", "")
    city = request.GET.get("City", "")
    category = request.GET.get("Category", "")
    subCategory = request.GET.get("Sub-Category", "")
    productName = request.GET.get("Product Name", "")
    quantity = request.GET.get("Quantity", "")
    unitPrice = request.GET.get("Unit Price", "")
    discount = request.GET.get("Discount", "")
    sales = request.GET.get("Sales", "")
    profit = request.GET.get("Profit", "")
    paymentMode = request.GET.get("Payment Mode", "")
    columnFilter = []

    if (orderID or orderDate or customerName or region or city or category or subCategory or productName or quantity or unitPrice or discount or sales or profit or paymentMode):
        if orderID:
           columnFilter.append(orderID) 
        if orderDate:
            columnFilter.append(orderDate)
        if customerName:
            columnFilter.append(customerName)
        if region:
            columnFilter.append(region)
        if city:
            columnFilter.append(city)
        if category:
            columnFilter.append(category)
        if subCategory:
            columnFilter.append(subCategory)
        if productName:
            columnFilter.append(productName)
        if quantity:
            columnFilter.append(quantity)
        if unitPrice:
            columnFilter.append(unitPrice)
        if discount:
            columnFilter.append(discount)
        if sales:
            columnFilter.append(sales)
        if profit:
            columnFilter.append(profit)
        if paymentMode:
            columnFilter.append(paymentMode)


    if (columnSort or ascending or (len(columnFilter) > 0)):

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


def plots(request):
    salesByProduct = request.GET.get("salesByProduct", "")

    grouped_df = df.groupby("Product Name")["Sales"].sum().reset_index()
    grouped_df = grouped_df.sort_values(by="Sales", ascending=False)

    graph = px.bar(
        grouped_df,
        y="Product Name",
        x="Sales",
        color="Product Name",
        title="Total Sales by Product",
        template="plotly",
        orientation="h",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    graph.update_traces(
        marker=dict(opacity=1, line=dict(width=1, color="black"))
    )

    graph.update_layout(
        margin=dict(l=200, r=40, t=80, b=40),
        autosize=True,
        height=20 * len(grouped_df)
    )

    graph_html = graph.to_html(full_html=False)

    return render(request, 'plots.html', {
        'plot': graph_html
    })
    

