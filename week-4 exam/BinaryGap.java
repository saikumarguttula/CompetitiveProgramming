import java.util.*;

public class BinaryGap{

	static void gap_Binary(String st){
		int max = 0, count = 0;

		for (int i=0;i<st.length();i++) {

			if (st.charAt(i) == '0') {
				count = 0;
			}

			if (st.charAt(i) == '1') {
				count++;
			}

			if (count > max) {
				max = count;
			}
		}
		System.out.println(max);
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		int rem = 0;

		String st = "";

		while(num != 0){
			rem = num % 2;
			st = st + rem;
			num = num/2;
		}
		System.out.println(st);
		gap_Binary(st);
	}
}
