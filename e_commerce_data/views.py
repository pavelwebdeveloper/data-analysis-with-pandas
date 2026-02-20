from django.shortcuts import render
import pandas as pd
import plotly.express as px
import io

pd.set_option("display.precision", 0)

# reading the file with e-commerce data
df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

# views
def e_commerce_data(request):

    # reading the file with e-commerce data inside this function again
    # because of problems accessing the data inside if blocks later
    df = pd.read_csv('./e_commerce_data/Ecommerce_Sales_Data_2024_2025.csv')

    # obtaining input data sent through the form with GET method
    columnSort = request.GET.get("columnSort", "")
    ascending = request.GET.get("ascending", "")
    minValueInput = request.GET.get("minValueInput", "")
    filterByColumn = request.GET.get("filterByColumn", "")
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

    # intiating an array to hold column headings
    columnFilter = []

    # checking if any of the column names have been submitted
    if (orderID or orderDate or customerName or region or city or category or subCategory or productName or quantity or unitPrice or discount or sales or profit or paymentMode):
        # if any of the column names have been submitted then adding them to the columnFilter array
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

    if (filterByColumn and minValueInput):
        df = df[df[filterByColumn] > int(minValueInput)]


    table = df.to_html(classes='table table-striped', index=False)

    return render(request, 'ecommerce_data.html', {
        'table': table
    })

def e_commerce_data_aggregating_statistics(request):

    aggregatingStatistics = request.GET.get("aggregatingStatistics", "")

    df_aggregation_statistics = df.describe()

    if (aggregatingStatistics == ""):
        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics
        })
    elif (aggregatingStatistics == "averageProfitByCategories"):
        averageProfitByCategories = df[["Category", "Profit"]].groupby("Category").mean().reset_index()
        averageProfitByCategories_table = averageProfitByCategories.to_html(classes='table table-striped', index=False)

        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics,
            'aggregating_statistics_table': averageProfitByCategories_table
        })
    elif (aggregatingStatistics == "averageSalesByCategories"):
        averageSalesByCategories = df[["Category", "Sales"]].groupby("Category").mean().reset_index()
        averageSalesByCategories_table = averageSalesByCategories.to_html(classes='table table-striped', index=False)

        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics,
            'aggregating_statistics_table': averageSalesByCategories_table
        })
    elif (aggregatingStatistics == "averageProfitBySub-Categories"):
        averageProfitBySubCategories = df[["Sub-Category", "Profit"]].groupby("Sub-Category").mean().reset_index()
        averageProfitBySubCategories_table = averageProfitBySubCategories.to_html(classes='table table-striped', index=False)

        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics,
            'aggregating_statistics_table': averageProfitBySubCategories_table
        })
    elif (aggregatingStatistics == "averageSalesBySub-Categories"):
        averageSalesBySubCategories = df[["Sub-Category", "Sales"]].groupby("Sub-Category").mean().reset_index()
        averageSalesBySubCategories_table = averageSalesBySubCategories.to_html(classes='table table-striped', index=False)

        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics,
            'aggregating_statistics_table': averageSalesBySubCategories_table
        })
    elif (aggregatingStatistics == "paymentModeCounts"):
        paymentModeCounts = df["Payment Mode"].value_counts().reset_index()
        paymentModeCounts.columns = ["Payment Mode", "Count"]
        paymentModeCounts_table = paymentModeCounts.to_html(classes='table table-striped', index=False)

        return render(request, 'ecommerce_data_aggregating_statistics.html', {
            'df_aggregation_statistics': df_aggregation_statistics,
            'aggregating_statistics_table': paymentModeCounts_table
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
    kindOfPlot = request.GET.get("kindOfPlot", "")

    if (kindOfPlot == ""):
        return render(request, 'plots.html')
    elif (kindOfPlot == "salesByProduct"):
        graph = barPlotBuilder("Product Name", "Sales", "h", "Total Sales by Product")
    elif (kindOfPlot == "salesByCategory"):
        graph = barPlotBuilder("Category", "Sales", "v", "Total Sales by Category")
    elif (kindOfPlot == "salesBySub-Category"):
        graph = barPlotBuilder("Sub-Category", "Sales", "v", "Total Sales by Sub-Category")
    elif (kindOfPlot == "salesByCity"):
        graph = barPlotBuilder("City", "Sales", "v", "Total Sales by City")
    elif (kindOfPlot == "quantityByProduct"):
        graph = barPlotBuilder("Product Name", "Quantity", "h", "Total Sold Quantity by Product")
    elif (kindOfPlot == "quantityByCategory"):
        graph = barPlotBuilder("Category", "Quantity", "v", "Total Sold Quantity by Category")
    elif (kindOfPlot == "quantityBySub-Category"):
        graph = barPlotBuilder("Sub-Category", "Quantity", "v", "Total Sold Quantity by Sub-Category")
    elif (kindOfPlot == "salesByRegion"):
        graph = barPlotBuilder("Region", "Sales", "v", "Total Sales by Region")

    graph_html = graph.to_html(full_html=False)

    return render(request, 'plots.html', {
            'plot': graph_html
        })

def barPlotBuilder(columnName1, columnName2, plotOrientation, plotName):
    grouped_df = df.groupby(columnName1)[columnName2].sum().reset_index()
    grouped_df = grouped_df.sort_values(by=columnName2, ascending=False)

    graph = px.bar(
            grouped_df,
            y = columnName1 if plotOrientation == "h" else columnName2,
            x = columnName2 if plotOrientation == "h" else columnName1,
            color=columnName1,
            title=plotName,
            template="plotly",
            orientation = plotOrientation,
            color_discrete_sequence=px.colors.qualitative.Bold
        )

    graph.update_traces(
            marker=dict(opacity=1, line=dict(width=1, color="black"))
        )

    graph.update_layout(
            margin=dict(l=200, r=40, t=80, b=40),
            autosize=True,
            #height=20 * len(grouped_df)
            height = 20 * len(grouped_df) if columnName1 != "Region" else 100 * len(grouped_df),
        )

    return graph
    
    

