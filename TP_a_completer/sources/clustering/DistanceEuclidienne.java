package clustering;

/**
 * Distance entre deux données numériques.
 *
 * @author  Emilie Allart
 */
public class DistanceEuclidienne implements Distance {

	@Override
	public double valeur(Donnee d1, Donnee d2) throws ClusterException {
		if (d1.nbDimensions() != d2.nbDimensions())
			throw new ClusterException("les donnees doivent avoir la même dimension");
		int dist = 0;
		for (int i = 0; i < d1.nbDimensions(); i++ ) {
			dist += Math.pow((d1.valeurDim(i)-d2.valeurDim(i)),2);
		}
		return Math.sqrt(dist);
	}

}
