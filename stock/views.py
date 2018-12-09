from django.views.generic.dates import TodayArchiveView
from django.utils import timezone
from django.views import generic
from django.shortcuts import get_object_or_404, render
from datetime import datetime

from .get_data import top_20_stocks, stock_detail
from .models import Trading_Date, Stock_Info, fifteen_mins_interval


def refresh_data():
    data = top_20_stocks()
    new_top_20_list = Trading_Date.objects.create(trading_date=data.date)
    for stock in data.top_20_detail:
        stock_info = Stock_Info.objects.create(trading_date=new_top_20_list, stock_name=stock.name,
                                               stock_ticker=stock.ticker, closing_price_of_the_day=stock.closing_price)
        for interval in stock.interval_price:
            fifteen_mins_interval.objects.create(
                stock=stock_info, end_of_interval=interval, price_of_the_interval=stock.interval_price[interval])


class StockTodayArchiveView(TodayArchiveView):
    if not Trading_Date.objects.exists():
        refresh_data()
    elif Trading_Date.objects.latest("trading_date").trading_date.date() < timezone.now().date():
        refresh_data()
    queryset = Trading_Date.objects.all()
    date_field = "trading_date"
    allow_future = True


def stock_detail(request, ticker):
    day = Trading_Date.objects.latest(
        "trading_date").stock_info_set.all().get(stock_ticker=ticker)
    stock_interval_price = day.fifteen_mins_interval_set.all().order_by(
        '-end_of_interval')

    return render(request, 'stock/interval_price_for_individual_stock.html', {
        'stock_interval_price': stock_interval_price,
        "stock_ticker": ticker,
    })


class search_ticker():
    pass