## list comprehensions
##exception handling

defmodule Module10 do

  def main do
    list_comprehension()
    exception_handling()
  end

  def exception_handling do

    err =try do
      5/ 0

    rescue
      ArithmeticError -> "Can't divide by 0."
    end

    IO.puts err

  end

  def list_comprehension do

    dbl_list= for  n <- [1,2,3,4,5,6], do: n*2
    IO.inspect(dbl_list)
    even_list= for n <- [1,2,3,4,5,6,7,8,123,123,123,33,1,2313,1,312,325233,5324,9] ,do: rem(n,2)===0
    IO.inspect(even_list)

  end

end


Module10.main()
