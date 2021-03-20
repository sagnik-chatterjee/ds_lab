##enumerables in elixir

defmodule Module9 do

  def main do
    call_enumarable()
  end

  def call_enumarable do
    ## enumerable is a datatype that allows its datatype to be counted of
    IO.puts("Even List:- #{Enum.all?([1,2,3,4,5,6,7,8,9,10],
      fn(n)-> rem(n,2) == 0 end
    )}")

    IO.puts("Even List:- #{Enum.any?([1,2,3,4,5,6,7,8,9,10],
      fn(n)-> rem(n,2) == 0 end
    )}")

    #print the list using enum
    Enum.each([1,2,3,4,5,6,7,8,9,10],fn(n)-> IO.puts("Element is:- #{n}") end)

    dbl_list= Enum.map([1,2,3,4,5],fn(n)->IO.puts("Doubled it :#{n*2}") end)

    sum_vals = Enum.reduce([1,2,3],fn(n,sum)-> n+sum  end )
    IO.puts("Total sum : #{sum_vals}")

    #printsthe unique elemnts in the list
    IO.inspect Enum.uniq([1,2,2,4,5,1])


  end

end


Module9.main()
