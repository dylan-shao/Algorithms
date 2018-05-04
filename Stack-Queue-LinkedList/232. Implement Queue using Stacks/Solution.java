class MyQueue {
    Stack<Integer> stack1;
    Stack<Integer> stack2;
    private int front;
    /** Initialize your data structure here. */
    public MyQueue() {
        Stack<Integer> st1 = new Stack<>();
        Stack<Integer> st2 = new Stack<>();
        stack1 = st1;
        stack2 = st2;
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        if(stack1.empty()){
            front = x;
        }
        stack1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(stack2.empty()) {
            while(!stack1.empty()){
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
    
    /** Get the front element. */
    public int peek() {
       if(stack2.empty()) {
            return front;
        }
        return stack2.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack1.empty() && stack2.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
