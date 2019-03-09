# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:00:43 2019

@author: Javier Soto
Professor Olac fuentes
TAs:
    -Anindita Nath
    -Maliheh Zaragaran
IA
    -Eduardo Lara
Peer Leader
    -Erick Macik
    
the puspose of this lab is to demonstrate my knowldge of implementing Binary 
search trees as provided by Professor Olac Fuentes
"""

import bst
import matplotlib.pyplot as plt

def SearchIte(T,k):
    #will search a binary tree for item k with out using recursion
    temp = T
    while temp is not None:
        if temp.item == k:
            return temp
        elif temp.item > k:
            temp = temp.left
        else:
            temp = temp.right
    return None

def draw_btree(ax,n,x,y,delta_x,delta_y,T):
    if T is not None:
        temp = T
        if n>0:
            # taken from my implementation of draw tree from Lab1 CS2302
            #for ease of ploting create 2 lists of corrisponding x,y values
            x_values = [x-delta_x,x,x+delta_x]
            y_values = [y-delta_y,y,y-delta_y]
        
            circle = plt.Circle((x, y), .5, color = 'white')
            ax.add_artist(circle)
        
            ax.text(x, y, str(temp.item), fontsize=10)
            ax.plot(x_values,y_values)
        
            #draw center then left child then right child 
            draw_btree(ax,n-1,x_values[0],y_values[0],delta_x*.5,delta_y*.5,temp.left)
            draw_btree(ax,n-1,x_values[2],y_values[2],delta_x*.5,delta_y*.5,temp.right)

def ListToTree(L,T):
    #will take a sorted list and create a balanced BST
    if len(L) > 0:
        head = int(len(L)/2)
        T.item = L[head]
        #to create right sub tree
        ListToTree(L[head+1:],T.right)
        #to create left sub tree
        ListToTree(L[:head],T.left)
    return T

def TreeToList(T,L):
    #will take a BST and return a sorted list of the elements in that tree
    if T is not None:
        TreeToList(T.left,L)
        L.append(T.item)
        TreeToList(T.right,L)

def AtDepth(T,index,items):
    #Will take a BST and print the items based on there location in the tree
    if T is not None:
        items[index] = items[index] + str(T.item) + ' '
        AtDepth(T.left,index+1,items)
        AtDepth(T.right,index+1,items)

def Question1(T):
    print('Question 1')
    print('Please see "Figure1"')
    plt.close("all") 
    fig, ax = plt.subplots() 
    
    height = bst.MaxHeight(T)
    draw_btree(ax,height,100,100,10,10,T)
    ax.axis('off')
    plt.show()   
    print()
        
def Question2(T):
    print('Question 2')
    searchee= int(input('Which number Would you like to search for?'))
    temp = SearchIte(T,searchee)
    if temp is not None:
        print('The subtree with item ' + str(searchee) + ' is: ',end = ' ')
        bst.InOrder(temp)
    else:
        print('Item ' + str(searchee) + ' was not found in this tree')
    print()
    
def Question3():
    #sorted list to create a tree from
    B = [1,2,3,4,5,7,8,9,10,12,15,18]
    TempTree = None
    TempTree =ListToTree(B,TempTree)
    print('Question 3')
    print('The new tree from sorted list is: ' , end =' ')
    bst.InOrder(TempTree)
    print()
    Question1(TempTree)

def Question4(T):
    List =[]
    TreeToList(T,List)
    print('Question 4')
    print('The new list created from a tree is: ')
    print(*List, sep = ', ')
    print()
    
def Question5(T):
    print('Question 5')
    items =[]
    Height = bst.MaxHeight(T)
    for i in range(Height):
        items.append('Key at depth ' + str(i) + ': ')
    
    AtDepth(T,0,items)
    for i in range(len(items)):
        print(items[i])
    print()
        


T = None
A = [70, 50, 90, 130, 80, 40, 60,10]
for a in A:
    T = bst.Insert(T,a)
    
Question1(T)
Question2(T)
#Question3()
Question4(T)
Question5(T)

