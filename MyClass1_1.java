/* 
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures.
*/
public class MyClass1_1{
public static void main (String[] args){
String test1 = "This wont work";
String test2= "thisSHould";
if (isUnique(test1)) System.out.println("WTF THIS IS WRONG");
else {System.out.println(test1);
//      System.out.println(test1.length);
      System.out.println(test1.length());
}

if (isUnique(test2)) System.out.println(test2);
else System.out.println("WTF THIS IS WRONG prt2");

}

public static boolean isUnique(String str){
  if (str.length()>128) return false;

  boolean[] set = new boolean[128];
  for (int i=0; i < str.length(); i++){
    int val = str.charAt(i);
    if(set[val]){
      return false;
    }
    set[val]=true;
  }
  return true;

}
}
