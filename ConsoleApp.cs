using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ClassLibrary2;
namespace ConsoleApp26
{
    class Program
    {
        static string CreateRandomString()
        {
            Random ForString = new Random();
            string result = "";
            for(int i = 0; i < 6; i++)
            {
                if (i == 0)
                {
                    result += (char)ForString.Next(65, 91);
                }
                else
                {
                    result += (char)ForString.Next(97,123);
                }
            }
            return result;
        }
        static void Main(string[] args)
        {
            Random rnd = new Random();
            int whith = 50;//rnd.Next(10,31);
            List<Car> test = new List<Car>();
            for(int i = 0; i < 20; i++)
            {
                
                if (rnd.Next(0, 2) % 2 == 0)
                {
                    test.Add(new SlowCar(CreateRandomString()));
                }
                else
                {
                    test.Add(new SpeedCar(CreateRandomString()));
                }
            }
            do
            {
                for(int j = 0; j < 20; j++)
                {
                    test[j].PrintMap(whith);
                    test[j].Step();
                }
                Console.WriteLine();
                while (Console.ReadKey().Key != ConsoleKey.Spacebar) ;
                
            } while ((test[0].X<whith) & (test[1].X < whith) & (test[2].X < whith) & (test[3].X < whith) & (test[4].X < whith) & (test[5].X < whith));
            int max=0;
            foreach (Car obj in test)
            {
                if (obj.X > max)
                {
                    max = obj.X;
                }
            }
            string result="";
            foreach (Car obj in test)
            {
                if (obj.X == max)
                {
                    result = obj.Name;
                }
            }
            
         
            Console.ReadKey();
        }
    }
}
