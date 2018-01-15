inport numpy as np
function GreenCoordiantesAlgo(V,T,M)
//V : vertex de la cage, T : Face de la cage (ensemble de triplet contenant les sommets), M : Point du maillage
for i in length(M):
	for j in lenght(T):
		n=
		for k in range(3):
			T[j,k]-=i
		p = dot(T[j,k]