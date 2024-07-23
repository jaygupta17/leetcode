class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> nums = new ArrayList<>();
        for(int i=1; i<=9;i++){
            lex(n,i,nums);
        }
        return nums;
    }
    public void lex(int n,int i,List<Integer> result){
         if(i>n) return;
         result.add(i);   
         for(int j=0;j<=9;j++){
            lex(n,i*10+j,result);
         }
    }
}