from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Welcome')



products=[
    {'id': 1, 'title': 'Mobile', 'price':333,'image':'mobile.png','description':'Apple Iphone 5s 32gb Silver With Signs Of Wear - Iphone 5 S White'},
    {'id': 2, 'title': 'labtop', 'price':222,'image':'lab.png','description':'Star Labtop Mk Iii Linux Laptop Computer Open Left - Side Angle Laptop'},
    {'id': 3, 'title': 'watch', 'price':100,'image':'watch.png','description':'Bangalore Watch Company Mens Watches'},
    {'id': 4, 'title': 'Smart TV', 'price':500,'image':'tv2.png','description':'Ks Suhd K Smart - Tv 49 Pollici Samsung'},
     {'id': 5, 'title': 'storage', 'price':20,'image':'storage.png','description':'Alpha 5000 E Mount Camera And 16 50 Mm Zoom Lens With - Micro Sd'},
    {'id': 6, 'title': 'camera', 'price':250,'image':'camera.png','description':'Cameras & Optics,camera Accessory,point And Shoot Camera,camera,digital - Flir T840'},
    {'id': 7, 'title': 'Earphone', 'price':40,'image':'era.png','description':'Original Earphones For Nubia Mobile Phone - Headphones'},
    {'id': 8, 'title': 'Battery', 'price':70,'image':'charge.png','description':'Firefly Replacement Battery - Firefly 2 Battery'},
]

def product(request):
    return HttpResponse(products)


def filter_products(request,id):
    id=int(id)
    f_products=filter(lambda prod:prod['id']==id,products)
    f_products=list(f_products) 
    # print(f_products[0])

    if f_products:
        return HttpResponse(f_products[0])
    
    return HttpResponse('no products found')


# render a list of products in html format

def product_list(request):
    return render(request,'Amazon/store.html',context={'products':products})




# render product details
def product_detail(request, id):
    # retrieve the product details based on the product id
    id = int(id)
    product_detail = None

    for product in products:
        if product['id'] == id:
            product_detail = product
            break

    if product_detail:
        return render(request, 'Amazon/product_detail.html',context={'product_detail': product_detail})
    else:
        return HttpResponse('Product not found')