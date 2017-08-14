using System;
using System.Collections;
using System.Collections.Generic;
using DecimaltoBinary;

	class MainClass
	{
		public static void Main (string[] args)
	{
//		1. Viết 1 chương trình convert 1 list có N phần tử (không cần nhập vào từ bàn phím) số hệ thập phân ra hệ nhị phân nhé, mấy cái 10001011 ý :)))

 	List<int> numbers = new List<int> ();
	Random rand = new Random();

	for (int i = 0; i < 11; i++) 
	{
		numbers.Add (System.Random(0, 100));
		Console.WriteLine(numbers);

		for (int x=0; x < numbers.Count; x++)
		{
			string binary = Convert.ToString(numbers[x],2);
					Console.WriteLine("This number:" + numbers[x]);
					Console.WriteLine(" In binary is: " + binary);
		}
	

	}
	}
}
