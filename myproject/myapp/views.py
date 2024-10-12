from django.shortcuts import render, redirect, get_object_or_404
from .forms import Header_topForm, Header_middleForm, header_botForm
from .models import header_top, header_middle, header_bot
from django.utils.dateparse import parse_date

def index(request):
    return render(request, 'index.html')  

def all_info(request):
    header_tops = header_top.objects.all()
    header_middles = header_middle.objects.all()
    header_bots = header_bot.objects.all()

    header_data = zip(header_tops, header_middles, header_bots)

    return render(request, 'all_info.html', {
        'header_data': header_data,
    })

def create_all_info(request):
    if request.method == 'POST':
        header_top_form = Header_topForm(request.POST)
        header_middle_form = Header_middleForm(request.POST)
        header_bot_form = header_botForm(request.POST)

        if header_top_form.is_valid() and header_middle_form.is_valid() and header_bot_form.is_valid():
            header_top_form.save()
            header_middle_form.save()
            header_bot_form.save()
            return redirect('all_info')  

    else:
        header_top_form = Header_topForm()
        header_middle_form = Header_middleForm()
        header_bot_form = header_botForm()

    return render(request, 'create_all_info.html', {
        'header_top_form': header_top_form,
        'header_middle_form': header_middle_form,
        'header_bot_form': header_bot_form
    })

def edit_all_info(request, id):
    header_top = get_object_or_404(header_top, id=id)  
    header_middle = get_object_or_404(header_middle, id=id)  
    header_bot = get_object_or_404(header_bot, id=id)  

    if request.method == 'POST':
        header_top_form = Header_topForm(request.POST, instance=header_top)
        header_middle_form = Header_middleForm(request.POST, instance=header_middle)
        header_bot = header_botForm(request.POST, instance=header_bot)

        if header_top_form.is_valid() and header_middle_form.is_valid() and header_bot_form.is_valid():
            header_top_form.save()
            header_middle_form.save()
            header_bot_form.save()
            return redirect('all_info')  
    else:
        header_top_form = Header_topForm(instance=header_top)
        header_middle_form = Header_middleForm(instance=header_middle)
        header_bot_form = header_botForm(instance=header_bot)

    context = {
        'header_top_form': header_top_form,
        'header_middle_form': header_middle_form,
        'header_bot_form': header_bot_form,
    }

    return render(request, 'edit_all_info.html', context)

def delete_info(request, id):
    header_top = get_object_or_404(header_top, id=id)
    header_middle = get_object_or_404(header_middle, id=id)
    header_bot = get_object_or_404(header_bot, id=id)

    if request.method == 'POST':
        header_top.delete()
        header_middle.delete()
        header_bot.delete()
        return redirect('all_info')  
    else:
        context = {
            'header_top': header_top,
            'header_middle': header_middle,
            'header_bot': header_bot,
        }
        return render(request, 'delete_info.html', context)
