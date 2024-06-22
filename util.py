import numpy as np

def data_stats(data):

    if isinstance(data, np.ndarray):
        nparray_stats(data)
        return 
    
    print(f"Data type: {type(data)}, len: {len(data)}")

def nparray_stats(arr):
    print(f"ndarray len: {len(arr)}")
    print(f"First element: {arr[0][1]}\n{arr[0][0]}")
    print(f"W x H : {len(arr[0][0][0])} x {len(arr[0][0])}")

def threeDimToFloat(arr):
    return [[[float(x) for x in row]for row in img] for img in arr]

def convertLabels(arr):
    res = []
    for x in arr:
        vec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
        if x == "0":
            vec[0] = 1.0

        elif x == "1":
            vec[1] = 1.0

        elif x == "2":
            vec[2] = 1.0

        elif x == "3":
            vec[3] = 1.0
            
        elif x == "4":
            vec[4] = 1.0

        elif x == "5":
            vec[5] = 1.0

        elif x == "6":
            vec[6] = 1.0

        elif x == "7":
            vec[7] = 1.0

        elif x == "8":
            vec[8] = 1.0

        elif x == "9":
            vec[9] = 1.0
        
        elif x == "+":
            vec[10] = 1.0

        elif x == "-":
            vec[11] = 1.0

        elif x == "_":
            vec[12] = 1.0

        elif x == "%":
            vec[13] = 1.0

        elif x == "[":
            vec[14] = 1.0

        elif x == "]":
            vec[15] = 1.0
        
        res.append(vec)

    return res

