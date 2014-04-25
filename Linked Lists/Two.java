import java.util.*;

public class Two {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        list.add(5);
        list.add(2);
        list.add(-3);
        list.add(7);

        System.out.println(findNthToLast(list, 0));
    }

    public static Integer findNthToLast(LinkedList<Integer> list, int n) {
        int count = list.size();
        if (n >= count || count == 0 || n < 0) {
            return null;
        }
        int finalIndex = count - n - 1;
        int soFar = 0;
        int value = 0;
        while (soFar <= finalIndex) {
            value = list.get(soFar);
            soFar++;
        }
        return value;

    }
}
