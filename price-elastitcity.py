#يطلب من المستخدم معلومات عن الكميات والسعر القديم والجديد
p1=float(input("Enter the old price"))
p2=float(input("Enter the new price"))
q1=float(input("Enter the previous required quantity"))
q2=float(input("Enter the new required quantity"))

#معادلة مرونة النقطة في الاقتصاد
result=((q2-q1)/q1)/((p2-p1)/p1)
final_result=abs(result)


#البرنامج يخبر المستخدم عن مدى مرونة المنتج حسب المعطيات
if final_result==0.0:
    print("The product is perfectly inelastic")
elif final_result==1:
   print("The product has unit elasticity")
elif 0<final_result<1:
    print("The product is relatively inelastic")
elif 1<final_result<2:
    print("the product is elastic")
elif 2<final_result<5:
    print("The product is highly elastic")
else:
    print("The product is perfectly elastic")
