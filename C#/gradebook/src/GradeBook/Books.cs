using System;
using System.Collections.Generic;

namespace GradeBook
{
    class Book
    {
        public Book(string name)
        {
            grades = new List<double>();
            this.name = name;
        }
        public void AddGrade(double grade)
        {
            grades.Add(grade);
        }

        public void ShowStats()
        {
            var result = 0.0;
            var HighGrade = double.MinValue;
            var LowGrade = double.MaxValue;
            foreach (var number in grades)
            {
                HighGrade = Math.Max(number, HighGrade);
                LowGrade = Math.Min(number, LowGrade);
                result += number;
            }
            result /= grades.Count;
            Console.WriteLine($"The highest grade is {HighGrade:N1}");
            Console.WriteLine($"The lowest grade is {LowGrade:N1}");
            Console.WriteLine($"The average grade is {result:N1}");
        }

        private List<double> grades;
        private string name;
    }
}