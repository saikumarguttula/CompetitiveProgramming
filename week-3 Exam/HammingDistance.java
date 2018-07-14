import java.util.*;

public class HammingDistance{

	public static int [] decimalToBinary(int z,int[] arr){
		int i = 7;
		while(z != 0){
			int rem = z%2;
			arr[i--] = rem;
			z = z/2;
		}

		return arr;
	} 


	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		int y = input.nextInt();
		int[] arr1 = new int[8];
		int[] arr2 = new int[8];
		System.out.println(Arrays.toString(decimalToBinary(x,arr1)));
		System.out.println(Arrays.toString(decimalToBinary(y,arr2)));
		int distance = 0;
		for (int i=0,j=0;i<8;i++,j++) {
			if(arr1[i] != arr2[j]){
				distance++;
			}
		}
		System.out.println(distance);
	}

}
