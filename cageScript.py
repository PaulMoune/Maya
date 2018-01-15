import maya.cmds as cmds;

cmds.duplicate('polySurface1');
cmds.select('polySurface2');
cmds.polyReduce(p=80,ch=False,kev=True);
cmds.select('polySurface2');
nor = [];
nb = cmds.polyEvaluate(v=True);
for i in range(nb):
    nor.append(0.367418);
print(nor)
cmds.select('polySurface2.vtx[:]');
cmds.moveVertexAlongDirection(n = nor);