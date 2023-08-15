# มี map โดยที่ เลข 0 เป็นน้ำทะเล เลข 1 เป็นพื้นดิน จงหาว่าใน map มีกี่เกาะถ้าพื้นดินติดกันซ้าย ขวา บน ล่าง ถือว่าเป็นเกาะเดียวกัน

# เช่น
# 0001
# 1100
# 0010

# จะมี3เกาะ

def deleteIsland(Map, y, x):
    if y < 0 or y >= len(Map) or x < 0 or x >= len(Map[0]) or Map[y][x] != 1:
        return
    Map[y][x] = 0

    deleteIsland(Map, y - 1, x)
    deleteIsland(Map, y + 1, x)
    deleteIsland(Map, y, x - 1)
    deleteIsland(Map, y, x + 1)


def countIsland(Map):
    count = 0
    for y in range(len(Map)):
        for x in range(len(Map[0])):
            if Map[y][x] == 1:
                count += 1
                deleteIsland(Map, y, x)
    return count


inp = input("Enter Input : ").split('/')

Map = []

for i in inp:
    temp = [*i]
    temp = list(map(int, temp))
    Map.append(temp)

print(f"Island have : {countIsland(Map)}")
