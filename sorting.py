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



    