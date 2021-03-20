##mathematically doing things with elixir

defmodule Module3 do
  def main do
    do_maths_stuff()
  end

  def do_maths_stuff do
      #simple maths thigns
      #addn
      IO.puts("5 + 4 = #{5+4}")
      #subtraction
      IO.puts("5 - 4 = #{5-4}")
      #multiplication
      IO.puts("5 * 4 = #{5*4}")
      #division
      IO.puts("5 / 4 = #{5/4}")
      #integer division
      IO.puts("1234 div 4 = #{div(5,4)}")
      #remainder
      IO.puts("123 rem 4 = #{rem(5,4)}")

      


  end


end


Module3.main()
