from django.shortcuts import render, redirect
from .models import News
from main.models import FooterLink, Contact
from django.core.paginator import Paginator

def news_list(request):

    news = News.objects.all()
    pagination = Paginator(news,10)
    current_page = int(request.GET.get('page', 1))
    page_range = pagination.page_range[current_page - 3 if current_page > 3 else 0 : current_page + 3 ]
    length = len(page_range)

    context ={
        'news_list' : pagination.get_page(current_page),
        'page_range' : page_range,
        'footer_links' : FooterLink.objects.all(),
        'contact' : Contact.objects.last(),
    }

    if length >1:
        context['len'] = length

    return render(request, 'news_list.html', context)


def news_detail(request, slug):

    news = News.objects.filter(slug=slug).last()
    if news:
        context = {
            'news' : news,
            'footer_links' : FooterLink.objects.all(),
            'contact' : Contact.objects.last(),
        }

        return render(request, 'news_detail.html', context)
    else:
        return redirect('home')