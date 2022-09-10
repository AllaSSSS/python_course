# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

void DecToBinary(int number)
{
    string Binary = "";
    while (number > 0)
    {
        Binary = number % 2 + Binary;
        number /= 2;
    }
    Console.WriteLine(Binary);
}

DecToBinary(10);