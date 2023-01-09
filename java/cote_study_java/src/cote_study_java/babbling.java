package cote_study_java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;

public class babbling {
	static LinkedList<String> Arr = new LinkedList<String>();

	public static void main(String[] args) {

		String[] babble = { "aya", "ye", "woo", "ma" };
		int res = solution(babble);
		System.out.println(res);

	}

	public static int solution(String[] babbling) {
		int answer = 0;

		LinkedList<String> list = new LinkedList<String>();
		LinkedList<String> n = new LinkedList<String>(Arrays.asList("aya", "ye", "woo", "ma"));

		int check[] = new int[n.size()];

		for (int i = 1; i <= 4; i++) {
			permutation(list, check, n, i);
			list.clear();
		}
		ArrayList<String> obj = new ArrayList<String>(Arrays.asList(babbling));
		
		for (String i : Arr) {
			answer += Collections.frequency(obj, i);
		}

		return answer;
	}

	private static void permutation(LinkedList<String> list, int[] check, LinkedList<String> n, int r) {

		if (list.size() == r) {

			String str_val = "";

			for (String i : list) {
				str_val += i;
			}

			Arr.add(str_val);
			return;

		} else {
			for (int i = 0; i < n.size(); i++) {

				if (check[i] == 0) {

					check[i] = 1;
					list.add(n.get(i));
					permutation(list, check, n, r);
					list.removeLast();
					check[i] = 0;

				}

			}

		}

	}

}
