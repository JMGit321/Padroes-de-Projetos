from random import randint
def time(func):
        import time
        def wrap(*a,**b):
            t1 = time.time()
            func(*a,**b)
            t2 = time.time()
            print("Tempo de duracao da execucao",t2-t1)
        return wrap

class MeuConjunto(object):

        def __init__(self):
            self.valor = []


class HeapClass(object):
        
        def sort(self,arg):
            if(type(arg) is not MeuConjunto):
                print("Coloque somente argumentos da classe MeuConjunto")
            else:
                @time
                def heapsort(alist):
                    build_max_heap(alist)
                    for i in range(len(alist) - 1, 0, -1):
                        alist[0], alist[i] = alist[i], alist[0]
                        max_heapify(alist, index=0, size=i)
                def parent(i):
                    return (i - 1)//2
 
                def left(i):
                    return 2*i + 1
 
                def right(i):
                    return 2*i + 2
 
            def build_max_heap(alist):
                    length = len(alist)
                    start = parent(length - 1)
                    while start >= 0:
                        max_heapify(alist, index=start, size=length)
                        start = start - 1
 
            def max_heapify(alist, index, size):
                    l = left(index)
                    r = right(index)
                    if (l < size and alist[l] > alist[index]):
                        largest = l
                    else:
                        largest = index
                    if (r < size and alist[r] > alist[largest]):
                        largest = r
                    if (largest != index):
                        alist[largest], alist[index] = alist[index], alist[largest]
                        max_heapify(alist, largest, size)
            
            heapsort(arg.valor)
            return arg









class MergeClass(object):
        

        def sort(self,arg):
            if(type(arg) is not MeuConjunto):
                print("Coloque somente argumentos da classe MeuConjunto")
            else:
                 @time
                 def mergeSort(alist):
    
                    if len(alist)>1:
                        mid = len(alist)//2
                        lefthalf = alist[:mid]
                        righthalf = alist[mid:]

                        mergeSort(lefthalf)
                        mergeSort(righthalf)

                        i=0
                        j=0
                        k=0
                        while i < len(lefthalf) and j < len(righthalf):
                             if lefthalf[i] < righthalf[j]:
                                alist[k]=lefthalf[i]
                                i=i+1
                             else:
                                alist[k]=righthalf[j]
                                j=j+1
                             k=k+1

                        while i < len(lefthalf):
                            alist[k]=lefthalf[i]
                            i=i+1
                            k=k+1

                        while j < len(righthalf):
                            alist[k]=righthalf[j]
                            j=j+1
                            k=k+1
            mergeSort(arg.valor)
            return arg





class QuickClass(object):
        

        def sort(self,arg):
            if(type(arg) is not MeuConjunto):
                print("Coloque somente argumentos da classe MeuConjunto")
            else:
                @time
                def quickSort(alist):
                   quickSortHelper(alist,0,len(alist)-1)

                def quickSortHelper(alist,first,last):
                   if first<last:

                       splitpoint = partition(alist,first,last)

                       quickSortHelper(alist,first,splitpoint-1)
                       quickSortHelper(alist,splitpoint+1,last)


                def partition(alist,first,last):
                   pivotvalue = alist[first]

                   leftmark = first+1
                   rightmark = last

                   done = False
                   while not done:

                       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                           leftmark = leftmark + 1

                       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                           rightmark = rightmark -1

                       if rightmark < leftmark:
                           done = True
                       else:
                           temp = alist[leftmark]
                           alist[leftmark] = alist[rightmark]
                           alist[rightmark] = temp

                   temp = alist[first]
                   alist[first] = alist[rightmark]
                   alist[rightmark] = temp


                   return rightmark
            quickSort(arg.valor)
            return arg
            
class ordenador(object):
        def sorte(self,MeuConjunto,ordena):
                ordenado = ordena.sort(MeuConjunto)
                print(type(ordena),ordenado.valor)
a = MeuConjunto()
b = MeuConjunto()
c = MeuConjunto()
for x in range(100):
        a.valor.append(randint(1,100))
        b.valor.append(randint(1,100))
        c.valor.append(randint(1,100))
d = MeuConjunto()
e = MeuConjunto()
f = MeuConjunto()
for x in range(1000):
        d.valor.append(randint(1,1000))
        e.valor.append(randint(1,1000))
        f.valor.append(randint(1,1000))
g = MeuConjunto()
h = MeuConjunto()
i = MeuConjunto()
for x in range(10000):
        g.valor.append(randint(1,1000))
        h.valor.append(randint(1,1000))
        i.valor.append(randint(1,1000))
        
heap = HeapClass()
quick = QuickClass()
merge = MergeClass()
orde = ordenador()
print("100 elementos")
orde.sorte(a,heap)
orde.sorte(b,quick)
orde.sorte(c,merge)
print("1000 elementos")
orde.sorte(d,heap)
orde.sorte(e,quick)
orde.sorte(f,merge)
print("10000 elementos")
orde.sorte(g,heap)
orde.sorte(h,quick)
orde.sorte(i,merge)




