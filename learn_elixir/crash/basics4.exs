##comparing values using elixir
defmodule Module4 do
  def main do
    do_stuff_compare()
    do_logical_operator()
  end

  def do_stuff_compare do

    ##comapring values
    ## == will return true it it looks same
    ## === returns true if the type is also same
    IO.puts("4 == 4.0 : #{4 == 4.0}")
    IO.puts("4 === 4.0 : #{4 === 4.0}")
    IO.puts("4 != 4.0 : #{4 != 4.0}")
    IO.puts("4 !== 4 : #{4 !==4.0}")

    #check for greater than ,less than etc.
    IO.puts( " 5 > 4 : #{5 >4}")
    IO.puts( " 5 >= 4 : #{5 >= 4}")
    IO.puts( " 5 < 4 : #{5 < 4}")
    IO.puts( " 5 <= 4 : #{5 <= 4}")

  end

  def do_logical_operator do
    ##logical ope s if else
      age =16
      IO.puts("Vote and Drive : #{(age >= 16) and (age >= 18)}")
      IO.puts("Vote and Drive : #{(age >= 16) or (age <= 18)}")
      IO.puts not true


  end

end


Module4.main()
