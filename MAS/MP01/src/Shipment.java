import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Shipment implements Serializable {
    private LocalDate shipDate; // mandatory attribute
    private LocalDate deliveryDate; // optional attribute

    private static int maxNumberOfDaysBetweenTodayAndShipDate = 7;

    private final List<Package> packages = new ArrayList<>(); // multi value attribute
    private static List<Shipment> extent = new ArrayList<>(); // extent

    private void addToExtent() {
        extent.add(this);
    }

    private void removeFromExtent() {
        extent.remove(this);
    }

    public Shipment(LocalDate shipDate, LocalDate deliveryDate, List<Package> packages) {
        setShipDate(shipDate);
        setDeliveryDate(deliveryDate);

        this.packages.addAll(packages);
        addToExtent();
    }

    public Shipment(LocalDate shipDate, List<Package> packages) {
        setShipDate(shipDate);

        this.packages.addAll(packages);
        addToExtent();
    }

    public Shipment(LocalDate shipDate) {
        setShipDate(shipDate);
        addToExtent();
    }

    public void setShipDate(LocalDate shipDate) {
        if (shipDate == null) {
            throw new IllegalArgumentException("Ship date is required.");
        }
        if (shipDate.isBefore(LocalDate.now())) {
            throw new IllegalArgumentException("Ship date in the past");
        }

        this.shipDate = shipDate;
    }

    public void setDeliveryDate(LocalDate deliveryDate) {
        if (deliveryDate == null) {
            throw new IllegalArgumentException("Delivery date is required.");
        }
        if (deliveryDate.isBefore(LocalDate.now())) {
            throw new IllegalArgumentException("Delivery date in the past");
        }

        this.deliveryDate = deliveryDate;
    }

    public void addPackage(Package pkg) {
        if (pkg == null) {
            throw new IllegalArgumentException("Package cannot be null");
        }

        packages.add(pkg);
    }

    public void removePackage(Package pkg) {
        packages.remove(pkg);
    }

    public LocalDate getShipDate() {
        return shipDate;
    }

    public LocalDate getDeliveryDate() {
        return deliveryDate;
    }

    public List<Package> getPackages() {
        return new ArrayList<>(packages);
    }

    @SuppressWarnings("unchecked")
    public static void loadExtent(ObjectInputStream in) throws IOException, ClassNotFoundException {
        extent = (ArrayList<Shipment>) in.readObject();
    }

    public static void saveExtent(ObjectOutputStream out) throws IOException{
        out.writeObject(extent);
    }

    public static List<Shipment> getExtent() {
        return new ArrayList<>(extent);
    }

    public static void showExtent() {
        for (Shipment shipment : extent) {
            System.out.println(shipment);
        }
    }

    public static List<Shipment> findShipmentsSentOnDate(LocalDate date) {
        if (date == null) {
            throw new IllegalArgumentException("Date cannot be null.");
        }

        return extent
                .stream()
                .filter(s -> s.shipDate.equals(date))
                .collect(Collectors.toList());
    }

    public static int getMaxNumberOfDaysBetweenTodayAndShipDate() {
        return maxNumberOfDaysBetweenTodayAndShipDate;
    }

    public static void setMaxNumberOfDaysBetweenTodayAndShipDate(int maxNumberOfDaysBetweenTodayAndShipDate) {
        Shipment.maxNumberOfDaysBetweenTodayAndShipDate = maxNumberOfDaysBetweenTodayAndShipDate;
    }

    @Override
    public String toString() {
        return "Shipment{" +
                "shipDate=" + shipDate +
                ", deliveryDate=" + deliveryDate +
                ", packages=" + packages +
                '}';
    }
}
