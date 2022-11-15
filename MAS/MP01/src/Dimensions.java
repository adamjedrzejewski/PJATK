import java.io.Serializable;

public class Dimensions implements Serializable {
    private double length; // object attribute
    private double width; // object attribute
    private double height; // object attribute

    private static final double lowerBoundary = 0.0;

    public Dimensions(double length, double width, double height) {
        setLength(length);
        setWidth(width);
        setHeight(height);
    }

    public Dimensions(Dimensions dimensions) { // method overload
        this(dimensions.length, dimensions.width, dimensions.height);
    }

    public void setLength(double length) {
        if (length <= lowerBoundary)
        {
            throw new IllegalArgumentException("Length out of boundary.");
        }
        this.length = length;
    }

    public void setWidth(double width) {
        if (width <= lowerBoundary)
        {
            throw new IllegalArgumentException("Length out of boundary.");
        }
        this.width = width;
    }

    public void setHeight(double height) {
        if (height <= lowerBoundary)
        {
            throw new IllegalArgumentException("Length out of boundary.");
        }
        this.height = height;
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public String toString() { // method override
        return "Dimensions{" +
                "length=" + length +
                ", width=" + width +
                ", height=" + height +
                '}';
    }
}
