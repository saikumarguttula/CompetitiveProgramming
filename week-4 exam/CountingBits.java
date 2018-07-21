import java.util.*;

public class CountingBits{

	static ArrayList <Integer> al = new ArrayList <Integer>();

	static void bitsCount(int n){

		if (n == 0) {
			al.add(n);
		}

		else {
			int count = 0;
			while (n != 0) {
				int rem = n %2;
				n = n/2;

				if(rem == 1)
					count++;
			}
			al.add(count);
		}

	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();

		for (int i=0;i<=num;i++) {
			bitsCount(i);
		}

		System.out.println(al);
	}
}
