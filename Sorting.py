import time
from numpy.random import randint
import matplotlib.pyplot as plt
def mergesort(array):
    if(len(array))>1:
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1

def printlist(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()

if __name__ == '__main__' :
    array=[6,5,12,10,9,1]
    mergesort(array)
print(array)

def partition(array,low,high):
    pivot=array[high]
    i=low-1

    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
data=[8,7,2,1,0,9,6]
print("Unsorted Array")
print(data)

size=len(data)
quicksort(data,0,size-1)

print("Sorted Array in Ascending Order:")
print(data)

def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]< array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
data=[-2,45,0,11,-9]
size=len(data)
selectionsort(data,size)
print("Sorted Array in Ascending Order:")
print(data)

def readinput():
    a=[]
    n=int(input("Enter the no.of TV channels:"))
    print("Enter the no.of viewers")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a

elements=list()
times=list()
global labeldata
print("1.Mergesort 2.Quick Sort 3.Selection Sort")
ch=int(input("Enter the choice"))
if(ch==1):
    array=readinput()
    mergesort(array)
    labeldata="MergeSort"
    print("Sorted Array is:")
    print(array)
elif(ch==2):
    array=readinput()
    size=len(array)
    labeldata="QuickSort"
    quicksort(array,0,size-1)
    print("Sorted Array is:")
    print(array)

if(ch==3):
    array=readinput()
    size=len(array)
    labeldata="SelectionSort"
    selectionsort(array,size)
    print("Sorted Array is:")
    print(array)
print("******Running Time Analysis******")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    print(i)
    start=time.time()

    if ch==1:
        mergesort(array)
    elif ch==2:
        size=len(array)
        quicksort(array,0,size-1)
    else:
        size=(len(array))
        selectionsort(array,size)
    end=time.time()
    print("Sorted list is ",array)
    print(len(array),"Elements Sorted by",labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)

plt.xlabel('List length')
plt.ylabel('Timke complexity')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()