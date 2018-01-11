import maya.api.OpenMaya as OM
MyFile = open("C:\Users\ensimag\Documents\MayaProject\Lowres.off","r")
mesh = OM.MFnMesh()
data = MyFile.readline().rstrip('\n\r').split(" ")
if data[0] != "OFF" :
    print("Error : il faut lire un fichier OFF")
else :
    data = MyFile.readline().rstrip('\n\r').split(" ")
    print(data)
    nb_vertices, nb_faces = int(data[0]),int(data[1])
    Vertices = []
    for i in range(0,nb_vertices) :
        data = MyFile.readline().rstrip('\n\r').split(" ")
        Vertices.append(float(data[0]))
        Vertices.append(float(data[1]))
        Vertices.append(float(data[2]))
    for i in range( nb_faces ) :
        data = MyFile.readline().rstrip('\n\r').split(" ")
        vert = int(data[0])
        points = []
        for j in range(vert) :
            points.append(OM.MPoint(Vertices[3*int(data[j+1])],Vertices[3*int(data[j+1])+1],Vertices[3*int(data[j+1])+2]))
        print(points)
        mesh.addPolygon(points, mergeVertices=True, pointTolerance=0.0001)
MyFile.close()