class Solution {
    public boolean isPalindrome(String s) {
        // handles when string is just one char
        if (s.length() == 1) {
            return true;
        }

        // set two pointer indexes 
        int rightIndex = s.length() - 1;
        int leftIndex = 0;

        // go to the first letter of the left index
        while (Character.isLetterOrDigit(s.charAt(leftIndex)) == false && leftIndex < s.length() - 1) {
           // System.out.println(s.charAt(leftIndex));
            leftIndex += 1;
        }

        // go to the first letter of the right index
        while (Character.isLetterOrDigit(s.charAt(rightIndex)) == false && rightIndex > 0) {
            //System.out.println(s.charAt(rightIndex));
            rightIndex += -1;
        }

        int debugCounter = 1;
        System.out.println("Start Indexes " + leftIndex + " " + rightIndex);

        while (leftIndex < rightIndex) {
            while (Character.isLetterOrDigit(s.charAt(leftIndex)) == false) {
                System.out.println("counter");
                leftIndex++;
                if (leftIndex + 1 == s.length()) {
                    return true;
                }
            }

            while (Character.isLetterOrDigit(s.charAt(rightIndex)) == false) {
                rightIndex--;
                if (rightIndex + 1 == s.length()) {
                    return true;
                }
            }

           
            System.out.println("Start Indexes2 " + leftIndex + " " + rightIndex);
            if (Character.toLowerCase(s.charAt(leftIndex)) != Character.toLowerCase(s.charAt(rightIndex))) {
                System.out.println("Character at " + leftIndex + " is " + s.charAt(leftIndex));
                System.out.println("Character at " + rightIndex + " is " + s.charAt(rightIndex));
                System.out.println("Comparison #: " + debugCounter);
                debugCounter++;
                return false;
            }
            
            leftIndex++;
            rightIndex--;
        }

        return true;
    }
}
