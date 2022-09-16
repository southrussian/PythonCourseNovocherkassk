vertices = ["Vertex0", "Vertex1", "Vertex2", "Vertex3", "Vertex4", "Vertex5"]
coordinates = [5, 3, 2, 1, 4, 0]

vertices_sorted = []

for i in coordinates:
    for j in vertices:
        if i == vertices.index(j):
            vertices_sorted.append(j)
print(vertices_sorted)

try:
    triangles_f = open('triangles.txt', 'r')  # откроем файл с треугольниками
    triangles_list = [line.split() for line in triangles_f]
    print('Длина массива точек:', len(triangles_list))
    print(triangles_list)
finally:
    triangles_f.close()
