##concurrency

defmodule Module11 do

  def main do
    do_concurrency()
  end

  def do_concurrency do

    ##allows multiple blocks of code at once
    ##use spawn

    ## create 2 sepearete process and output
    spawn(fn()->loop(50,1) end )
    spawn(fn()->loop(100,50) end )

    #send messages between processes

    send(self(), {:french ,"lambda"})

    receive do
      ##communicate between processes
      {:german,name } -> IO.puts("Guten tag #{name}")
      {:french,name } -> IO.puts("Bonjour #{name}")
      {:english,name } -> IO.puts("Hello #{name}")

    after
      500 -> IO.puts "Time up"

    end

    ##no meesage then timeout for 500 ms

  end

  def loop(0,_) , do: nil

  def loop(max,min) do
    if max < min do
      loop(0,min)
    else
      IO.puts("Count is:- #{max}")
      loop(max-1,min)
    end
  end


end


Module11.main()
