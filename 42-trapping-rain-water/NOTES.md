​
* * intuition is bascially , we keep pushing index in stack until a element comes who is greater than top of the stack element;
* eg:
* 1st element is 5  st =[5]
* 2nd - 4  st = [5,4]
* 3rd - 3 st = [5,4,3]
* doing this we can see that there is no boundary on right side so theres no way water will be stored.
* unitl a bigger element that top of stack comes we will not get any stored water
* if bigger element comes like
* eg: 4th element - 5 st = [5,4,3,5]  // now here will be haviing some water stored
* so now we will be getting how much water is stored
​
so we will be poping stack element till curr element is bigger than top element;
​
i.e while(arr[st.top()]<arr[i])
​
now we will pop current top
curr = st.top();
st.pop();
​
now we will find the width of water stored for each index
// curr_index - top -1;
diff = i-st.top()-1;
​
boundary elements min ---> min(arr[i],arr[st.top()])   // min(right , left);
now we also need to minus the height of curr block
and this will be multiplied with difference
​
i,e  min(arr[i],arr[st.top()]) - arr[curr]) * diff;
// this wiill give water stored for each index
​
​
​
​
​