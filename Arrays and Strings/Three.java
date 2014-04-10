public class Three {
    
    public static void main(String[] args) {
        String s = "Heee1eee";
        char[] chars = s.toCharArray();
        removeDuplicates(chars);
        System.out.println(chars);
    }

    public static void removeDuplicates(char[] chars) {
        for (int i = 0; i < chars.length; i++) {
            for (int j = i+1; j < chars.length; j++) {
                if (chars[j] == chars[i]) {
                    chars[j] = ' ';
                }
            }
            if (chars[i] == ' ') {
                for (int j = i+1; j < chars.length; j++) {
                    if (chars[j] != chars[i]) {
                        chars[j] ^= chars[i];
                        chars[i] ^= chars[j];
                        chars[j] ^= chars[i];
                        break;
                    }
                }
            }
        }
    }

}
