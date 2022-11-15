import java.io.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // let's create example data
        Dimensions dim1 = new Dimensions(1, 2, 3);
        Dimensions dim2 = new Dimensions(2, 3, 4);

        // constructor/method overload
        Dimensions dim3 = new Dimensions(dim2);

        // method override
        System.out.printf("toString override: %s\n", dim3);

        // object attribute
        System.out.printf("Height: %.2f, Length: %.2f, Width: %.2f\n", dim1.getHeight(), dim1.getLength(), dim1.getWidth());

        Package pkg1 = new Package(dim1, 4);
        // complex attribute
        System.out.printf("Package dimensions: %s\n", pkg1.getDimensions());

        // derived attribute
        System.out.printf("Package volume: %.2f\n", pkg1.getVolume());

        Package pkg2 = new Package(dim2, 5);
        Package pkg3 = new Package(dim3, 6);
        List<Package> packages = new ArrayList<>();
        packages.add(pkg1);

        Shipment shipment = new Shipment(LocalDate.now(), packages);

        // mandatory attribute
        System.out.printf("Ship date: %s\n", shipment.getShipDate());

        // optional attribute
        System.out.printf("Delivery date: %s\n", shipment.getDeliveryDate());
        shipment.setDeliveryDate(LocalDate.now().plusDays(1));
        System.out.printf("Delivery date: %s\n", shipment.getDeliveryDate());

        // multivalued attribute
        shipment.addPackage(pkg2);
        shipment.addPackage(pkg3);

        // class attribute
        Shipment.setMaxNumberOfDaysBetweenTodayAndShipDate(7);
        System.out.printf("Furthest possible ship date for a new entry: %s\n", LocalDate.now().plusDays(Shipment.getMaxNumberOfDaysBetweenTodayAndShipDate()));

        // class extent
        System.out.printf("There are currently: %d instances of Shipment class\n", Shipment.getExtent().size());

        // class method
        System.out.printf("Number of shipments sent today: %d\n", Shipment.findShipmentsSentOnDate(LocalDate.now()).size());

        // extent - persistence
        File file = new File("extent");
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file))) {
            Shipment.saveExtent(out);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(file))) {
            Shipment.loadExtent(in);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}