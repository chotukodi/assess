import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile {
    public static void main(String[] args)  throws FileNotFoundException {

           File file = new File("data.txt");
            Scanner scan = new Scanner(file);

            System.out.println(scan.nextLine());

        }

}