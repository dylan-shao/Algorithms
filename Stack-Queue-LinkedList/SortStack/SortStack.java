import java.util.*;
public class SortStack {
    // This function return the sorted stack
    public static Stack<Integer> sortstack(Stack<Integer> input) {
        Stack<Integer> tmpStack1 = new Stack<Integer>();
        Stack<Integer> tmpStack2 = new Stack<Integer>();
        
        while(!input.isEmpty() || !tmpStack1.isEmpty()) {
            int globalMin = Integer.MAX_VALUE;
            while(!input.isEmpty()) {
                int tmpVal = input.pop();
                tmpStack1.push(tmpVal);
                globalMin = Math.min(globalMin, tmpVal);
            }
            while(!tmpStack1.isEmpty()) {
                int tmpV = tmpStack1.pop();
                if(tmpV == globalMin) {
                    tmpStack2.push(globalMin);
                }
                else {
                	input.push(tmpV);
                }
            }
        }
        return tmpStack2; 
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
        System.out.println("Sorted numbers are:");
     
        while (!tmpStack.empty())
        {
            System.out.print(tmpStack.pop()+" ");
        } 
  }
}
