using System;

namespace Session2inC
{
	class MainClass
	{
		public static void Main (string[] args)
		{

			//  serious exercise 1 - bmi exercise 

			Console.Write ("Bạn cao bao nhiêu m? ");
			float height = float.Parse (Console.ReadLine());
			Console.Write ("Bạn nặng bao nhiu kí? ");
			float weight = float.Parse (Console.ReadLine());
			float bmi = weight / (height * height);
			Console.WriteLine ("Chỉ số BMI của bạn là: " + bmi.ToString("F"));
			if (bmi < 16) 
			{
				Console.WriteLine ("Bạn thiếu thịt quá à. Cần bổ sung khẩn cấp!");
			} 
			else if (bmi <= 18.5) 
			{
				Console.WriteLine ("Cần bổ sung thịt cho đầy đặn nhé ;) ");
			} 
			else if (bmi <= 25) 
			{
				Console.WriteLine ("Ăn uống đầy đủ dinh dưỡng quá hen. Tiếp tục duy trì phong độ nhéo ;) ");
			} 
			else if (bmi <= 30) 
			{
				Console.WriteLine ("Có vẻ bạn hơi mập xíu xíu rùi.");
			} 
			else if (bmi > 30) 
			{
				Console.WriteLine ("Tập thể dục nhiều vô hen, hơi mũm mĩm quá ồi!");
			} 
			else 
			{
				Console.WriteLine ("Tui hông tính được bmi của bạn. Kiểm tra lại tui hoặc kiểm tra lại bạn đi!");
			}
			Console.ReadLine ();




			//Serious exercise 2: B-Max 

			Console.WriteLine ();
			Console.WriteLine ();
			Console.Write ("Hello, ");
			Console.Write ("my name is ");
			Console.WriteLine ("B-Max!");

			Console.WriteLine ();
			Console.WriteLine ();
			int column = 20;
			int row = 20;



			//Serious exercise 3: Star 

			for (int i = 0; i < column; i++) 
			{
				Console.Write ("* ");
			}

			Console.WriteLine ();
			Console.WriteLine ();
			for (int i = 0; i < column / 2; i++) 
			{
				Console.Write ("x ");
				Console.Write ("* ");
			}

			Console.WriteLine ();
			Console.WriteLine ();
			for (int i = 0; i < row; i++) 
			{
				if (i % 2 == 0) 
				{
					for (int j = 0; j < column / 2; j++) 
					{
						Console.Write ("x ");
						Console.Write ("* ");
					}
				} 
				else 
				{
					for (int j = 0; j < column / 2; j++) 
					{
						Console.Write ("* ");
						Console.Write ("x ");
					}	
				}
				Console.WriteLine ();
			}
			Console.ReadLine ();
		}
	}
}