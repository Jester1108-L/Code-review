def expanded_form(num)
  stringNumber = num.to_s()
  out = ""
  index = 0
  while index < stringNumber.length
    out = out + stringNumber[index]
    numZero = 0
    while numZero < stringNumber.length - index - 1
      out = out + "0"
      numZero += 1
    end
    if index < stringNumber.length - 1
      out = out + "+"
    end
    index += 1
  end
  print(out)
end

expanded_form(2252255)
