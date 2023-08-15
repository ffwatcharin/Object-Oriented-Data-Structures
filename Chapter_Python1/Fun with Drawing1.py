# เขียนภาษา Python เพื่อวาดพีระมิด ซึ่งจะรับ input เป็นขนาดของพีระมิด โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

def draw_pyramid(size):
    size = (size-1)*2+1
    for col in range(size):
        for row in range(size): 
            if col%2 == 0: 
                if row%2!=0 and col>row:
                    print('.', end='')    
                else:
                    print('#', end='')
            else:
                if row%2==0 and col>row:
                    print('#', end='')    
                else:
                    print('.', end='')
        for row in range(size-1, 0, -1): 
            if col%2 == 0: 
                if row%2==0 and col>=row:
                    print('.', end='')    
                else:
                    print('#', end='')
            else: 
                if row%2!=0 and col>=row:
                    print('#', end='')    
                else:
                    print('.', end='')
        print('')
    for col in range(size-2, -1, -1):
        for row in range(size): 
            if col%2 == 0: 
                if row%2!=0 and col>row:
                    print('.', end='')    
                else:
                    print('#', end='')
            else:
                if row%2==0 and col>row:
                    print('#', end='')    
                else:
                    print('.', end='')
        for row in range(size-1, 0, -1):
            if col%2 == 0: 
                if row%2==0 and col>=row:
                    print('.', end='')    
                else:
                    print('#', end='')
            else: 
                if row%2!=0 and col>=row:
                    print('#', end='')    
                else:
                    print('.', end='')
        print('')

print("*** Fun with Drawing ***")
size = int(input("Enter input : "))
draw_pyramid(size)

