class MinStack {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    /** initialize your data structure here. */
    public MinStack() {
        Stack<Integer> st1 = new Stack<>();
        Stack<Integer> st2 = new Stack<>();
        stack1 = st1;
        stack2 = st2;
    }
    
    public void push(int x) {
        stack1.push(x);
        if(stack2.empty()){
            stack2.push(x);
        }else {
            stack2.push(Math.min(stack2.peek(),x));
        }
        
    }
    
    public void pop() {
        stack2.pop();
        stack1.pop();
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int getMin() {
        return stack2.peek();
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
