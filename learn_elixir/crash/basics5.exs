##decision making and logics
defmodule Module5 do
  def main do
    decision_making()
    do_stuff_2()
  end

  def do_stuff_2 do
      age =16

      #like switch stmt
      case  2 do
        1 -> IO.puts("Entered 1 ")
        2 -> IO.puts("Entered 2")
        _ -> IO.puts("Nothing !!!!")
      end

      ##ternary operator
      IO.puts("Ternary Operator")
      IO.puts("#{if age>18 , do: IO.puts("Ok"), else: IO.puts("Not ok")}")
  end

  def decision_making do

    age = 16

    if age >=18 do
      IO.puts("Can vote")
    else
      IO.puts("Cant vote")

    end

    unless age === 18 do ##like while age != 18
      IO.puts("Youre not 18")

    else
      IO.puts("You are 18")
    end

    cond do
      age >= 14 -> IO.puts("You can wait")
      age >= 16 -> IO.puts("You can drive")
      age >= 18 -> IO.puts("Can Vote")
      true -> IO.puts("Default action that needs to de done")
    end

  end
end


Module5.main()
