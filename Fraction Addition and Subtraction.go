func fractionAddition(expression string) string {
    n := len(expression)
    i := 0
    var numerator, denominator strings.Builder
    num := make([]int, 0)
    den := make([]int, 0)
    look_num := true
    pos := 1
    for i < n {
        c := expression[i]
        if c == '+' || c == '-' {
            if numerator.Len() > 0 {
                k, _ := strconv.Atoi(numerator.String())
                num = append(num, k * pos)
                numerator.Reset()
            } else {
                num = append(num, 0)
            }


            if denominator.Len() > 0 {
                k, _ := strconv.Atoi(denominator.String())
                den = append(den, k)
                denominator.Reset()
            } else {
                den = append(den, 1)
            }

            if c == '+' {
                pos = 1
            } else {
                pos = -1
            }

            look_num = true
        } else if c == '/' {
            look_num = false
        } else if look_num {
            numerator.WriteByte(c)
        } else {
            denominator.WriteByte(c)
        }
        i++
    }

    k, _ := strconv.Atoi(numerator.String())
    num = append(num, k * pos)

    k, _ = strconv.Atoi(denominator.String())
    den = append(den, k)

    n = len(num)
    product := 1
    for _, d := range den {
        if product % d == 0 {
            continue
        }
        product *= d
    }

    summ := 0
    for j := 0; j < n; j++ {
        summ += num[j] * (product / den[j])
    }

    sign := 1
    if summ < 0 {
        sign = -1
        summ *= -1
    }

    for summ % 2 == 0 && product % 2 == 0 {
        summ /= 2
        product /= 2
    }

    j := 3
    for j <= summ && j <= product && summ > 1 && product > 1 {
        if summ % j == 0 && product % j  == 0 {
            summ /= j
            product /= j
        } else {
            j += 2
        }
    }

    return strconv.Itoa(summ * sign) + "/" + strconv.Itoa(product)
}


