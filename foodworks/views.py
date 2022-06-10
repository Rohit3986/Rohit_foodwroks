import email
from django.shortcuts import render,redirect,HttpResponse
from foodworks.models import foodrecord,orderrecord
from datetime import datetime
# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST.get("subject") #currently not adding any restriction for login 
        password=request.POST.get("pass")
        return redirect("/login")
    return render(request,"index.html")

def login(request):
    context={}


    #the below lists will fetch data from foodrecord 
    coffee_list=list(foodrecord.objects.filter(item_type="Coffee").values("item_type","item_name","item_price","stock_available"))
    pizza_list=foodrecord.objects.filter(item_type="Pizza").values("item_type","item_name","item_price","stock_available")
    momos_list=foodrecord.objects.filter(item_type="Momos").values("item_type","item_name","item_price","stock_available")
    biryani_list=foodrecord.objects.filter(item_type="Biryani").values("item_type","item_name","item_price","stock_available")
    pasta_list=foodrecord.objects.filter(item_type="Pasta").values("item_type","item_name","item_price","stock_available")
    shakes_list=foodrecord.objects.filter(item_type="Shakes").values("item_type","item_name","item_price","stock_available")
    burger_list=foodrecord.objects.filter(item_type="Burger").values("item_type","item_name","item_price","stock_available")
    noodles_list=foodrecord.objects.filter(item_type="Noodles").values("item_type","item_name","item_price","stock_available")
    paneer_list=foodrecord.objects.filter(item_type="Paneer").values("item_type","item_name","item_price","stock_available")
    
    #we will pass this context dictionary in our html pages
    context={"coffee":coffee_list,"pizza":pizza_list,"momos":momos_list,"pasta":pasta_list,"biryani":biryani_list,"paneer":paneer_list,"burger":burger_list,"noodles":noodles_list,"shakes":shakes_list}
    
    
    if request.method=="POST":

        #we are storing all food and drink types in a list
        food_type_list=["coffee","pizza","momos","pasta","biryani","paneer","burger","noodles","shakes"  ]
        
        for i in food_type_list:    #this loop will assign selected food type value by the user in val variables
            val=request.POST.get(i)
            if val is not None:
                break

        #this context will store details of food which will be booked by the user
        context={"food":context[val],"food_type":val}
        return render(request,"order_booking.html",context)
    return render(request,"login.html",context)

def order_history(request):
    context={}
    if request.method=="POST":
        delete_order=request.POST.get("delete")
        update_order=request.POST.get("update")

        #this if statement will work when user will use update option
        if update_order is not None:
            orderrecord.objects.filter(order_id=update_order).delete()
            return redirect("/login")

        #if user selects delete option then below code will work
        orderrecord.objects.filter(order_id=delete_order).delete()
        return redirect("/my_orders")
    food_ordered=orderrecord.objects.all().values("item_name","ordered_qty","item_price","order_id","total_payable")
    context={"order_details":food_ordered}
    return render(request,"myorders.html",context)

def order_booking(request):
    if request.method=="POST":
        ordered_qty=request.POST.get("qty")
        order=request.POST.get("order")
        ammout_per_qty=foodrecord.objects.filter(item_name=order).values("item_price")[0]['item_price']
        ammout_payable=int(ordered_qty)*int(ammout_per_qty)
        date_val=datetime.now().strftime("%H%M%S")
        order_id=order[0:3].upper()+str(ammout_payable)+date_val
        
        #we will store this details in our order_record table
        food_ordered=orderrecord(item_name=order,ordered_qty=ordered_qty,item_price=ammout_per_qty,order_id=order_id,total_payable=ammout_payable)
        food_ordered.save()
        return redirect("/login")
    return render(request,"order_booking.html")

def logout(request):
    return render(request,"logout.html")


