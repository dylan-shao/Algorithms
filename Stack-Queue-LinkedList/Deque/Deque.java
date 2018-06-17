package StackQueueLinkedList;
import  java.util.*;
//deque using stacks

public class Deque {
 Stack<Integer> stack1;
 Stack<Integer> stack2;
 Stack<Integer> stack3;
 public Deque(){
     Stack<Integer> st1 = new Stack<>();
     Stack<Integer> st2 = new Stack<>();
     Stack<Integer> st3 = new Stack<>();
     stack1 = st1;
     stack2 = st2;
     stack3 = st3;
 }

 public void lPush(int x) {
     stack1.push(x);
 }

  public void rPush(int x) {
     stack2.push(x);
 }

  public int lPop() {
	 if(this.isEmpty()) {
		 throw new EmptyStackException();
	 }
     if(stack1.empty()) {
         int size = stack2.size()/2;
         while(size>0) {
             stack3.push(stack2.pop());
             size--;
         }
         while(!stack2.empty()) {
             stack1.push(stack2.pop());
         }
         while(!stack3.empty()) {
             stack2.push(stack3.pop());
         }
     }
     return stack1.pop();
 }

  public int rPop() {
	 if(this.isEmpty()) {
		 throw new EmptyStackException();
	 }
     if(stack2.empty()) {
         int size = stack1.size()/2;
         while(size>0) {
             stack3.push(stack1.pop());
             size--;
         }
         while(!stack1.empty()) {
             stack2.push(stack1.pop());
         }
         while(!stack3.empty()) {
             stack1.push(stack3.pop());
         }
     }
     return stack2.pop();
 }
  
  public int size() {
	  return stack1.size() + stack2.size();
  }
  
  public boolean isEmpty() {
	  return stack1.empty() && stack2.empty();
  }
  
  public static void main(String []args){
	  Deque d = new Deque();
	  d.rPush(4);
	  d.rPush(5);
	  d.rPush(6);
	  d.lPush(3);
	  d.lPush(2);
	  d.lPush(1);
	  while (!d.isEmpty())
      {
          System.out.print(d.lPop()+" ");
      }
  }
}
