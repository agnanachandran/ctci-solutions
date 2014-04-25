public class Three {

    public static class Node {
        Node next = null;
        int data;
        public Node(int d) { data = d; }
        public void appendToTail(int d) {
            Node end = new Node(d);
            Node n = this;
            while (n.next != null) {
                n = n.next;
            }
            n.next = end;
        }
    }

    public static void main(String[] args) {
        Node ll1 = new Node(3);
        ll1.appendToTail(1);
        ll1.appendToTail(5);
        Node ll2 = new Node(5);
        ll2.appendToTail(9);
        ll2.appendToTail(2);

        int carry = 0;
        while (ll1 != null) {
            int sum = ll1.data + ll2.data + carry;
            if (sum > 9) {
                carry = 1;
                sum -= 10;
            }
            System.out.println(sum);
            ll1 = ll1.next;
            ll2 = ll2.next;
        }

    }
}
