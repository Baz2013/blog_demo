/**
 * Created by gucb on 2016/11/23.
 */
import edu.princeton.cs.algs4.StdRandom;

public class EXCER1E1P11 {

    public static final int RandNum = 20;

    public static boolean[][] get_array() {
        int len1 = StdRandom.uniform(RandNum);
        int len2 = StdRandom.uniform(RandNum);
        boolean[][] res = new boolean[len1][len2];

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                int num = StdRandom.uniform(2);
                if(num == 0)
                    res[i][j] = true;
                else
                    res[i][j] = false;
            }
        }

        return res;
    }

    public static void  printArrary(boolean[][] r_array){
        for (int i = 0; i < r_array.length; i++) {
            for (int j = 0; j < r_array[i].length; j++) {
                if (r_array[i][j] == true)
                    System.out.print('*');
                else
                    System.out.print(' ');
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        boolean[][] tmp_array = get_array();
        printArrary(tmp_array);
    }
}
