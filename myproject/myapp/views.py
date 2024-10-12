from django.shortcuts import render, redirect , get_object_or_404
from .forms import Header_topForm, Header_middleForm, FooterForm
from .models import Header_top, Header_middle, Footer
from django.utils.dateparse import parse_date

def main(request):
    return render(request, 'main.html')  

def all_info(request):
    header_tops = Header_top.objects.all()
    header_middles = Header_middle.objects.all()
    footers = Footer.objects.all()

    header_data = zip(header_tops, header_middles, footers)

    return render(request, 'all_info.html', {
        'header_data': header_data,
    })

def create_all_info(request):
    if request.method == 'POST':
        header_top_form = Header_topForm(request.POST)
        header_middle_form = Header_middleForm(request.POST)
        footer_form = FooterForm(request.POST)

        if header_top_form.is_valid() and header_middle_form.is_valid() and footer_form.is_valid():
            header_top_form.save()
            header_middle_form.save()
            footer_form.save()
            return redirect('all_info')  

    else:
        header_top_form = Header_topForm()
        header_middle_form = Header_middleForm()
        footer_form = FooterForm()

    return render(request, 'create_all_info.html', {
        'header_top_form': header_top_form,
        'header_middle_form': header_middle_form,
        'footer_form': footer_form
    })


def edit_all_info(request, id):
    header_top = get_object_or_404(Header_top, id=id)  
    header_middle = get_object_or_404(Header_middle, id=id)  
    footer = get_object_or_404(Footer, id=id)  

    if request.method == 'POST':
        header_top_form = Header_topForm(request.POST, instance=header_top)
        header_middle_form = Header_middleForm(request.POST, instance=header_middle)
        footer_form = FooterForm(request.POST, instance=footer)

        if header_top_form.is_valid() and header_middle_form.is_valid() and footer_form.is_valid():
            header_top_form.save()
            header_middle_form.save()
            footer_form.save()
            return redirect('all_info')  
    else:
        header_top_form = Header_topForm(instance=header_top)
        header_middle_form = Header_middleForm(instance=header_middle)
        footer_form = FooterForm(instance=footer)

    context = {
        'header_top_form': header_top_form,
        'header_middle_form': header_middle_form,
        'footer_form': footer_form,
    }

    return render(request, 'edit_all_info.html', context)


def delete_info(request, id):
    header_top = get_object_or_404(Header_top, id=id)
    header_middle = get_object_or_404(Header_middle, id=id)
    footer = get_object_or_404(Footer, id=id)

    if request.method == 'POST':
        header_top.delete()
        header_middle.delete()
        footer.delete()
        return redirect('all_info')  
    else:
        context = {
            'header_top': header_top,
            'header_middle': header_middle,
            'footer': footer,
        }
        return render(request, 'delete_info.html', context)

