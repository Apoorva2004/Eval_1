#!/usr/bin/env python
# coding: utf-8

# In[20]:


def stuinfo():
    name=input("Enter name of student: ")
    std=int(input("Enter class: "))
    height=int(input("Enter height(in cm): "))
    weight=int(input("Enter weight(in kg): "))
    sport=input("Enter interested sport: ")
    student={"NAME":name,"CLASS":std,"HEIGHT":height,"WEIGHT":weight,"SPORT":sport}
    print(student)
def diet_chart():
    stw=int(input("Enter weight(in kg): "))
    sth=int(input("Enter height(in cm): "))
    cal=int(input("Enter calorie intake: "))
    chart={"WEIGHT":stw,"HEIGHT":sth,"Calorie_intake":cal}
    print(chart)
    if chart["Calorie_intake"]<100:
       print("RED")
    elif((chart["Calorie_intake"]>100) & (chart["Calorie_intake"]<200)):
       print("ORANGE")
    else:
       print("GREEN")
    #for i in chart.keys():
     #   if chart[i]<100:
      #      print("RED")
       # elif((chart[i]>100) & (chart[i]<150)):   
        #    print("ORANGE")
        #elif((chart[i]>150) & (chart[i]<200)):
         #   print("GREEN")
            
stuinfo()
diet_chart()


# In[ ]:





# In[ ]:




