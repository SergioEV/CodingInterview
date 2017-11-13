public class MyClass1_2{
  public static void main (String[] args){
    String test1 = "hi";
    String test2 = "ih";
    sort(test1);
    sort(test2);
    if(permutation(test1,test2))
      System.out.println(test1 + " and " + test2 + " are permutations");
  }

  static String sort(String s){
    char[] array = s.toCharArray();
    java.util.Arrays.sort(array);
    return new String(array);
  }

  static boolean permutation(String s, String t){
    if(s.length()!=t.length())
      return false;
    return sort(s).equals(sort(t));
  }
}

