##some of the functional inbuilt datastructues in elixir
defmodule Module6 do
  def main do
    tuples_use()
    lists_use()
    map_use()
  end

  def map_use do
    capitals= %{"Alabama"=> "Montgomery",
      "Alaska" => "Juneau",
      "Arizona" => "Phoenix",
      "California" => "San Diego"

  }

  IO.puts("Capital of alaska is:  #{capitals["Alaska"]}")

  capitals2= %{alabama: "Montmegory",
  alaska: "Juneua",arizona: "Phoenix"

  }
  IO.puts("Capital of arizona is : #{capitals2.arizona }")

  #dict is deprecated use Map
  ##capitals3= Dict.put_new(capitals,"Arkansas","Little Rock")


  end



  def display_list_recur([word| words]) do
    IO.puts word
    display_list_recur(words)

  # recursively inserts and deletes element at list
  #  IO.puts display_list_recur(List.delete_at(words,1))
  #  IO.puts display_list_recur(List.insert_at(words,4,"ok!"))

  #get first item in list
  IO.puts List.first(words)
  #prints the last item in the list
  IO.puts List.last(words)

  my_stats=[name: "Derek",height: 5.78]


  end

  def display_list_recur([]), do: nil
    ##base case to break off


  def lists_use do
    list1=[1,2,3]
    list2=[4,5,6]

    #concateniating 2 lists
    list3 = list1 ++ list2

    #subtract a list from another list
    list4 =list3 -- list1

    ## check if 6 in list4
    IO.puts(6 in list4)

    #subtract the head of the list
    [head | tail ] = list3
    IO.puts("Head : #{head}")

    ##output data using write i.e without newline
    IO.write("Tail: ")
    IO.inspect tail

    ##converting the number as from ascii char
    IO.inspect [97,98] , char_lists: :as_lists

    ##enumerate over lsists

    Enum.each tail ,fn item ->
      IO.puts item
    end

    words = ["Random","Words","in","a","List"]
    Enum.each  words ,fn word ->
      IO.puts word
    end
    IO.puts("Prints recusrviely")
    display_list_recur(words)

  end

  def tuples_use do
    ##not supposed for enumerating in them
    my_stats = {175, 6.25,:Sagnik}

    #cant directly print tuple
    #so we first convert the tuple into a list
    #and then make the list into a bitstring which can be printed
    IO.puts(my_stats|> Tuple.to_list |> Enum.join(","))

    IO.puts("Is it a tuple ? #{is_tuple(my_stats)}")

    my_stats2= Tuple.append(my_stats,42)
    IO.puts("Age :- #{elem(my_stats2,3)}")

    ##tuple size
    IO.puts("Tuple size :- #{tuple_size(my_stats2)}")

    #delete value at index
    my_stats3 =Tuple.delete_at(my_stats2,2)

    #insert value at index
    my_stats4 =Tuple.insert_at(my_stats3,0,1974)

    #duplicating a tupel
    many_zeros = Tuple.duplicate(0,5)

    #pattern matching using tuples

    {weight,height,name} = {175,6.35,"lambda"}
    IO.puts("Weight : #{weight}")


  end

end


Module6.main()
