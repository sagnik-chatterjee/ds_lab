defmodule Module2 do
  def main do
    data_stuff()
    do_stuff_strings()
  end

  def data_stuff do
    ## int type
    my_int =12345 ##no maxint size like in python3
    IO.puts("#{my_int}")
    IO.puts("Is this type of data int  : #{is_integer(my_int)} ")

    ##flaot stuff
    my_float = 3.14159
    IO.puts("#{my_float}")
    IO.puts("Is this type of data float : #{is_float(my_float)} ")

    ##atoms
    #Atom are constants whose values are thier own name
    # Often used to enumerate over distinct values
    # Atoms are equal is their names are equal
    IO.puts("Is this atom: #{is_atom(:Pittsburgh)}")
    :"NewYork"
    #prefix a vairbale with underscore means that it is not meant to be used
    _one_to_10 =1..10
  end

  ##strings
  def do_stuff_strings do

    my_str= "My sentence"
    IO.puts("Length of the string : #{String.length(my_str)}")

    ##combining the strings
    #concatenate
    longer_string=my_str<> " "<> " is a longer string "
    IO.puts("Longer strings is : #{longer_string}")

    ##chekc if they string values and datatypes are qual as well(kind of like javascript)
    IO.puts(" Are the two strings Equal : #{"Egg" === "egg" }")


    #check if string contains anohter string

    IO.puts("To check if My is present in my_str ? #{String.contains?(my_str,"My")} ")

    #return the very first character
    IO.puts("First : #{String.first(my_str)}")


    #character at index 4
    IO.puts("Index 4 char : #{String.at(my_str,4)} ")

    #Substring
    IO.puts("Substring used : #{String.slice(my_str,3,8)}")

    #inspect --> print the internal reper of value
    IO.inspect(String.split(longer_string, " "))

    #revesing the string
    IO.puts(String.reverse(longer_string))

    ##uppercase
    IO.puts(String.upcase(longer_string))

    #lowercase
    IO.puts(String.downcase(longer_string))

    #capitalize sthe string
    IO.puts(String.capitalize(longer_string))

    ## pipes values from one thing to another
    #40 piped to differnt function to print it
    4 * 10 |> IO.puts
  end


end


Module2.main()
