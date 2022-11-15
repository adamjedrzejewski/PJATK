import java.io.Serializable;

public class Package implements Serializable {
    private Dimensions dimensions; // complex attribute
    private double weight; // simple attribute
    public static final double weightLowerBoundary = 0.0; // class attribute

    public Package(Dimensions dimensions, double weight) {
        setDimensions(dimensions);
        setWeight(weight);
    }

    public void setDimensions(Dimensions dimensions) {
        if (dimensions == null) {
            throw new IllegalArgumentException("Dimensions cannot be null.");
        }
        this.dimensions = dimensions;
    }

    public void setWeight(double weight) {
        if (weight <= weightLowerBoundary) {
            throw new IllegalArgumentException("Weight out of boundary.");
        }
        this.weight = weight;
    }

    public Dimensions getDimensions() {
        return new Dimensions(this.dimensions);
    }

    public double getWeight() {
        return this.weight;
    }

    public double getVolume() {
        return dimensions.getHeight() * dimensions.getLength() * dimensions.getWidth();
    }

    @Override
    public String toString() {
        return "Package{" +
                "dimensions=" + dimensions +
                ", weight=" + weight +
                '}';
    }
}
