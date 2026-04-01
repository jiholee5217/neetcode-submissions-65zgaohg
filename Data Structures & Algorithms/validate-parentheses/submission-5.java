class Solution {
    public boolean isValid(String s) {
        char[] sArray = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> parentheses = new HashMap<>();

        parentheses.put(')', '(');
        parentheses.put(']', '[');
        parentheses.put('}', '{');

        for (int i = 0; i < sArray.length; i++) {
            if (parentheses.containsKey(sArray[i])) {
                if (!stack.isEmpty() && stack.peek() == parentheses.get(sArray[i])) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(sArray[i]);
            }
        }

        return stack.isEmpty();
    }
}
