// this is follow up: optimize the space useage of stack 2 if there are a lot of duplicate elements in stack1
// like 2222221111112134333333311111-1

class MinStack {
    private Stack<Integer> stack1;
    private Stack<HashMap> stack2;
    /** initialize your data structure here. */
    public MinStack() {
        Stack<Integer> st1 = new Stack<>();
        Stack<HashMap> st2 = new Stack<>();
        stack1 = st1;
        stack2 = st2;
    }
    
    public void push(int x) {
        stack1.push(x);
        if(stack2.empty()){
            HashMap<Integer, Integer> map = new HashMap<>();
            map.put(x,stack1.size());
            stack2.push(map);
        }else {
            int lastMin = (int) stack2.peek().keySet().toArray()[0];
            int min = Math.min(lastMin,x);
            

            if(lastMin != min){
                HashMap<Integer, Integer> map = new HashMap<>();
                map.put(min,stack1.size());
                stack2.push(map);
            }
        }
        
    }
    
    public void pop() {
        stack1.pop();
        if(stack1.size() < (int) stack2.peek().values().toArray()[0]) {
            stack2.pop();
        }
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int getMin() {
       return (int) stack2.peek().keySet().toArray()[0];
      
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
