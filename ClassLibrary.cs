using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary2
{
    public abstract class Car
    {
        public int X { get; set; }
        public string Name { get; set; }
        public abstract char Symbol { get; }
        public abstract void Step();
        public abstract void PrintMap(int width);

    }
    public class SpeedCar : Car
    {
        Random rnd = new Random(0);
        public override char Symbol { get { return '>'; } }
        public override void Step()
        {
            this.X +=rnd.Next(3,6);
        }
        public SpeedCar(string name)
        {
            Name = name;
        }
        public override void PrintMap(int width)
        {
            char[] way = new char[width];
            for (int i = 0; i < width; i++)
            {
                way[i] = '-';
            }
            way[X] = Symbol;
            foreach (char symbol in way)
            {
                Console.Write(symbol);
            }
            Console.WriteLine();
        }
    }
    public class SlowCar : Car
        {
            Random rnd = new Random(0);
            public override char Symbol { get { return '0'; } }
            public override void Step()
            {
                this.X+=rnd.Next(0,3);
            }
            public SlowCar(string name)
            {
                Name = name;
            }
            public override void PrintMap(int width)
            {
                char[] way = new char[width];
                for (int i = 0; i < width; i++)
                {
                    way[i] = '-';
                }
                way[X] = Symbol;
                foreach (char symbol in way)
                {
                    Console.Write(symbol);
                }
                Console.WriteLine();
        }
    }

}

