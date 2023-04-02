from django.shortcuts import render, redirect
from .forms import expenseForm
from .models import Expense
from django.db.models import Sum
import datetime
# Create your views here.


def indexView(request):
    if request.method == 'POST':
        expense = expenseForm(request.POST)
        if expense.is_valid():
            instance = expense.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('index')

    # expenses = Expense.objects.all()
    expenses = Expense.objects.filter(staff=request.user)

    total_expense = expenses.aggregate(Sum('amount'))

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year, staff=request.user)
    yearly_sum = data.aggregate(Sum('amount'))

    today1 = datetime.date.today() - datetime.timedelta(days=1)
    data = Expense.objects.filter(date__gt=today1, staff=request.user)
    today_sum = data.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data1 = Expense.objects.filter(date__gt=last_month, staff=request.user)
    monthly_sum = data1.aggregate(Sum('amount'))
    print(monthly_sum)

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data2 = Expense.objects.filter(date__gt=last_week, staff=request.user)
    weekly_sum = data2.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter(staff=request.user).values(
        'date').order_by('date').annotate(sum=Sum('amount'))

    category_sums = Expense.objects.filter(staff=request.user).values(
        'category').order_by('category').annotate(sum=Sum('amount'))
    print(category_sums)

    expense_form = expenseForm()
    return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses, 'total_expense': total_expense, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum, 'weekly_sum': weekly_sum, 'daily_sums': daily_sums, 'today_sum': today_sum, 'category_sums': category_sums})


def editView(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = expenseForm(instance=expense)
    if request.method == 'POST':
        expenses = Expense.objects.get(id=id)
        form = expenseForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'myapp/edit.html', {'expense_form': expense_form})


def deleteView(request, id):
    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')


def loginView(request):
    return render(request, 'myapp/login.html')


def registerView(request):
    return render(request, 'myapp/register.html')
