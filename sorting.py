def bubble_sort(draw_data, ascending=True, draw_func=None):
    data = draw_data.data
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            num1 = data[j]
            num2 = data[j + 1]
            
            if num1 > num2 and ascending or (num1 < num2 and not ascending):
                data[j], data[j+1] =  data[j + 1], data[j]
                if draw_func != None:
                    draw_func(draw_data, {j: draw_data.GREEN, j+1: draw_data.RED}, True)
                yield True
                
    return data


def insertion_sort(draw_data, ascending=True, draw_func=None):
    data = draw_data.data
    
    for i in range(1, len(data)):
        curr = data[i]
        
        while True:
            ascending_sort = i > 0 and data[i-1] > curr and ascending
            descending_sort = i > 0 and data[i-1] < curr and not ascending
            
            if not ascending_sort and not descending_sort:
                break
            
            data[i] = data[i-1]
            i = i-1
            data[i] = curr
            draw_func(draw_data, {i-1: draw_data.GREEN, i: draw_data.RED}, True)
            yield True
    
    return data
            



    