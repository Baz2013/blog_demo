import edu.princeton.cs.algs4.StdRandom;

/**
 * Created by gucb on 2016/11/23.
 */
public class EXER1E1P13 {

    public static final int RandNum = 10;
    public static final int FEILD = 5;

    public static int[][] get_array() {
        int len1 = StdRandom.uniform(RandNum);
        int len2 = StdRandom.uniform(RandNum);
        int[][] res = new int[len1][len2];

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                int num = StdRandom.uniform(FEILD);
                res[i][j] = num;
            }
        }

        return res;
    }

    public static void  printArrary(int[][] r_array){
        for (int i = 0; i < r_array.length; i++) {
            for (int j = 0; j < r_array[i].length; j++) {
                System.out.print(r_array[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void transposition(int[][] r_array) {


    }

    public static void main(String[] args) {
        int[][] arr = get_array();
        printArrary(arr);
    }
}
