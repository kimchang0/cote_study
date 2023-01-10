package cote_study_java;
import java.lang.Math;

public class next_word {

	/**
	 * # ���� ����
	 * �������� Ȥ�� ������ common�� �Ű������� �־��� ��, ������ ���� �������� �� ���ڸ� return �ϵ��� solution �Լ��� �ϼ��غ�����.
	 * 
	 * # ���ѻ��� 
	 * 2 < common�� ���� < 1,000
	 * -1,000 < common�� ���� < 2,000 
	 * common�� ���Ҵ� ��� �����Դϴ�.
	 * �������� Ȥ�� �������� �ƴ� ���� �����ϴ�.
	 * �������� ��� ����� 0�� �ƴ� �����Դϴ�.
	 * 
	 * # ����� ��
	 * common	result
	 * [1, 2, 3, 4]	5
	 * [2, 4, 8]	16
	 * 
	 * # ����� �� ����
	 * ����� �� #1
	 * [1, 2, 3, 4]�� ������ 1�� ���������̹Ƿ� ������ �� ���� 5�̴�.
	 * 
	 * ����� �� #2
	 * [2, 4, 8]�� ���� 2�� �������̹Ƿ� ������ �� ���� 16�̴�.
	 */
	
	
	public static void main(String[] args) {
		
		int [] arr = {1, 2, 4, 8};
		int res = solution(arr);
		System.out.println(res);
	}

	public static int solution(int[] common) {
		
		if(common[1] - common[0] == common[2] - common[1]) { // ���������� ������������ �˾ƺ��� ���� ������ ����
			return common[0] + (common[1] - common[0]) * (common.length); // ���������� ��� �������� ����(an = a1 +(n-1)d)�� �̿��� ����
		} else {
			return (int) (common[0] * Math.pow((common[1] / common[0]), common.length)); // �������� ��� ������ ����(an = a1 * Math.pow(r, n-1);)�� ���� ����
		}
	}

}
