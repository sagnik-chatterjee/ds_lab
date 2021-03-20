##Recursion
## Loops

defmodule Module8 do

    def main do
      do_recursion()
      looping()
    end

    def looping do
      ##using recusrtsion to loop since datas as immutable

      IO.puts("Sum : #{sum([1,2,3])}")

      loop(5,1)

    end

    def sum([]) ,do: 0


    def sum([h|t]) ,do: h + sum(t)
    ##sum the head with the tail

    def loop(0,_), do: nil

    def loop(max,min) do
      if max < min do
        loop(0,min)
      else
        IO.puts("Num:- #{max}")
        loop(max-1,min)
      end
    end



    def factorial(num) do

      if num <=1 do
        1
      else
        result =num*factorial(num-1)
        result
      end
    end

    def fibonacci(num) do

      if num <= 1 do
        num
      else
        result = fibonacci(num-1)+fibonacci(num-2)
        result
      end
    end


    def do_recursion do
      #factorial example
      IO.puts("Factorial Example ")
      num=IO.gets("Enter a number ")|>String.trim
      IO.puts(factorial(String.to_integer(num )))

      ##fibonacci example
      IO.puts("Fibonaaci Example")
      num2=IO.gets("Enter a number : ")|>String.trim
      IO.puts(fibonacci(String.to_integer(num2)))


    end

end


Module8.main()
