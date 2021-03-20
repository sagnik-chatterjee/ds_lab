defmodule Module1 do
  @moduledoc """
   @author: Sagnik Chatterjee
   Takes in a name as an input and displays that in standard I/O
  """
  #defines a module ,where elxiir startts reading this
  def main do
    name = IO.gets("Enter your name ..." )
    |> String.trim
    IO.puts("Hello ,#{name}")
  end
end


Module1.main()
