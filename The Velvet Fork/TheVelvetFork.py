"""
Author: Davin Strouse
Date: 2/21/2025
Summary: This is a resturant ordering system.
"""

import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage


class binaryOrder(EasyFrame):

    def __init__(self):
        # Dataset
        self.addedMeals = {
    'Steak Meal': 19.99,
    'Burger Meal': 9.99,
    'Salmon Meal': 14.99,
    'Soup Meal': 9.99,
    'Lobster Meal': 24.99,
    'Shrimp Meal': 12.99
}
        
        
        self.window = EasyFrame.__init__(self,title="Velvet Fork Ordering System",width= 1300,height= 700,)
        
        # GUI Panels
        self.logoPanel = self.addPanel(row=0,column=0,rowspan=22,columnspan=1,background="green")
        self.backgroundPanel = self.addPanel(row=0,column=1,rowspan=22,columnspan=3,background="light blue")
        self.foodPanel = self.addPanel(row=1,column=0,rowspan=15,columnspan=1,background="gray")
        self.receiptPanel = self.addPanel(row=1,column=2,rowspan=15,columnspan=1,background="maroon")
        self.descPanel = self.addPanel(row=1,column=1,rowspan=15,columnspan=1,background="pink")

        #Logo Area
        self.logoLabel = self.addLabel(text="",row=0,column=0)
        self.image = PhotoImage(file="Logo.png",height=500,width=500,)
        self.logoLabel["image"] = self.image
        
        


        #Food Panel Buttons and Labels
        self.steakButton = self.foodPanel.addButton(text='Steak Meal',row=0,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=0,column=1,command= lambda:self.addMeal('Steak Meal'))
        self.steakButton.config(font=("Arial",25))
        self.burgerButton = self.foodPanel.addButton(text='Burger Meal',row=1,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=1,column=1,command= lambda:self.addMeal('Burger Meal'))
        self.burgerButton.config(font=("Arial",25))
        self.salmonButton = self.foodPanel.addButton(text='Salmon Meal',row=2,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=2,column=1,command= lambda:self.addMeal('Salmon Meal'))
        self.salmonButton.config(font=("Arial",25))
        self.soupButton = self.foodPanel.addButton(text='Soup Meal',row=3,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=3,column=1,command= lambda:self.addMeal('Soup Meal'))
        self.soupButton.config(font=("Arial",25))
        self.lobsterButton = self.foodPanel.addButton(text='Lobster Meal',row=4,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=4,column=1,command= lambda:self.addMeal('Lobster Meal'))
        self.lobsterButton.config(font=("Arial",25))
        self.shrimpButton = self.foodPanel.addButton(text='Shrimp Meal',row=5,column=0,columnspan=1)
        self.foodPanel.addButton(text='Add Meal',row=5,column=1,command= lambda:self.addMeal("Shrimp Meal"))
        self.shrimpButton.config(font=("Arial",25))
        
        for widget in [self.steakButton,self.burgerButton,self.salmonButton,self.soupButton,self.lobsterButton,self.shrimpButton]:
            widget.grid_configure(padx=0, pady=0)
        
        
        #Receipt Area
        self.receiptPanel.addLabel(text='Order',row=0,column=0,columnspan=2,sticky="NEW")
        self.rowNumber = 1
    
    
    def addMeal(self, mealName):
        #Adds meal to receipt panel
        self.receiptPanel.addLabel(text=[mealName],row=self.rowNumber,column=0,sticky="W")
        price=self.addedMeals[mealName]
        self.receiptPanel.addLabel(text=f"${price:.2f}",row=self.rowNumber,column=1,sticky="E")
        self.rowNumber=self.rowNumber+1
        
        




binaryOrder().mainloop()