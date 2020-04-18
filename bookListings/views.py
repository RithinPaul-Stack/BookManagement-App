from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from bookListings.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
    }
    return render(request, 'listings/bookListings.html', context)

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
    'listings': paged_listings
    } 
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    print(listing)
    context = {
      'listing': listing
    }
    return render(request, 'listings/listing.html', context)

@login_required
def borrow(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Borrow.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(request, 'You have already borrowed this Book')
            return redirect('/listings/'+listing_id)
    borrow = Borrow(book_title=listing, listing_id=listing_id, name=name, email=email, phone=phone, user_id=user_id )

    borrow.save()
    messages.success(request, 'Your details have been successfully submitted and the book has been lent')
    return redirect('/listings/'+listing_id)
