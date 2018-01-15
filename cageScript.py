import maya.cmds as cmds;

cmds.duplicate('polySurface1');
cmds.select('polySurface2');
cmds.polyReduce(p=80,ch=False,kev=True);
cmds.select('polySurface2.vtx[0:196]');
#cmds.moveVertexAlongDirection(n = 0.367418);