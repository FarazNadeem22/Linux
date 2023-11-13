class Solution {
    public String mergeAlternately(String word1, String word2) {
        int lenWrdOne = word1.length();
        int lenWrdTwo = word2.length();
        int loopOverThis = lenWrdOne + lenWrdTwo;
        int counter = 0;
        String merged = "";

        while (counter < loopOverThis) {
            if (counter < lenWrdOne) {
                try {
                    merged = merged + word1.charAt(counter);
                } catch (Exception e) {
                    // Do nothing
                }
            }
            if (counter < lenWrdTwo) {
                try {
                     merged = merged + word2.charAt(counter);
                } catch (Exception e) {
                    // Do nothing
                }
            }
            counter++;
        }

        return merged;
    }
}
