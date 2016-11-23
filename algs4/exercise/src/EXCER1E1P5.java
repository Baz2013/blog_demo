/**
 * Created by gucb on 2016/11/23.
 */
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdIn;

public class EXCER1E1P5 {

        public static boolean isZeroToOne(Double x){
            if (x > 0.0000001 && x < 1.0)
                return true;
            else
                return false;
        }
        public static void main(String[] args){
            Double a = StdIn.readDouble();
            Double b = StdIn.readDouble();

            System.out.println(isZeroToOne(a)&&isZeroToOne(b));
        }
}
