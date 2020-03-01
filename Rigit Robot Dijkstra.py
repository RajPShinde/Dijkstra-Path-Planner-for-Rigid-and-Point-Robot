import numpy as np
import cv2 as cv2
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def take_input():
    print("Enter a start node co-ordinates x,y (e.g 5 4)")
    C= [int(i) for i in input().split()]
    return C

def draw_map():
    fig1, ax = plt.subplots()
    patches = []
    obstacle1 = mpatches.Polygon([[25,185],[75,185],[100,150],[75,120],[50,150],[20,120]], True)
    obstacle2 = mpatches.Polygon([[225,40],[250,25],[225,10],[200,25]], True)
    obstacle3 = mpatches.Polygon([[30.05,76.16],[100,38.66],[95,30],[25.05,67.5]], True)
    obstacle4 = mpatches.Circle((225, 150), 25)
    obstacle5= mpatches.Ellipse((150,100),80,40)
    patches.append(obstacle1)
    patches.append(obstacle2)
    patches.append(obstacle3)
    patches.append(obstacle4)
    patches.append(obstacle5)
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array([0,0,0,0,0]))
    ax.add_collection(p)
    plt.axis([0, 300, 0, 200])
    fig1.show()

def draw_trial_map():
    fig2, ax2 = plt.subplots()
    patches = []
    obstacle1 = mpatches.Polygon([[90,60],[110,60],[110,40],[90,40]], True)
    obstacle2 = mpatches.Circle((160, 50), 15)
    patches.append(obstacle1)
    patches.append(obstacle2)
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array([0,0]))
    ax2.add_collection(p)
    plt.axis([0, 200, 0, 100])
    fig2.show()

def up(x,y):
    y=y-1
    return x,y
 
def down(x,y):
    y=y+1
    return x,y
 
def left(x,y):
    x=x-1
    return x,y
  
def right(x,y):
    x=x+1
    return x,y
  
def up_left(x,y):
    x=x-1
    y=y-1
    return x,y
  
def up_right(x,y):
    x=x+1
    y=y-1
    return x,y

def down_left(x,y):
    x=x-1
    y=y-1
    return x,y

def down_right(x,y):
    x=x+1
    y=y-1
    return x,y

def check_if_inlier(x,y):
    if cv2.pointPolygonTest(np.float32([[30.05,76.16],[100,38.66],[95,30],[25.05,67.5]]),(x,y),False)>-1: return 1
    if ((x-150)/40)**2+((y-100)/20)**2<=1: return 1
    if cv2.pointPolygonTest(np.float32([[25,185],[75,185],[100,150],[75,120],[50,150],[20,120]]),(x,y),False)>-1: return 1
    if cv2.pointPolygonTest(np.float32([[225,40],[250,25],[225,10],[200,25]]),(x,y),False)>-1: return 1 
    if (x-225)**2+(y-150)**2<=25: return 1 
    return 0
    

def dijkstra(N):
    Parent=[]

def find path(path):
    
    

    
draw_map()
draw_trial_map()
p=check_if_inlier(225,13)
print(p)