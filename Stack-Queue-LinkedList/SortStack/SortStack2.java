// only use one additional stack
import java.util.*;
public class SortStack2 {
    // This function return the sorted stack
    public static Stack<Integer> sortstack(Stack<Integer> input) {
        Stack<Integer> tmpStack = new Stack<Integer>();
        while(!input.isEmpty()) {
            int globalMin = Integer.MAX_VALUE;
            while(!input.isEmpty()) {
                int tmpValue = input.pop();
                globalMin = Math.min(globalMin, tmpValue);
                tmpStack.push(tmpValue);
            }
            int count = 0;
            while(!tmpStack.isEmpty() && tmpStack.peek()>=globalMin) {
                int tmpValue = tmpStack.pop();
                if(tmpValue == globalMin) {
                    count++;
                }else {
                    input.push(tmpValue);
                }
            }
            while(count>0) {
                tmpStack.push(globalMin);
                count--;
            }
        }
        return tmpStack;
    }
    
  public static void main(String []args){
    Stack<Integer> input = new Stack<Integer>();
        input.add(34);
        input.add(3);
        input.add(31);
        input.add(98);
        input.add(92);
        input.add(23);
     
        // This is the temporary stack
        Stack<Integer> tmpStack=sortstack(input);
        System.out.println("Sorted numbers are1:");
     
        while (!tmpStack.empty())
        {
            System.out.print(tmpStack.pop()+" ");
        } 
}
}
