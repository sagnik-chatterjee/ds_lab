## pattern matching
##anonymous functions


defmodule Module7 do
  def main do
    pattern_matching()
    anonymous_functions()
  end

  def anonymous_functions do
    ##anonymous functions have no names and cannot be passed to other functions

    get_sum = fn(x,y) -> x+y end

    IO.puts(" 5 + 5 = #{get_sum.(5,5)}")
    IO.puts(" 10 + 5 = #{get_sum.(10,5)}")


    get_less = &(&1 -&2 - &3)
    IO.puts(" 1 -2 -3 = #{get_less.(1,2,3)}")

    ##function accepting differnet number of params
    add_sum = fn
      {x,y} -> IO.puts("2 args passed , result :- #{x+y}")
      {x,y,z} ->IO.puts("3 args passed , result :- #{x+y+z}")

    end

    add_sum.({1,2,3})
    add_sum.({100,1001})


    ##setting defualt for parameters
    IO.puts do_it()
  end

  def do_it(x \\ 1 , y \\ 1) do
    #gives  x a default value of 1 and y a defualt value of 1
    x+y
  end


  def pattern_matching do
    [length,width]=[20,30]

    IO.puts("Width: #{width}")

    ##pattern patching with the first elemnt with the lsit
    #list inside anohter list
    #[ , [ , a]] = [20, [30, 40]]
    #IO.puts("Get num : #{a}")

  end

end


Module7.main()
