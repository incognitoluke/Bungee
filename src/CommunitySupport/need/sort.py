from .models import Order
from .form import OrderForm

def sort_orders(queryset):
    new_sorted = {}

    i = 0 
    for item in queryset:
        i += 1
        urgency_weight = (int(item.urgency) * 0.7)
        position_weight = (len(queryset) - (i))*0.3 
        name = item.name
        new_sorted[name] = urgency_weight + position_weight
    pointer = 0
    
    unique_id = 0
    for item in new_sorted:
        if item == queryset[pointer].name:
            Order.objects.filter(name=item).update(alias=(str(unique_id) + str(unique_id) + str(queryset[pointer].id)))
            Order.objects.filter(name=item).update(score=new_sorted[item])
            pointer += 1
        else:
            pointer += 1
            continue
    
    return new_sorted

queryset = Order.objects.all()
sort_orders(queryset)