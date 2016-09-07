#!/usr/env python

def quick_sort(array, start, end):
    if(start < end):
        i = start
        j = end
        base_value = array[i]
        while i < j :
            while (i < j and array[j] >= base_value):
                j = j - 1
            if(i < j):
                array[i] = array[j]
                i = i + 1
                print '\t-->%s, %d, %d' %(array,i ,j)
            while(i < j and array[i] < base_value):
                i = i + 1
            if(i < j):
                array[j] = array[i]
                j = j -1
                print '\t<--%s, %d, %d' %(array,i ,j)
        array[i] = base_value
        print '%s, %d, %d' %(array,i ,j)
        quick_sort(array, start, i -1)
        quick_sort(array, i + 1, end)

if __name__ == '__main__':
    array = [100, 9, 55, 18, 29, 332, 441, 0, 8, 6]
    print array
    print 'above origion'
    quick_sort(array, 0, len(array) - 1)