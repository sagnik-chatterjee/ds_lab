defmodule HelloWorld do
  def say_hi do
      IO.puts("Hello world")
  end
end

defmodule Greeter2 do
  def hello(%{name: person_name} = person)do
    IO.puts("Hello "<> person_name)
    IO.inspect(person)
  end
end


HelloWorld.say_hi
#Greeter2.hello("sagnik")

IO.puts(1+1)
